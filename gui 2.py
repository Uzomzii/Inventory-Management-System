import tkinter as tk
from gui_db import create_table, insert_input

root = tk.Tk()

create_table()

root.geometry('400x300')

first_name_label = tk.Label(root, text='First Name:', font=('Times New Roman', 14), fg='Blue')
first_name_label.grid(row=0, column=0)

last_name_label = tk.Label(root, text='Last Name:', font=('Times New Roman', 14))
last_name_label.grid(row=1, column=0)

phone_label = tk.Label(root, text='Phone No.', font=('Times New Roman', 14))
phone_label.grid(row=2, column=0)

def click_me():
    first_name = first_name_entry.get() # We use .get() to retrieve data from the entry widget
    last_name = last_name_entry.get()
    phone = phone_entry.get()
    insert_input(first_name, last_name, phone)
    
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)



first_name_entry = tk.Entry(root, font=('Times New Roman', 14))
first_name_entry.grid(row=0, column=1)

last_name_entry = tk.Entry(root, font=('Times New Roman', 14))
last_name_entry.grid(row=1, column=1)

phone_entry = tk.Entry(root, font=('Times New Roman', 14))
phone_entry.grid(row=2, column=1)

button = tk.Button(root, text='Submit', width=15, height=1, font=('Times New Roman', 12), command=click_me)
button.grid(row=3, column=1)


root.mainloop()