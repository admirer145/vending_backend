from flask import Blueprint, request, jsonify
import requests
import base64
import urllib.parse

qr_routes = Blueprint("qr_routes", __name__)


def get_serial_number():
    # Replace this with the logic to fetch and increment the serial number from a file or database
    # For now, we will simulate incrementing the serial number by 1 in each call
    with open("serial_number.txt", "r+") as file:
        serial_number = int(file.read() or "0")
        serial_number += 1
        file.seek(0)
        file.write(str(serial_number))
        file.truncate()
    return str(serial_number).zfill(3)  # Padded with zeros to ensure three digits

@qr_routes.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json

    if data is None:
        return jsonify({"error": "No JSON data provided"}), 400

    quantity = data.get("quantity")  # Get the quantity from the user input
    if quantity is None:
        return jsonify({"error": "Quantity field is missing in JSON data"}), 400

    amount = quantity * 10  # Calculate the amount based on the quantity

    terminal_id = "1111"  # Replace with your constant terminal ID
    product_id = "0001"    # Replace with your constant product ID

    # Constructing the order ID based on the provided information
    serial_number = get_serial_number()
    order_id = f"{terminal_id}{serial_number}"

    tn = f"{product_id}{quantity}"  # Construct the product code and quantity for tn

    # Create the modified QR code data string using the provided information
    qr_code_data = f"upi://pay?ver=01&pa=9769819152@ybl&pn=BATRMAN&mc={terminal_id}&tid={terminal_id}&tr={order_id}&tn={tn}&am={amount}&mam={amount}&cu=INR&refUrl=https://BATRMAN.in&qrMedium=04&mode=15"

    # Properly encoding the QR code data for the URL
    encoded_qr_code_data = urllib.parse.quote(qr_code_data)

    # URL to generate QR code using the modified data string
    qr_code_url = f"https://api.qrserver.com/v1/create-qr-code/?size=150x150&data={encoded_qr_code_data}&format=jpg"

    # Fetching the QR code image
    response = requests.get(qr_code_url)

    if response.status_code == 200:
        qr_code_content = response.content

        # Converting the image content to base64
        qr_code_base64 = base64.b64encode(qr_code_content).decode('utf-8')

        return jsonify({"qr_code": qr_code_base64})
    else:
        return jsonify({"error": "Failed to generate the QR code image."}), 500

if __name__ == "__main__":
    from flask import Flask
    qrapp = Flask(__name__)
    qrapp.register_blueprint(qr_routes)
    qrapp.run(debug=True, port=50001)
