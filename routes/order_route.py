from flask import Blueprint, request, jsonify
import sqlite3

order_routes = Blueprint("order_routes", __name__)


@order_routes.route("/clear_orders", methods=["POST"])
def clear_orders():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Delete all records from the orders table
    cursor.execute("DELETE FROM orders")

    conn.commit()
    conn.close()

    return jsonify({"message": "All orders cleared successfully"})

@order_routes.route("/save_order", methods=["POST"])
# ...

@order_routes.route("/save_order", methods=["POST"])
def save_order():
    order_data = request.json

    if order_data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    user_id = order_data.get("user_id")
    if user_id is None:
        return jsonify({"error": "user_id field is missing in JSON data"}), 400

    # Extract individual fields from order_data
    picked_pkg = order_data.get("picked_pkg")
    left_pkg = order_data.get("left_pkg")
    total_pkg = order_data.get("total_pkg")
    date = order_data.get("date")
    time = order_data.get("time")
    machine = order_data.get("machine")
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    # Insert the order details into the database
    cursor.execute('''
        INSERT INTO orders (user_id, picked_pkg, left_pkg, total_pkg, date, time)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (user_id, picked_pkg, left_pkg, total_pkg, date, time, machine))

    conn.commit()
    conn.close()

    return jsonify({"message": "Order details saved successfully"})


@order_routes.route("/get_all_orders", methods=["GET"])
def get_all_orders():
    conn = sqlite3.connect('orders.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    conn.close()

    # Converting data to a list of dictionaries for JSON serialization
    orders_list = []
    for order in orders:
        order_dict = {
            "id": order[0],
            "user_id": order[1],
            "picked_pkg": order[2],   # Use the correct column index
            "left_pkg": order[3],     # Use the correct column index
            "total_pkg": order[4],    # Use the correct column index
            "date": order[5],
            "time": order[6],
            "machine": order[7]
        }
        orders_list.append(order_dict)

    return jsonify({"orders": orders_list})
