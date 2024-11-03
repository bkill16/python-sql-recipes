import sqlite3
import os

DATABASE_NAME = "recipes.db"

def get_connection():
    """Establishes and returns a connection to the SQLite database."""
    connection = sqlite3.connect(DATABASE_NAME)
    connection.row_factory = sqlite3.Row 
    connection.execute("PRAGMA foreign_keys = ON;")  # Enforce foreign keys
    return connection

def initialize_database():
    """Initializes the database by creating tables if they don't exist."""
    with get_connection() as connection:
        with open(os.path.join(os.path.dirname(__file__), "schema.sql"), "r") as f:
            connection.executescript(f.read())

initialize_database()