import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import filedialog
import pickle
import os
import sys

WIDTH = 1000
HEIGHT = 1000

root = tk.Tk()
root.geometry('400x400')
root.start = 0
# Functions
def delete():
    to_do_list.delete(tk.ANCHOR)

def add():
    to_do_list.insert(tk.END, adding.get())
    adding.delete(0,tk.END)

# Menu functions
def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir='C:\LoginTasks\Tasks Data',
        title='Save File',
        filetypes=(('Dat Files', '*.dat'), 
        ('All Files', '*.*'))
        )
    if file_name:
        if file_name.endswith('.dat'):
            pass
        else:
            file_name = f'{file_name}.dat'
        count = 0
        while count < to_do_list.size():
            if to_do_list.itemcget(count, 'fg') == '#dedede':
                to_do_list.delete(to_do_list.index(count))
            else:
                count += 1
    stuff = to_do_list.get(0, tk.END)

    output_file = open(file_name, 'wb')

    pickle.dump(stuff, output_file)


def open_list():
    file_name = filedialog.askopenfilename(
        initialdir='C:\LoginTasks\Tasks Data',
        title='Save File',
        filetypes=(('Dat Files', '*.dat'), 
        ('All Files', '*.*'))
    )

    if file_name:
        to_do_list.delete(0, tk.END)
        # Open dat file
        input_file = open(file_name, 'rb')
        # Load Dat file
        stuff = pickle.load(input_file)
        # Output Dat file
        for item in stuff:
            to_do_list.insert(tk.END, item)
def clear_list():
    to_do_list.delete(0, tk.END)

def logout():
    os.system('python design.py')
    sys.exit()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
frame = tk.Canvas(root, bg='#3B413C', bd=10)
frame.place(relwidth=1, relheight=1)
title = tk.Label(root, bg='#9DB5B2', bd=0, text='Notes', font=('Verdana', 12))
title.place(relx=.15, rely=.05, relwidth=.7, relheight=.07)

# Listbox
to_do_list = tk.Listbox(root, bg='#9DB5B2', bd=0, highlightthickness=0, selectbackground='#a6a6a6', activestyle='none', font=('Verdana', 10))
to_do_list.place(relx=.05, rely=.155, relwidth=.9, relheight=.5)


# Create a list and add list to list box 
items = []
for i in items:
    to_do_list.insert(tk.END, i)

# Making the scrollbar
scrollbar = tk.Scrollbar(to_do_list)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)
to_do_list.config(yscrollcommand=scrollbar)
scrollbar.config(command=to_do_list.yview)

# Lower half
adding = tk.Entry(root, font=('Verdana', 8), bg='#9DB5B2', bd=0)
adding.place(relx=.15, rely=.7, relwidth=.7, relheight=.07)

def counter():
    number.set(number.get()+1)
    to_do_list.itemconfig(
        to_do_list.curselection(),
        fg='#dedede',)
    to_do_list.selection_clear(0, tk.END)

number = tk.IntVar()

# Increment Box
increment = tk.Label(root, bg='#9db5b2', bd=0, textvariable=number, font=('Verdana', 8))
increment.place(relx=.9, rely=.06, relwidth=.05, relheight=.05)

# Action Buttons
delete_btn = tk.Button(root, bg='#9db5b2', text='Delete', bd=0, command=delete)
delete_btn.place(relx=.045, rely=.835, relwidth=.15, relheight=.08)
complete_btn = tk.Button(root, bg='#9db5b2', text='Completed', bd=0, command=counter)
complete_btn.place(relx=.225, rely=.835, relwidth=.18, relheight=.08)
add_btn = tk.Button(root, bg='#9db5b2', text='Add', bd=0, command=add)
add_btn.place(relx=.435, rely=.835, relwidth=.15, relheight=.08)
logout_btn = tk.Button(root, bg='#9db5b2', text='Logout', bd=0, command=logout)
logout_btn.place(relx=.615, rely=.835, relwidth=.15, relheight=.08)
open_btn = tk.Button(root, bg='#9db5b2', text='Open File', bd=0, command=open_list)
open_btn.place(relx=.795, rely=.835, relwidth=.15, relheight=.08)


# Create Menu
my_menu = tk.Menu(root)
root.config(menu=my_menu)

file_menu = tk.Menu(my_menu, tearoff=False)
my_menu.add_cascade(label='File', menu=file_menu)
# Add Drop down items
file_menu.add_command(label='Save List', command=save_list)
file_menu.add_separator()
file_menu.add_command(label='Clear List', command=clear_list)

root.mainloop()