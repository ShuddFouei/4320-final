import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import sqlite3
with sqlite3.connect('fridge.db') as db:
    cursor=db.cursor()


    
cursor.execute(""" CREATE TABLE IF NOT EXISTS foods(food text NOT NULL, exp date NOT NULL); """)



def submit():
    newFood = food_var.get()
    newExp = exp_var.get()

    cursor.execute("INSERT INTO foods (food, exp) VALUES(?, ?)", (newFood, newExp))
    db.commit()

def View():
    con1 = sqlite3.connect('fridge.db')
    cur1 = con1.cursor()
    cur1.execute("SELECT * FROM foods")
    rows = cur1.fetchall()    
    for row in rows:
        print(row) 
        tree.insert("", tk.END, values=row)        
    con1.close()

main = tk.Tk()
tree = ttk.Treeview(main, column=("c1", "c2",), show='headings')
tree.column("#1", anchor=tk.CENTER)
tree.heading("#1", text="Food")
tree.column("#2", anchor=tk.CENTER)
tree.heading("#2", text="Expiration")

main.title("Fridge App")
food_var = tk.StringVar()
exp_var = tk.IntVar()
label = tk.Label(main, text="Enter and Track whats in the Fridge", font=("Arial", 12), padx=100, pady=20) 

food_label = tk.Label(main, text = 'Enter Food', font=('Arial',10,'bold'))
food_entry = tk.Entry(main,textvariable = food_var, font=('Arial',10))

exp_label = tk.Label(main, text = 'Enter Expiration Date', font=('Arial',10,'bold'))
exp_entry = tk.Entry(main,textvariable = exp_var, font=('Arial',10))

button1 = tk.Button(main, text="Add", 
                   command = submit, padx=50, pady=20, bg="gray")
button2 = tk.Button(main, text="View", 
                   command = View, padx=48, pady=20, bg="gray")


label.pack()
food_label.pack()
food_entry.pack()
exp_label.pack()
exp_entry.pack()
button1.pack()
button2.pack()
tree.pack()
main.mainloop()