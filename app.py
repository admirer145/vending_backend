from flask import Flask, render_template, request, jsonify  # Add render_template
import requests
import base64
import urllib.parse

qrapp = Flask(__name__)

# Simulated database (dictionary)
orders_database = {}

@qrapp.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json  # Get the JSON payload from the request

    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    amount = data.get("amount")
    if amount is None:
        return jsonify({"error": "Amount field is missing in JSON data"}), 400

    # Create the QR code data string using the provided UPI QR data
    qr_code_data = f"upi://pay?ver=01&pa=9769819152@ybl&pn=V2BDMON1&mc=5413&tid=&tr=ViswaTest123&tn=PayToViswaNotes&am={amount}&mam={amount}&cu=INR&refUrl=https://billdesk.com&qrMedium=04&mode=15"

    # Properly encode the QR code data for the URL
    encoded_qr_code_data = urllib.parse.quote(qr_code_data)

    # URL to generate QR code using the modified data string
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_qr_code_data}&format=jpg"

    # Fetch the QR code image
    response = requests.get(qr_code_url)

    if response.status_code == 200:
        qr_code_content = response.content

        # Convert the image content to base64
        qr_code_base64 = base64.b64encode(qr_code_content).decode('utf-8')

        return jsonify({"qr_code": qr_code_base64})
    else:
        return jsonify({"error": "Failed to generate the QR code image."}), 500

@qrapp.route("/save_order", methods=["POST"])

def save_order():
    order_data = request.json  # Get the JSON payload from the request

    if order_data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    user_id = order_data.get("user_id")
    if user_id is None:
        return jsonify({"error": "user_id field is missing in JSON data"}), 400

    # Save the order details in the simulated database
    orders_database[user_id] = order_data

    return jsonify({"message": "Order details saved successfully"})

# @qrapp.route("/", methods=["GET"])
# def index():
#     return render_template("qr.html")

@qrapp.route("/get_order/<string:user_id>", methods=["GET"])
def get_order(user_id):
    order_data = orders_database.get(user_id)

    if order_data is None:
        return jsonify({"error": "Order not found"}), 404

    return jsonify(order_data)

if __name__ == "__main__":
    qrapp.run(debug=True,port=50001)
