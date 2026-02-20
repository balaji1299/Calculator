from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calculate', methods=['POST'])
def divide():
    data = request.get_json()
    
    if data['b'] == 0:
        return jsonify({"error": "Division by zero"}), 400

    return jsonify({"result": data['a'] / data['b']})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5004)
