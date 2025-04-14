from langchain_community.utilities import SQLDatabase
import os
import pandas as pd
from sqlalchemy import create_engine
from pathlib import Path

def save_uploaded_file(file) -> str:
    """
    Function to save the uploaded CSV file or SQLite database file to the asset folder as a SQLite file 
    and return the path of the file.

    Args:
        file (st.UploadedFile): FileUploader object of the uploaded CSV/SQLite/DB file.

    Returns:
        str: Path of the saved file.

    Note:
        - If the uploaded file is of type SQLite/DB, the function saves the file directly to the assets folder.
        - If the uploaded file is of type CSV, the function converts the CSV file to SQLite using pandas and then saves it.
        - If the file type is unsupported, a default SQLite file path is returned.
    """

    file_name = Path(file.name)
    file_extension = file_name.suffix.lower()  # Get the file extension in lowercase
    print("File Extension:", file_extension)

    # Handle CSV files
    if file_extension == '.csv':
        print("Converting CSV to SQLite database")
        table_name = "data"  # Table name when saving the data in sqlite
        backend_folder = "assets\\db"
        os.makedirs(backend_folder, exist_ok=True)  # Ensure the folder exists

        # Define the SQLite database file path
        csv_file_name = os.path.splitext(file.name)[0]
        db_file_path = os.path.join(backend_folder, f"{csv_file_name}.db")

        # Read the uploaded CSV file into a DataFrame
        df = pd.read_csv(file)

        # SQlite Engine to handle sqlite file 
        engine = create_engine(f'sqlite:///{db_file_path}')

        # Save the DataFrame to the SQLite database
        df.to_sql(table_name, engine, if_exists="replace", index=False)

        return db_file_path

    # Handle SQLite/DB files
    elif file_extension in [".sqlite", ".db"]:
        print("Saving the SQLite/DB file directly")
        backend_folder = "assets\\db"
        os.makedirs(backend_folder, exist_ok=True)  # Ensure the folder exists
        file_path = os.path.join(backend_folder, file.name)

        # Save the uploaded file
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())

        return file_path

    # Handle unsupported file types
    else:
        print("Unsupported file type. Using default SQLite file.")
        return "assets/db/Chinook.db"


def get_db_object(file_path: str) -> SQLDatabase:
    """
    Function to create and return a SQLDatabase object from a SQLite file.

    Args:
        file_path (str): Path to the SQLite database file.

    Returns:
        SQLDatabase: An instance of SQLDatabase connected to the given SQLite file.
    """
    # Creating the instance of given sqlite file
    db = SQLDatabase.from_uri(f"sqlite:///{file_path}")
    
    return db