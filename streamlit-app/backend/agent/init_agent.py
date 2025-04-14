from langgraph.prebuilt import create_react_agent
from backend.tools.get_sql_tools import get_sql_tools
from langchain_community.utilities import SQLDatabase
from langchain_groq import ChatGroq

def init_agent(db: SQLDatabase, llm: ChatGroq):
    """
    Function to initialize the SQL Agent with the input database object and LLM runnable.

    Args:
        db (SQLDatabase): The SQLDatabase object representing the SQLite database.
        llm (ChatGroq): The ChatGroq LLM object to be used as the base LLM.

    Returns:
        sql_agent: The initialized SQL Agent object.
    """
    
    # Retrieve the tools required for interacting with the database
    tools = get_sql_tools(db, llm)

    # Define the system message for the agent's behavior and instructions
    system_message = f"""
    You are an agent designed to interact with a SQL database. 
    Analyze the input and provide answers appropriately.
    If the input is regarding the SQLite database, create a syntactically correct SQLite query to run, 
    then look at the results of the query and return the answer using appropriate tools.

    Guidelines:
    - Unless the user specifies a specific number of examples, always limit your query to at most 10 results.
    - Order the results by a relevant column to return the most interesting examples in the database.
    - Never query for all the columns from a specific table; only ask for the relevant columns given the question.
    - Use only the tools provided below to interact with the database.
    - Double-check your query before executing it. If you encounter an error, rewrite the query and try again.
    - Do NOT make any DML statements (INSERT, UPDATE, DELETE, DROP, etc.) to the database.

    Steps:
    1. Always start by looking at the tables in the database to see what you can query. Do NOT skip this step.
    2. Query the schema of the most relevant tables.
    3. Show the output in Markdown tables.

    Tools to be used:
    {tools}
    """

    # Create the SQL Agent using the provided LLM, tools, and system message
    sql_agent = create_react_agent(llm, tools, prompt=system_message)

    return sql_agent
