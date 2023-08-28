
import sqlite3
from logging import getLogger
logger = getLogger("main")

logger.debug("Creating the connections")

# Create a connection to the SQLite database
conn = sqlite3.connect('data.db', check_same_thread=False)
cursor = conn.cursor()


def create_tables():
    # Create the data table with the correct schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS data (
            id INTEGER PRIMARY KEY,
            temperature REAL,
            latitude REAL,
            longitude REAL
        )
    ''')
    # Create the orders table with the correct schema
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS orders (
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
    # Commit the changes 
    conn.commit()


# close the connections
def cleanup():
    # cursor.close()
    # conn.close()
    pass


create_tables()
