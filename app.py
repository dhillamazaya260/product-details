from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Midsize SUV", "category": "SUV"},
    {"id": 2, "name": "Compact Sedan", "category": "Sedan"},
    {"id": 3, "name": "Electric Hatchback", "category": "Electric"},
]

@app.route("/")
def health():
    return jsonify({"status": "ok"})

@app.route("/products")
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
