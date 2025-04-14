# SQL AI Agent

## Overview

The SQL AI Agent is a Python-Streamlit web-based application that leverages AI to interact with SQLite databases and CSV files. It allows users to ask natural language questions about their data and receive responses directly from the application.

The SQL AI Agent is built using the following technologies and modules:
- **Python** - Used as the primary programming language for the application.

- **Streamlit** - Used to create the web-based user interface and handle front-end interactions.

- **LangChain** - Used for building language models and generating SQL queries from user input.

- **LangGraph** - Used for graph-based natural language processing and for building the agent's understanding of the input data.

- **GROQ's APIs** - Used for advanced language model capabilities and integration with various open-sourced LLMs provided by Groq Cloud.

- **SQLite** - Used as the lightweight disk-based database for storing and querying data.

- **SQLite3 Python Library** - Used to interact with SQLite databases from Python.

- **Pandas** - Used for data manipulation and analysis, particularly for handling CSV files.

- **Git / GitHub** - Used for version control and for hosting the source code and managing the repository.

## Features

- **Natural Language Querying**: Ask questions in plain English, and the agent will generate and execute SQL queries to fetch the required data.
- **CSV and SQLite Support**: Upload CSV files or SQLite databases as input for the agent.
- **Interactive Chat Interface**: Engage with the agent through a chat-based interface.
- **Customizable LLMs**: Choose from a list of supported language models to power the agent.
- **Secure and Efficient**: Ensures safe interaction with the database by restricting destructive SQL operations (e.g., `INSERT`, `UPDATE`, `DELETE`).


## Getting Started

## Installation

### Prerequisites

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/) installed
- SQLite installed (optional, for local database testing)

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/m-asif-ansari/SQL-AI-Agent.git
   cd SQL-AI-Agent
   ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. Install the required dependencies:
    ```bash 
    pip install -r requirements.txt
    ```

4. Start the Streamlit application:
    ```bash
    cd streamlit-app
    streamlit run app.py
    ```

### Usage

1. Generate your GROQ API KEY:
    - Create a account on [Groq](https://groq.com).
    - Generate your free Groq API Key.
    - Create a .env file as per the sample .env.example file.
    - Paste your Groq API key in env file. 

2. Open the Application:
    - Start the Streamlit app
    - Open your web browser and navigate to the URL provided by Streamlit (usually http://localhost:8501).

2. Upload a File:
    - Click on the "CSV File" or "SQLite Database" button in the sidebar to upload a file.
    - Follow the instructions to upload the file.

3. Select an LLM:
    - Use the dropdown in the sidebar to select a language model.

4. Start a Conversation:
    - Enter your query in the chat input box and press Enter.
    - The agent will interpret your query and provide a response.


## Directory Structure

```markdown
sql-agent/
│
├── streamlit-app/
│   ├── app.py                     # Main Streamlit app
│   ├── backend/
│   │   ├── db/
│   │   │   └── db.py              # Handles file uploads and database interactions
│   │   ├── agent/
│   │   │   ├── init_llm.py        # Initializes the LLM
│   │   │   ├── init_agent.py      # Initializes the SQL agent
│   │   │   └── get_agent_response.py # Handles agent responses
│   │   ├── tools/
│   │   │   └── get_sql_tools.py   # Retrieves SQL tools for database interaction
│   │   ├── llm_list/
│   │   │   └── get_llm_list.py    # Provides a list of available LLMs
│   │    
│   └── assets/
│       ├── db/                    # Stores uploaded database files
│       └── static/                # Static assets (e.g., logo)
│           └── logo.png           # Logo for the application
│           
│
├── requirements.txt               # Python dependencies
├── README.md                      # Project documentation
├── .env                           # Environment variables
├── .env.example                   # Sample Env File
└── LICENSE                        # Open-Source License of Repo
```


## Credits

### Author:
- Mohd Asif Ansari 
- Github - [m-asif-ansari](https://github.com/m-asif-ansari)
- Gmail - [asif16907@gmail.com](mailto:asif16907@gmail.com)

### License:
- This project is licensed under the MIT License. See the [LICENSE](https://github.com/m-asif-ansari/SQL-AI-Agent/blob/main/LICENSE) file for details.
- Contributions are welcome! Please open an issue or submit a pull request if you find any bugs or have suggestions for improvements.
