import sqlite3

# Create a connection to the database
connection = sqlite3.connect('diary.db')

def create_table():
    with connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS diary (
            id INTEGER,
            date TEXT NOT NULL,
            time TEXT NOT NULL,
            topic TEXT NOT NULL UNIQUE,
            event TEXT NOT NULL,
            PRIMARY KEY (id AUTOINCREMENT)
        );
        """)

def input_data(date, topic, event):
    with connection:
        connection.execute("""
        INSERT INTO diary (date, time, topic, event)
        VALUES (?,CURRENT_TIMESTAMP,?,?);
        """, (date, topic, event))

def view_every_entry():
    with connection:
        cursor = connection.execute("""
            SELECT * FROM diary;
        """)
    record = cursor.fetchall()  # fetchall method converts a cursor object to a list of tuples
    return record

def view_single_entry(topic):
    with connection:
        cursor = connection.execute("""
            SELECT * FROM diary
            WHERE topic =?;
        """, (topic,))
    record = cursor.fetchall()
    return record

def modify_entry(topic, new_date, new_topic, new_event):
    with connection:
        connection.execute("""
        UPDATE diary
        SET date = ?, topic = ?, event = ?
        WHERE topic = ?;
        """, (new_date, new_topic, new_event, topic))

# create_table()
# print(view_every_entry())
# print(view_single_entry('How to make money'))