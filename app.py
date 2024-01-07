import os
import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext, simpledialog
from datetime import datetime

# Function to create the SQLite database table
def create_table():
    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS entries (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date_created TEXT,
            title TEXT,
            content TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Function to add a new entry to the database
def add_entry(title, content):
    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()
    date_created = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO entries (date_created, title, content) VALUES (?, ?, ?)",
                   (date_created, title, content))
    conn.commit()
    conn.close()

# Function to handle the "Add New" button click
def add_new_entry():
    title = simpledialog.askstring("Title", "Enter the title of the entry:")
    if title:
        content = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
        content.pack(padx=10, pady=10)
        content.insert(tk.INSERT, "Start typing your journal entry here...")
        
        def save_entry():
            entry_content = content.get("1.0", tk.END)
            add_entry(title, entry_content)
            content.destroy()
            messagebox.showinfo("Success", "Entry saved successfully!")

        save_button = tk.Button(root, text="Save Entry", command=save_entry)
        save_button.pack(pady=10)

# Function to initialize the application
def initialize_app():
    create_table()

# Main application code
root = tk.Tk()
root.title("Daily Journal")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "File" menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add "Add New" option to the "File" menu
file_menu.add_command(label="Add New", command=add_new_entry)

# Initialize the application
initialize_app()

# Run the application
root.mainloop()
