import tkinter as tk
from tkinter import ttk
import mysql.connector

def get_jabatan_data():
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='',
        database='informatika'
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute a query to retrieve data from the 'jabatan' table
    cursor.execute("SELECT id, nama_jabatan FROM jabatan")

    # Fetch all the data
    jabatan_data = cursor.fetchall()

    # Close the cursor and connection
    cursor.close()
    connection.close()

    return jabatan_data

def on_combobox_select(event):
    selected_index = combo.current()
    selected_id = jabatan_data[selected_index][0]
    selected_nama_jabatan = jabatan_data[selected_index][1]
    print(f"Selected Jabatan ID: {selected_id}, Nama Jabatan: {selected_nama_jabatan}")

# Create the main window
root = tk.Tk()
root.title("Jabatan ComboBox")

# Get data from MySQL table
jabatan_data = get_jabatan_data()

# Create a ComboBox
combo = ttk.Combobox(root, values=[nama_jabatan for _, nama_jabatan in jabatan_data])
combo.pack(pady=10)

# Bind the event handler to the ComboBox selection
combo.bind("<<ComboboxSelected>>", on_combobox_select)

# Run the Tkinter event loop
root.mainloop()
