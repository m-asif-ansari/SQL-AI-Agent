# Importing Additional Python Libraries
import streamlit as st
import sqlite3
import os
import pandas as pd
import time

# Importing Local Python Modules
from backend.db.db import save_uploaded_file, get_db_object
from backend.llm_list.get_llm_list import get_llm_list
from backend.agent.init_llm import init_llm
from backend.agent.init_agent import init_agent
from backend.agent.get_agent_response import get_agent_response

# Customizing the Streamlit Page
st.set_page_config(
    page_title="SQL-Agent",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://github.com/m-asif-ansari/SQL-AI-Agent',
        'About': "# This is a SQL-Agent. Made by- Asif Ansari"
    }
)

# Displaying the logo
st.logo("assets\\static\\logo.png", size="large")

# Page Title and Subtitle
st.title("SQLite AI Agent")
st.subheader("Ask questions about your SQLite database")

# Check if a file has been uploaded
if "input_file" not in st.session_state:
    st.error("Please upload a file to get started")
else:
    st.success(f"The Agent is currently working on {st.session_state.input_file['file'].name} database.")

# Sidebar customization
st.sidebar.title("SQLite AI Agent")
st.sidebar.write(
    "This is a simple SQLite AI agent that can fetch records from a SQLite database or a CSV file using natural language."
)

# File upload dialog
@st.dialog("File Upload")
def upload_file_dialog(file_type):
    """
    Handle file uploads for CSV or SQLite files.

    Args:
        file_type (str): The type of file to upload ("CSV" or "SQLITE").
    """
    st.write(f"Please upload your {file_type} file below.")
    st.write("This will be used as the input for the AI agent.")

    # File uploader widget
    if file_type.lower() == "csv":
        file = st.file_uploader("Upload CSV File", type=["csv"], key="csv_file")
    else:
        file = st.file_uploader("Upload SQLite Database", type=["sqlite", "db"], key="db_file")

    # Handle file submission
    if st.button("Submit"):
        try:
            file_path = save_uploaded_file(file)
            st.success("File uploaded to server.")
            st.session_state.input_file = {"file_type": file_type, "file": file, "file_path": file_path}
            st.session_state.db_object = get_db_object(file_path)
            st.rerun()  # Refresh the app to reflect the uploaded file
        except Exception as e:
            st.error(f"Error uploading the file to server: {e}")

# Sidebar options for file upload
st.sidebar.divider()
st.sidebar.write("Upload a file to get started")
st.sidebar.write("Please select a file type to upload:")
if st.sidebar.button("CSV File"):
    upload_file_dialog("CSV")
if st.sidebar.button("SQLite Database"):
    upload_file_dialog("SQLITE")
st.sidebar.divider()

# LLM selection
model_list = get_llm_list()
model_selection = st.sidebar.selectbox("Select LLM", model_list)
st.sidebar.write("This will be used as the LLM for the AI agent.")
st.sidebar.divider()

# Initialize the selected LLM
model_name = model_selection.split(" ")[0]
llm = init_llm(model_name)

# Initialize the SQL agent if a database object exists
if "db_object" in st.session_state:
    db = st.session_state.db_object
    sql_agent = init_agent(db, llm)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "How can I assist you?"}]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Function to generate a response with a delay for streaming effect
def response_generator(response):
    """
    Generate a response word by word with a delay for a streaming effect.

    Args:
        response (str): The full response to be streamed.

    Yields:
        str: The next word in the response.
    """
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.03)

# Chat input and response handling
if "input_file" not in st.session_state:
    st.chat_input("Upload a CSV or SQLite file to start a conversation with the Agent", disabled=True)
else:
    # React to user input
    if prompt := st.chat_input("Enter your query here!"):
        # Display user message in chat message container
        st.chat_message("user").markdown(prompt)
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.spinner("Generating response...", show_time=True):
            try:
                # Get the response from the SQL agent
                response = get_agent_response(sql_agent, prompt)
            except Exception as e:
                response = f"Facing issues with SQL Agent. Try using a different Base LLM. Error: {e}"
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.write_stream(response_generator(response))
        # Add assistant response to chat history
        st.session_state.messages.append({"role": "assistant", "content": response})

