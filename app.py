from flask import Flask, render_template
from routes.qr_route import qr_routes
from routes.order_route import order_routes
from routes.data_route import data_routes  # Corrected import statement
import schedule
import time

app = Flask(__name__)
app.register_blueprint(qr_routes)
app.register_blueprint(order_routes)
app.register_blueprint(data_routes)

@app.route("/", methods=["GET"])
def index():
    return render_template("qr.html")

if __name__ == "__main__":
    app.run("0.0.0.0", port=50001)
