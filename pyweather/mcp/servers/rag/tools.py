import os
# LangChain imports for RAG pipeline
# to convert text to vectors.
from langchain_google_genai import GoogleGenerativeAIEmbeddings
# to read the document
from langchain_community.document_loaders import TextLoader
# to chunk the document.
from langchain_text_splitters import RecursiveCharacterTextSplitter
# to act as our vector store.
from langchain_chroma import Chroma
from chromadb import Settings

from pyweather.mcp.servers.rag.server import mcp
from pyweather.mcp.servers.rag.config import CHROMA_PERSIST_DIR


@mcp.tool()
def ingest_document(file_path: str) -> str:
    """
    Loads a document from a file path, splits it into chunks, generates
    embeddings using Google's model, and stores them in a persistent
    Chroma vector store for later retrieval.

    This tool is the first step in the RAG pipeline. It prepares the knowledge
    base that can be queried by another tool.

    Args:
        file_path: The absolute or relative path to the text document.
                   For example: "/usercode/Guides/employee_handbook.txt".

    Returns:
        A string confirming the successful ingestion and the number of chunks processed,
        or an error message if the process fails.
    """
    # 1. Validate that the file path exists before proceeding.
    if not os.path.exists(file_path):
        return f"Error: The file at path '{file_path}' was not found."

    try:
        # 2. Initialize the embedding model.
        # We use a Google Gemini embedding model for consistency with the agent's LLM
        embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key="{{GOOGLE_GEMINI_API_KEY}}")

        # 3. Load the document content from the specified path
        loader = TextLoader(file_path, encoding='utf-8')
        documents = loader.load()

        # 4. Split the document into smaller, more manageable chunks
        # This is crucial for effective retrieval, as it provides more granular context
        # The Q&A format of the source doc is well-suited for this
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,  # The maximum size of a chunk in characters
            chunk_overlap=200 # Overlap helps maintain context between chunks
        )
        chunks = text_splitter.split_documents(documents)

        if not chunks:
            return "Error: Could not extract any text chunks from the document. The file might be empty."

        # 5. Ingest the chunks into the Chroma vector store
        # The `from_documents` class method is a convenient way to handle the
        # embedding and storage process in one step
        # It is configured to save the data to the specified persistent directory
        vector_store = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=CHROMA_PERSIST_DIR,
            client_settings=Settings(anonymized_telemetry=False)
        )

        file_name = os.path.basename(file_path)
        return f"Successfully ingested the document from '{file_name}' into the vector store."

    except Exception as e:
        # Catch-all for any other errors during the process
        print(f"An error occurred: {e}")
        return f"An unexpected error occurred during document ingestion: {e}"


@mcp.tool()
def query_rag_store(query: str) -> str:
    """
    Queries the persistent Chroma vector store to find the most relevant
    document chunks for a given user query.

    This tool loads the existing vector database, performs a similarity search,
    and returns the combined text of the most relevant chunks.

    Args:
        query: The user's question or search term (e.g., "how do I apply for leave?").

    Returns:
        A string containing the concatenated content of the most relevant document
        chunks, or an error/status message if no relevant information is found.
    """
    # 1. Check if the vector store has been created by the ingest tool
    if not os.path.exists(CHROMA_PERSIST_DIR):
        return "Vector store not found. Please run the 'ingest_document' tool first to create the knowledge base."

    try:
        # 2. Initialize the same embedding model used for ingestion
        # This is crucial for the similarity search to work correctly
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/embedding-001",
            google_api_key="{{GOOGLE_GEMINI_API_KEY}}"
        )

        # 3. Load the persistent vector store from disk
        vector_store = Chroma(
            persist_directory=CHROMA_PERSIST_DIR,
            embedding_function=embeddings,
            client_settings=Settings(anonymized_telemetry=False)
        )

        # 4. Perform the similarity search
        # This will embed the query and find the top 'k' most similar chunks
        # k=3 is a good number to provide sufficient but not overwhelming context
        results = vector_store.similarity_search(query, k=3)

        # 5. Process and return the results
        if not results:
            return "No relevant information was found in the document for your query."

        # Combine the content of the found documents into a single string for the agent
        # Using a separator helps the LLM distinguish between different retrieved chunks
        context = "\n---\n".join([doc.page_content for doc in results])

        return context

    except Exception as e:
        print(f"An error occurred during query: {e}")
        return f"An unexpected error occurred while querying the vector store: {e}"
