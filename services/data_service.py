from flask import jsonify
import sqlite3
from logging import getLogger

logger = getLogger("main")


def prepare_data():
    """
    This method prepares data from data db
    """
    logger.info("Start preparing the data")
    conn = sqlite3.connect('data.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
    latest_data = cursor.fetchone()

    conn.close()

    if latest_data:
        data = {
            "temperature": latest_data[1],
            "latitude": latest_data[2],
            "longitude": latest_data[3]
        }
    else:
        data = {
            "message": "No data available"
        }
    logger.info(f"Data preparation completed: {data}")
    return jsonify(data)
