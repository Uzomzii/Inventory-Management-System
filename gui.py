import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu

win = tk.Tk() # Create our application window

tabControl = ttk.Notebook(win)      # Create Tab Control
tab1 = ttk.Frame(tabControl)        # Create a tab
tabControl.add(tab1, text='Tab 1')  # Add the tab

tab2 = ttk.Frame(tabControl)
tabControl.add(tab2, text="Tab 2")

tabControl.grid(sticky=tk.W+tk.E)

mighty = tk.LabelFrame(tab1, text="Mighty Python")
mighty.grid(column=0, row=0, padx=10, pady=10)

# tk.Label(win, text="Welcome to my first GUI").grid(row=0, column=0)
tk.Label(mighty, text="Choose a number:").grid(column=0, row=0, columnspan=2, sticky="W")
number = tk.IntVar()
number_chosen = ttk.Combobox(mighty, width=12, textvariable=number)
number_chosen['values'] = (1,2,3,4,45, 100)
number_chosen.grid(column=0, row=1, columnspan=2, sticky="W")
number_chosen.current(0)

btn1 = tk.Button(mighty, text="With tk")
btn1.grid(column=0, row=2, sticky="W")

chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty, text='Disabled', variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=3, sticky="W")

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty, text='Unchecked', variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=3, sticky="W")

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty, text='Enabled', variable=chVarEn)
check3.select()
check3.grid(column=2, row=3, sticky="W")

def radCall():
    radSel = radVar.get()
    if radSel == 1: win.configure(background='Blue')
    elif radSel == 2: win.configure(background='Red')
    elif radSel == 3: win.configure(background='Yellow')
    


# create three Radiobuttons using one variable
radVar = tk.IntVar()

rad1 = tk.Radiobutton(mighty, text='Blue', variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=4, sticky="W")

rad2 = tk.Radiobutton(mighty, text='Red', variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=4, sticky="W")

rad3 = tk.Radiobutton(mighty, text='Yellow', variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=4, sticky="W")

scr =scrolledtext.ScrolledText(mighty, width=30, height=4, wrap=tk.WORD)
scr.grid(column=0, row=5, columnspan=3)

# Create a container to hold labels
frames = ttk.LabelFrame(mighty, text='Labels in a frame')
frames.grid(column=0, row=6, pady=5, padx=30, columnspan=3)

# Place labels into the container element
ttk.Label(frames, text='Label 1').grid(column=0, row=0)
ttk.Label(frames, text='Label 2').grid(column=0, row=1)
ttk.Label(frames, text='Label 3').grid(column=0, row=2)

def _quit():
    win.quit()
    win.destroy()
    exit()

# Creating a Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

# Create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)  # create File menu
menu_bar.add_cascade(label='File', menu=file_menu) # add file to menu bar and give it a label
file_menu.add_command(label="New File")
file_menu.add_command(label='Open File')
file_menu.add_separator()
file_menu.add_command(label="Exit", command=_quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label='Edit', menu=edit_menu)
edit_menu.add_command(label='Copy')

win.mainloop() # Keep on displaying your application