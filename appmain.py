from flask import Flask, render_template
from routes.qr_route import qr_routes
from routes.order_route import order_routes
from routes.data_route import data_routes  # Corrected import statement
from settings import SERVER_HOST, SERVER_PORT

# Initialize the flask app
app = Flask(__name__)

# Register the routes
app.register_blueprint(qr_routes)
app.register_blueprint(order_routes)
app.register_blueprint(data_routes)


# Create the root endpoint
@app.route("/", methods=["GET"])
def index():
    return render_template("qr.html")


# Start the server
if __name__ == "__main__":
    app.run(SERVER_HOST, port=SERVER_PORT)
