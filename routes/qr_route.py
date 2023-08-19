from flask import Blueprint, request, jsonify
import requests
import base64
import urllib.parse

qr_routes = Blueprint("qr_routes", __name__)

@qr_routes.route("/generate_qr", methods=["POST"])
def generate_qr():
    data = request.json

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

    pass

raspberry_pi_ip = "http://127.0.0.1:5000"

@qr_routes.route("/send_open_door_command", methods=["POST"])
def send_open_door_command():
    # Send the command to open the door to the Raspberry Pi (localhost) callback
    try:
        response = requests.get(f"{raspberry_pi_ip}/open_door_callback")
        if response.status_code == 200:
            return jsonify({"message": "Open door command sent successfully"})
        else:
            return jsonify({"error": "Failed to send open door command"}), 500
    except requests.ConnectionError:
        return jsonify({"error": "Could not connect to the Raspberry Pi"}), 500

# qr_routes.register_blueprint(qr_routes)

@qr_routes.route("/", methods=["GET"])
def index():
    return render_template("qr.html")

if __name__ == "__main__":
    qrapp.run(debug=True,port=50001)
