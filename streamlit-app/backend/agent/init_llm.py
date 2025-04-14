from langchain_groq import ChatGroq
from dotenv import load_dotenv

def init_llm(model_name: str) -> ChatGroq:
    """
    Function to initialize the LLM model to be used as the base LLM for the SQL Agent.

    Args:
        model_name (str): Name of the LLM to initialize as the base LLM.

    Returns:
        llm (ChatGroq): A ChatGroq runnable object for the given LLM name input.
    """
    # Load environment variables from the .env file to access the Groq API key
    load_dotenv()

    # Initialize the LLM runnable with the specified model name
    llm = ChatGroq(
        model=model_name
    )

    return llm