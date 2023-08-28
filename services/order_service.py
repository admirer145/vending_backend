from flask import jsonify
from models._init_ import cursor


def clear_order_data():
    # Delete all records from the orders table
    cursor.execute("DELETE FROM orders")
    return jsonify({"message": "All orders cleared successfully"})


def save_order_data(order_data):
    if order_data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    user_id = order_data.get("user_id")
    machine = order_data.get("machine")  # Extract the machine name from the JSON data

    picked_pkg = order_data.get("picked_pkg")
    left_pkg = order_data.get("left_pkg")
    total_pkg = order_data.get("total_pkg")
    date = order_data.get("date")
    time = order_data.get("time")

    cursor.execute('''
        INSERT INTO orders (user_id, picked_pkg, left_pkg, total_pkg, date, time, machine)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (user_id, picked_pkg, left_pkg, total_pkg, date, time, machine))

    return jsonify({"message": "Order details saved successfully"})


def get_all_orders_data():
    
    cursor.execute("SELECT * FROM orders")
    orders = cursor.fetchall()

    orders_list = []
    for order in orders:
        order_dict = {
            "id": order[0],
            "user_id": order[1],
            "picked_pkg": order[2],
            "left_pkg": order[3],
            "total_pkg": order[4],
            "date": order[5],
            "time": order[6],
            "machine": order[7]  # Adjust this index based on your schema order
        }
        orders_list.append(order_dict)
    return jsonify({"orders": orders_list})
