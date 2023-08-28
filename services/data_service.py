from flask import jsonify
from logging import getLogger
from models._init_ import cursor, conn

logger = getLogger("main")


def prepare_get_data():
    """
    This method get data from data db
    """
    logger.info("Data preparation started")

    cursor.execute("SELECT * FROM data ORDER BY id DESC LIMIT 1")
    latest_data = cursor.fetchone()
    logger.debug(f"Latest Data: {latest_data}")

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


def prepare_send_data(data):
    """
    This method populate the data into the db
    """
    if data:
        temperature = data.get("temperature")
        latitude = data.get("latitude")
        longitude = data.get("longitude")
        cursor.execute('''
            INSERT INTO data (temperature, latitude, longitude)
            VALUES (?, ?, ?)
        ''', (temperature, latitude, longitude))
        conn.commit()
        return jsonify({"message": "Data saved successfully"})
    else:
        return jsonify({"error": "No data provided"}), 400
