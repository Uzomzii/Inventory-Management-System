import sqlite3

connection = sqlite3.connect("gui.db")

def create_table():
    with connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS register
        (
            id INTEGER,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            phone TEXT NOT NULL UNIQUE,
            PRIMARY KEY(id AUTOINCREMENT)
        );
        """)

def insert_input(first_name, last_name, phone):
    with connection:
        connection.execute("""
        INSERT INTO register (first_name, last_name, phone)
        VALUES (?, ?, ?)
        """, (first_name, last_name, phone))