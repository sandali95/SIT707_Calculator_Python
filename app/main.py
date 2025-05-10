from flask import Flask, jsonify, request
from .calculator import add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_numbers():
    data = request.get_json()
    result = add(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/subtract', methods=['POST'])
def subtract_numbers():
    data = request.get_json()
    result = subtract(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/multiply', methods=['POST'])
def multiply_numbers():
    data = request.get_json()
    result = multiply(data['a'], data['b'])
    return jsonify({"result": result})

@app.route('/divide', methods=['POST'])
def divide_numbers():
    data = request.get_json()
    try:
        result = divide(data['a'], data['b'])
        return jsonify({"result": result})
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)