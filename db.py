import sqlite3

# Create a connection to the SQLite database
conn = sqlite3.connect('orders.db')
cursor = conn.cursor()

# Drop the orders table if it exists
cursor.execute('DROP TABLE IF EXISTS orders')

# Create the orders table with the correct schema
cursor.execute('''
    CREATE TABLE orders (
        id INTEGER PRIMARY KEY,
        user_id TEXT,
        picked_pkg INTEGER,
        left_pkg INTEGER,
        total_pkg INTEGER,
        date TEXT,
        time TEXT,
        machine TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
