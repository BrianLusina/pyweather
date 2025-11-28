from typing import List
import os
from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver
from langgraph.prebuilt import tools_condition, ToolNode

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

from app.clients.mcp.langchain.entities import State

google_api_key = os.getenv("GOOGLE_GEMINI_API_KEY")


async def create_graph(tools: List):
    # LLM configuration
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.0-flash", temperature=0, google_api_key=google_api_key
    )
    llm_with_tools = llm.bind_tools(tools)

    # Prompt template with user/assistant chat only
    prompt_template = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant with multiple roles. You have access to tools for checking the weather, "
                "managing a to-do list and access to RAG tools."
                "Use the tools when necessary based on the user's request."
                "Your role is to answer questions using the content of documents provided by the user. When a user "
                "gives you a file path, use your tool to ingest it into your memory. When they ask a question, use "
                "your search tool to find the relevant context within the ingested documents and use that context to "
                "form a clear answer.",
            ),
            MessagesPlaceholder("messages"),
        ]
    )

    chat_llm = prompt_template | llm_with_tools

    # Define chat node
    def chat_node(state: State) -> State:
        state["messages"] = chat_llm.invoke({"messages": state["messages"]})
        return state

    # Build LangGraph with tool routing
    graph = StateGraph(State)
    graph.add_node("chat_node", chat_node)
    graph.add_node("tool_node", ToolNode(tools=tools))
    graph.add_edge(START, "chat_node")
    graph.add_conditional_edges(
        "chat_node", tools_condition, {"tools": "tool_node", "__end__": END}
    )
    graph.add_edge("tool_node", "chat_node")

    return graph.compile(checkpointer=MemorySaver())
