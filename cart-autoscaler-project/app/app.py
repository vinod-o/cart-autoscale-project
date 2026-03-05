from flask import Flask, request, jsonify
import time

app = Flask(__name__)

cart_count = 0

@app.route('/add', methods=['POST'])
def add_product():
    global cart_count

    cart_count += 1

    # simulate heavy processing
    time.sleep(0.2)

    return jsonify({
        "message": "Product added",
        "cart_items": cart_count
    })


@app.route('/health')
def health():
    return "OK"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)