import requests
import os
from dotenv import load_dotenv


def get_llm_from_groq() -> list:
    """
    Fetch the list of available LLMs from the GROQ API.
    
    Args: No Inputs

    Returns: 
        model_list (List<str>) : returns a list of active LLMs from the Groq servers

    Note:
        Not using this function in deployment as Groq returns the list of all active LLMs.
        The list contains even the embeddings, images generations, preview, unstable LLMs which cannot be used as an agent.
    """

    # Loading the env file to initialize the Groq API
    load_dotenv()

    # Ensure the API key is set in the environment variables
    if "GROQ_API_KEY" not in os.environ:
        raise ValueError("GROQ_API_KEY environment variable is not set.")

    # Set up the request parameters
    api_key = os.environ.get("GROQ_API_KEY")
    url = "https://api.groq.com/openai/v1/models"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    # sending the get request to groq
    response = requests.get(url, headers=headers)

    # Initializing empty list to store the formatted data from groq api
    model_list = []

    # looping over the response data
    for i in response.json().get("data"):
        # formatting the LLMs name with their parent company for better understanding
        model = f"{i.get("id")} FROM- {i.get("owned_by")}"

        # Appending the model names in the model list variable
        model_list.append(model)
    
    # sorting the list for better visibility
    model_list.sort()

    # printing the LLMs list in terminal 
    for i in model_list:
        print(i)

    # returning the model list variable
    return model_list


def get_llm_list() -> list:
    """
    Returns the list of LLMs which is pre-defined by the admin.
    
    Args: No Inputs

    Returns: 
        model_list (List<str>) : returns a list of currently active LLMs that can be used with the Groq Api

    Note:
        This list should only contain LLMs that have Tools/ Function calling ability so that they can be used as Agents.
    """

    model_list = [
        "llama-3.1-8b-instant",
        "llama-3.3-70b-versatile",
        "meta-llama/llama-4-scout-17b-16e-instruct",
        "meta-llama/llama-4-maverick-17b-128e-instruct",
        "llama3-70b-8192",
        "llama3-8b-8192",
        "deepseek-r1-distill-qwen-32b",
        "deepseek-r1-distill-llama-70b",
        "gemma2-9b-it",
        "qwen-qwq-32b",
        "qwen-2.5-coder-32b",
        "qwen-2.5-32b",
    ]
    return model_list

if __name__ == "__main__":
    print("List of available models - ", get_llm_list())