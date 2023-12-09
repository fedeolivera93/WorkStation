import sqlite3

conn = sqlite3.connect('base.db')
cursor = conn.cursor()

# Execute the command to check for tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

# Fetch the results
tables = cursor.fetchall()

# Check if the "usuarios" table exists
if "usuarios" in tables:
    print("Table 'usuarios' exists")
else:
    print("Table 'usuarios' does not exist")

conn.close()