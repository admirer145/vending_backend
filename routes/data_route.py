from flask import Blueprint, request, jsonify
import sqlite3

data_routes = Blueprint("data_routes", __name__)

# New route to fetch updated data from the database
@data_routes.route("/get_data", methods=["GET"])
def get_data():
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
        return jsonify(data)
    else:
        return jsonify({"message": "No data available"})

@data_routes.route("/send_data", methods=["POST"])
def send_data():
    data = request.json

    if data:
        temperature = data.get("temperature")
        latitude = data.get("latitude")
        longitude = data.get("longitude")

        conn = sqlite3.connect('data.db')
        cursor = conn.cursor()

        cursor.execute('''
            INSERT INTO data (temperature, latitude, longitude)
            VALUES (?, ?, ?)
        ''', (temperature, latitude, longitude))

        conn.commit()
        conn.close()

        return jsonify({"message": "Data saved successfully"})
    else:
        return jsonify({"error": "No data provided"}), 400
# if __name__ == "__main__":
#     app.run("0.0.0.0", port=50001)
