# import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

first_name = ttk.Label(root, text="First Name:", font=("Calibri", 12))
first_name.grid(column = 0, row=0, padx=5)

first_name_entry = ttk.Entry(root, font=("Calibri", 12), width=20)
first_name_entry.grid(column=1, row=0, padx=5, pady=5,columnspan=2)

last_name = ttk.Label(root, text="Last Name:", font=("Calibri", 12))
last_name.grid(column = 0, row=1, padx=5)

last_name_entry = ttk.Entry(root, font=("Calibri", 12), width=20)
last_name_entry.grid(column=1, row=1, padx=5, pady=5,columnspan=2)

gender = ttk.Label(root, font=("Calibri", 12), text="Gender")
gender.grid(column=0, row=3, sticky="W")

genderVar = ttk.StringVar()


gender_male = ttk.Radiobutton(root, text='male', value="male", variable=genderVar, bootstyle="success")
gender_male.grid(column=1, row=3,columnspan=2, sticky="W")

gender_female = ttk.Radiobutton(root, text='female', value="female", variable=genderVar, bootstyle="success")
gender_female.grid(column=2, row=3, columnspan=2, sticky="W")

departure_label = ttk.Label(root, text='Departure', font=("Calibri", 12))
departure_label.grid(column=0, row=4)

departure_var = ttk.StringVar()
departure_chosen = ttk.Combobox(root, width=12, textvariable=departure_var, bootstyle="dark", state="readonly")
departure_chosen['values'] = ("Lagos", "PortHarcourt", "Abuja")
departure_chosen.grid(column=1, row=4)

arrival_label = ttk.Label(root, text='Arrival', font=("Calibri", 12))
arrival_label.grid(column=0, row=5)

arrival_var = ttk.StringVar()
arrival_chosen = ttk.Combobox(root, width=12, textvariable=arrival_var, bootstyle="dark", state="readonly")
arrival_chosen['values'] = ("Lagos", "PortHarcourt", "Abuja")
arrival_chosen.grid(column=1, row=5)


root.mainloop()