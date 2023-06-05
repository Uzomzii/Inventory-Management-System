import sqlite3

connection = sqlite3.connect("inventory.db")

def create_table():
    with connection:
        connection.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            item_id INTEGER NOT NULL,
            item_name TEXT NOT NULL,
            item_quantity INTEGER NOT NULL,
            item_price NUMERIC NOT NULL,
            PRIMARY KEY(item_id AUTOINCREMENT)
        )
        """)
# create_table()

def submit_entry(item_name, item_quantity, item_price):
    with connection:
        connection.execute("""
        INSERT INTO inventory (item_name, item_quantity, item_price)
        VALUES(?,?,?)
        """, (item_name, item_quantity, item_price))

def view_entry():
    with connection:
        cursor = connection.execute("SELECT * FROM inventory")
    return cursor.fetchall()

# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from ttkbootstrap.scrolled import ScrolledText

# app = ttk.Window()

# # scrolled text with autohide vertical scrollbar
# st = ScrolledText(app, padding=5, height=10, autohide=True)
# st.pack(fill=BOTH, expand=YES)

# # add text
# st.insert(END, 'Insert your text here.')

# app.mainloop()