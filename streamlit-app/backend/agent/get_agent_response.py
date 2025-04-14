from langgraph.prebuilt import create_react_agent

def get_agent_response(agent: create_react_agent, prompt: str) -> str:
    """
    Function to get a response from the agent based on the provided prompt.

    Args:
        agent (create_react_agent): The initialized agent object capable of processing the prompt.
        prompt (str): The user input or query to be processed by the agent.

    Returns:
        str: The content of the agent's response.
    """
    # Invoke the agent with the user prompt and retrieve the response
    response = agent.invoke({"messages": [{"role": "user", "content": prompt}]})

    # Debugging: Print each message in the response
    for message in response["messages"]:
        print(message)

    # Return the content of the last message in the response
    return response["messages"][-1].content