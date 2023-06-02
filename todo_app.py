# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
# """
# Created on Mon May 29 13:55:01 2023

# @author: evan
# """
# import sqlite3

# #create a database or connect to one
# conn = sqlite3.connect('tasks.db')

# #create a cursor
# c = conn.cursor()

# #create a table named tasks if it doesn't exist already
# c.execute("""CREATE TABLE IF NOT EXISTS tasks (
#             task text
#             )""")

# #commit the changes and close the connection
# conn.commit()
# conn.close()

# import tkinter as tk 
# from tkinter import messagebox

# def add_task():
#     task = task_entry.get()
#     if task != "":
#         #connect to db
#         conn = sqlite3.connect('tasks.db')
#         c = conn.cursor()
        
#         #add the task to the db
#         c.execute("INSERT INTO tasks VALUES (:task)", {'task': task})
        
#         conn.commit()
#         conn.close()
        
#         listbox_tasks.instert(tk.END, task)
#         task_entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning(title="Warning!", message="You must enter a task!")
        
# def delete_task():
#     try:
#         #get the selected task
#         selected_task = listbox_tasks.curselection()[0]
#         #delete the selected task
#         #listbox_tasks.delete(selected_task)
        
#         task = listbox_tasks.get(selected_task)
        
#         #connect to db
#         conn = sqlite3.connect('tasks.db')
#         c = conn.cursor()
        
#         c.execute("DELETE FROM tasks WHERE task=:task", {'task': task})
        
#         conn.commit()
#         conn.close()
        
#         listbox_tasks.delete(selected_task)
#     except:
#         messagebox.showinfo(title="Warning!", message="You must select a task.")

# def main():
#     #create the main window
#     root = tk.Tk()
#     root.title("My To-Do List App")
    
#     #Create an Entry widget
#     task_entry = tk.Entry(root, width=50)
#     task_entry.pack()
    
#     #create an add button
#     add_button = tk.Button(root, text="Add task", width=48, command=add_task)
#     add_button.pack()

#     #create a listbox widget
#     listbox_tasks = tk.Listbox(root, width=50)
#     listbox_tasks.pack()
    
#     #create a scrollbar for the listbox
#     scrollbar_tasks = tk.Scrollbar(listbox_tasks)
#     scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)
    
#     #configure the listbox to use the scrollbar
#     listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
#     scrollbar_tasks.config(command=listbox_tasks.yview)
    
#     #create a delete button
#     delete_button = tk.Button(root, text="Delete task", width=48, command=delete_task)
#     delete_button.pack()
    
#     #connect to the db
#     conn = sqlite3.connect('tasks.db')
#     c = conn.cursor()
    
#     #get all tasks from the db
#     c.execute("SELECT * FROM tasks")
#     tasks = c.fetchall()
    
#     conn.close()

#     #add all tasks to the listbox
#     for task in tasks:
#         listbox_tasks.instert(tk.END, task[0])
        
#     #run the event loop (kepp window open)
#     root.mainloop()
    
# if __name__ == "__main__":
#     main()


#Version 2
import sqlite3
import tkinter as tk 
from tkinter import messagebox

#Create a database or connect to one
conn = sqlite3.connect('tasks.db')

#Create a cursor
c = conn.cursor()

#Create a table named tasks if it doesn't exist already
c.execute("""CREATE TABLE IF NOT EXISTS tasks (
            task text
            )""")

#Commit the changes and close the connection
conn.commit()
conn.close()

#These will be defined in main() but we declare them here so that they can be accessed globally
task_entry = None
listbox_tasks = None

# def add_task():
#     task = task_entry.get()
#     if task != "":
#         #Connect to the database
#         conn = sqlite3.connect('tasks.db')
#         c = conn.cursor()

#         #Add the task to the database
#         c.execute("INSERT INTO tasks VALUES (:task)", {'task': task})

#         #Commit the changes and close the connection
#         conn.commit()
#         conn.close()

#         #Add the task to the Listbox and clear the Entry
#         listbox_tasks.insert(tk.END, task)
#         task_entry.delete(0, tk.END)
#     else:
#         messagebox.showwarning(title="Warning!", message="You must enter a task!")

#v2
def add_task():
    task = task_entry.get()
    if task != "":
        print(f"Retrieved task from Entry: {task}")  # Debug line

        # Connect to the database
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()

        # Add the task to the database
        c.execute("INSERT INTO tasks VALUES (:task)", {'task': task})

        # Commit the changes and close the connection
        conn.commit()
        conn.close()

        # Add the task to the Listbox and clear the Entry
        listbox_tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)

        print(f"Current tasks in Listbox: {listbox_tasks.get(0, tk.END)}")  # Debug line
    else:
        messagebox.showwarning(title="Warning!", message="You must enter a task!")


def delete_task():
    try:
        #Get the selected task
        selected_task = listbox_tasks.curselection()[0]
        task = listbox_tasks.get(selected_task)

        #Connect to the database
        conn = sqlite3.connect('tasks.db')
        c = conn.cursor()

        #Delete the task from the database
        c.execute("DELETE FROM tasks WHERE task=:task", {'task': task})

        #Commit the changes and close the connection
        conn.commit()
        conn.close()

        #Delete the selected task from the Listbox
        listbox_tasks.delete(selected_task)
    except:
        messagebox.showinfo(title="Warning!", message="You must select a task.")

# def main():
#     global task_entry, listbox_tasks

#     #Create the main window
#     root = tk.Tk()
#     root.title("My To-Do List App")

#     #Create an Entry widget
#     task_entry = tk.Entry(root, width=50)
#     task_entry.pack()

#     #Create an 'Add' button
#     add_button = tk.Button(root, text="Add task", width=48, command=add_task)
#     add_button.pack()

#     #Create a Listbox widget
#     listbox_tasks = tk.Listbox(root, width=50)
#     listbox_tasks.pack()

#     #Create a Scrollbar for the Listbox
#     scrollbar_tasks = tk.Scrollbar(listbox_tasks)
#     scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

#     #Configure the Listbox to use the Scrollbar
#     listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
#     scrollbar_tasks.config(command=listbox_tasks.yview)

#     #Create a 'Delete' button
#     delete_button = tk.Button(root, text="Delete task", width=48, command=delete_task)
#     delete_button.pack()

#     #Connect to the database
#     conn = sqlite3.connect('tasks.db')
#     c = conn.cursor()

#     #Get all tasks from the database
#     c.execute("SELECT * FROM tasks")
#     tasks = c.fetchall()

#     #Close the connection
#     conn.close()

#     #Add all tasks to the Listbox
#     for task in tasks:
#         listbox_tasks.insert(tk.END, task[0])

#     #Run the event loop (keep the window open)
#     root.mainloop()

#v2
def main():
    global task_entry, listbox_tasks

    # Create the main window
    root = tk.Tk()
    root.title("My To-Do List App")

    # Create an Entry widget
    task_entry = tk.Entry(root, width=50)
    task_entry.pack()

    # Create an 'Add' button
    add_button = tk.Button(root, text="Add task", width=48, command=add_task)
    add_button.pack()

    # Create a Listbox widget
    listbox_tasks = tk.Listbox(root, width=50)
    listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

    # Create a Scrollbar for the Listbox
    scrollbar_tasks = tk.Scrollbar(root)
    scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

    # Configure the Listbox to use the Scrollbar
    listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
    scrollbar_tasks.config(command=listbox_tasks.yview)

    # Create a 'Delete' button
    delete_button = tk.Button(root, text="Delete task", width=48, command=delete_task)
    delete_button.pack()

    # Connect to the database
    conn = sqlite3.connect('tasks.db')
    c = conn.cursor()

    # Get all tasks from the database
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()

    # Close the connection
    conn.close()

    # Add all tasks to the Listbox
    for task in tasks:
        listbox_tasks.insert(tk.END, task[0])

    # Run the event loop (keep the window open)
    root.mainloop()



if __name__ == "__main__":
    main()


