from flask import Flask, jsonify, render_template
import time

app = Flask(__name__)

cart = 0

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add():
    global cart
    cart += 1

    time.sleep(0.2)

    return jsonify({
        "message": "Product added",
        "cart_count": cart
    })


@app.route("/health")
def health():
    return "OK"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)