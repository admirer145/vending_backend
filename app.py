from flask import Flask, render_template
from routes.qr_route import qr_routes
from routes.order_route import order_routes

app = Flask(__name__)
app.register_blueprint(qr_routes)
app.register_blueprint(order_routes)

@app.route("/", methods=["GET"])
def index():
    return render_template("qr.html")

if __name__ == "__main__":
    app.run(debug=True, port=50001)
