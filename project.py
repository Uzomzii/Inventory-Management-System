import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from project_database import submit_entry, view_entry, create_table
from ttkbootstrap.scrolled import ScrolledText

create_table()

root = ttk.Window(themename='darkly')
root.title("Inventory Management System")

root.geometry("500x400")

# Create Labels for Item Name, Price and Quantity

item_label = ttk.Label(root, text="Item Name")
item_label.grid(column=0, row=0, pady=5, padx=5, sticky="W")

quantity_label = ttk.Label(root, text="Quantity")
quantity_label.grid(column=0, row=1, pady=5, padx=5, sticky="W")

price_label = ttk.Label(root, text="Price(=N=)")
price_label.grid(column=0, row=2, pady=5, padx=5, sticky="W")

# Create Entry widget for Item name, Price and Quantity

item_entry = ttk.Entry(root, width=30)
item_entry.grid(column=1, row=0, sticky="W", padx=5, pady=5)

quantity_entry = ttk.Entry(root, width=30)
quantity_entry.grid(column=1, row=1, sticky="W", padx=5, pady=5)

price_entry = ttk.Entry(root, width=30)
price_entry.grid(column=1, row=2, sticky="W", padx=5, pady=5)

def receive_input():
    item_name = item_entry.get()
    item_quantity = quantity_entry.get()
    item_price = price_entry.get()

    submit_entry(item_name, item_quantity, item_price)

    # Clear the values from the entry widget
    item_entry.delete(0, END)
    quantity_entry.delete(0, END)
    price_entry.delete(0, END)

submit_button = ttk.Button(root, text="Submit Data", command=receive_input)
submit_button.grid(column=0, row=3, padx=10, pady=5)


display = ScrolledText(root, height=10, width=70, fg="White")
display.grid(column=0, row=4, columnspan=2, sticky="W"+"E", padx=25, pady=5)

def display_query():
    records = view_entry()
    for record in records:
        display.insert(END, record)
    # return records

display_button = ttk.Button(root, text="Display Inventory", command=display_query)
display_button.grid(column=0, row=5, padx=10, pady=5)

root.mainloop()
# print(display_query())