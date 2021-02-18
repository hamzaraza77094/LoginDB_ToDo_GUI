import tkinter as tk
import matplotlib.pyplot as plt 
import numpy as np 
import sqlite3
import os
import sys
# Craete a database
conn = sqlite3.connect('login_info.db')
# Create cursor
c = conn.cursor()
# # Create table
# c.execute('''CREATE TABLE login (
#     username text,
#     password text
# )''')
HEIGHT = 1000
WIDTH = 1000
root = tk.Tk()
root.geometry('350x300')
def admin():
    if user.get() == 'hamzaraza77094' and password.get() == 'Raza77094':
        conn = sqlite3.connect('login_info.db')
        c = conn.cursor()
        c.execute('SELECT *, oid FROM login')
        records = c.fetchall() # This will get all of the records
        print(records)
        print_record = ''
        for record in records:
            print_record += str(record) + '\n'
        root2 = tk.Tk()
        root2.geometry('400x300')
        canvas2 = tk.Canvas(root2, height=HEIGHT, width=WIDTH)
        frame2 = tk.Frame(root2, bg='#3B413C', bd=10)
        frame2.place(relwidth=1, relheight=1)
        title2 = tk.Label(root2, bg='#DAF0EE', text='Admin Records')
        title2.place(relx=.28, rely=.1, relwidth=.5, relheight=.1)
        show_record = tk.Label(root2, bg='#DAF0EE', text=print_record, font=('arial', 8))
        show_record.place(relx=.1, rely=.25, relwidth=.8, relheight=.7)
        conn.commit()
        conn.close()
def registers():
    # connect to database
    conn = sqlite3.connect('login_info.db')
    # Make a cursor
    c = conn.cursor()
    # Insert into table
    c.execute('INSERT INTO login VALUES (:user, :password)', # Right here I stated the variables Im going to use and then below is the dictionary and I insert them into the table I want
        {
            'user': user.get(),
            'password': password.get()
        })
    # Commit and close
    conn.commit()
    conn.close()
    # Delet the entry fields
    user.delete(0,tk.END)
    password.delete(0,tk.END)
def submit_():
    conn = sqlite3.connect('login_info.db')
    c = conn.cursor()
    username1 = user.get()
    password1 = password.get()
    c.execute("select username, password from login where username = ? and password = ?", (username1, password1))
    if c.fetchone():
        logged_in = tk.Label(root, bg='#C1FBA4', text='Successful Login!')
        logged_in.place(relx=.1, rely=.85, relwidth=.8, relheight=.1)
        os.system('python todo.py')
    else:
        logged_in = tk.Label(root, bg='#FB6376', text='Unsuccessful Login.')
        logged_in.place(relx=.1, rely=.85, relwidth=.8, relheight=.1)
    conn.commit()
    conn.close()
    admin()
# Design of app
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
frame = tk.Frame(root, bg='#3B413C', bd=10)
frame.place(relwidth=1, relheight=1)
title = tk.Label(root, bg='#DAF0EE', text='Login')
title.place(relx=.28, rely=.08, relwidth=.5, relheight=.1)
user = tk.Entry(frame, bg='#9DB5B2', font=('Verdana', 8))
user.place(relwidth=.5, relheight=.07, relx=.37, rely=.25)
user_label = tk.Label(frame, bg='#9DB5B2', text='Username', font=('arial', 10))
user_label.place(relx=.14, rely=.25, relwidth=.19, relheight=.07)
password = tk.Entry(frame, bg='#9DB5B2', font=('Verdana', 8))
password.place(relwidth=.5, relheight=.07, relx=.37, rely=.4)
password_label = tk.Label(frame, bg='#9DB5B2', text='Pasword', font=('arial', 10))
password_label.place(relx=.14, rely=.4, relwidth=.19, relheight=.07)
register = tk.Button(frame, bg='#DAF0EE', text='Register', command=registers, bd=0)
register.place(relx=.24, rely=.55, relwidth=.23, relheight=.1)
submit = tk.Button(frame, bg='#DAF0EE', text='Submit', command=submit_, bd=0)
submit.place(relx=.54, rely=.55, relwidth=.23, relheight=.1)
conn.commit()
conn.close()
root.mainloop()