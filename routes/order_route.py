from flask import Blueprint, request, jsonify
from models._init_ import cursor, cleanup
from services.order_service import clear_order_data, save_order_data, get_all_orders_data

order_routes = Blueprint("order_routes", __name__)


@order_routes.route("/clear_orders", methods=["POST"])
def clear_orders():
    try:
        resp = clear_order_data()
    except Exception as err:
        raise Exception(f"Error occurred while clearing the orders: {err}")
    finally:
        cleanup()
    return resp


@order_routes.route("/save_order", methods=["POST"])
def save_order():
    order_data = request.json
    try:
        resp = save_order_data(order_data)
    except Exception as err:
        raise Exception(f"Error occurred while saving the order: {err}")
    finally:
        cleanup()
    return resp


@order_routes.route("/get_all_orders", methods=["GET"])
def get_all_orders():
    try:
        resp = get_all_orders_data()
    except Exception as err:
        raise Exception(f"Error occurred while getting all the orders: {err}")
    finally:
        cleanup()
    return resp
