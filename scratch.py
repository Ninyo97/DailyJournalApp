import sqlite3

# Function to query and print all entries from the database
def view_entries():
    conn = sqlite3.connect("journal.db")
    cursor = conn.cursor()

    # Execute a simple SELECT query to retrieve all entries
    cursor.execute("SELECT * FROM entries")
    
    # Fetch all rows and print the results
    entries = cursor.fetchall()
    for entry in entries:
        print(entry)

    conn.close()

# Call the function to view entries
view_entries()
