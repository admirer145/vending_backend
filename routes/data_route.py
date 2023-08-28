from flask import Blueprint, request
from services.data_service import prepare_get_data, prepare_send_data
from models._init_ import cleanup

data_routes = Blueprint("data_routes", __name__)


# New route to fetch updated data from the database
@data_routes.route("/get_data", methods=["GET"])
def get_data():
    try:
        resp = prepare_get_data()
    except Exception as err:
        raise Exception(f"Error occurred while getting the data: {err}")
    finally:
        cleanup()
    return resp


@data_routes.route("/send_data", methods=["POST"])
def send_data():
    data = request.json
    try:
        resp = prepare_send_data(data)
    except Exception as err:
        raise Exception(f"Error occurred while sending the data: {err}")
    finally:
        cleanup()
    return resp
