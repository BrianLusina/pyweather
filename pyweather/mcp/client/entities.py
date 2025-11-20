from typing_extensions import TypedDict
from typing import Annotated, List
from langgraph.graph.message import AnyMessage, add_messages


# LangGraph state definition
class State(TypedDict):
    messages: Annotated[List[AnyMessage], add_messages]
