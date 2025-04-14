from langchain_community.agent_toolkits import SQLDatabaseToolkit

def get_sql_tools(db, llm):
    """
    Function to retrieve the necessary SQL tools for interacting with the database.

    Args:
        db: The SQLDatabase object representing the database.
        llm: The LLM object to be used for generating queries and interacting with the database.

    Returns:
        list: A list of tools for interacting with the database, including:
              - Tool to list tables in the database.
              - Tool to get the schema of a table.
              - Tool to query the database.
    """
    # Initialize the SQLDatabaseToolkit with the database and LLM
    toolkit = SQLDatabaseToolkit(db=db, llm=llm)

    # Retrieve all tools from the toolkit
    tools = toolkit.get_tools()

    # Extract specific tools by their names
    list_tables_tool = next(tool for tool in tools if tool.name == "sql_db_list_tables")
    get_schema_tool = next(tool for tool in tools if tool.name == "sql_db_schema")
    db_query_tool = next(tool for tool in tools if tool.name == "sql_db_query")

    # Filter and return only the required tools
    tools = [list_tables_tool, get_schema_tool, db_query_tool]

    # Debugging: Print the tools for verification
    for tool in tools:
        print(f"Tool Loaded: {tool.name}")

    return tools