from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Sedan XYZ",     "make": "Toyota",     "model": "Corolla", "year": 2023},
    {"id": 2, "name": "SUV ABC",        "make": "Honda",      "model": "CR-V",    "year": 2023},
    {"id": 3, "name": "Truck LMN",      "make": "Ford",       "model": "F-150",   "year": 2022},
    {"id": 4, "name": "Hatchback PQR",  "make": "Volkswagen", "model": "Golf",    "year": 2023},
    {"id": 5, "name": "Electric EV1",   "make": "Tesla",      "model": "Model 3", "year": 2024},
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Product Details Microservice is running!"})

@app.route("/products", methods=["GET"])
def get_products():
    return jsonify(products)

@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=False)
