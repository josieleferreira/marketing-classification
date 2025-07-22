# app.py
import pickle
import statsmodels.api as sm
from flask_cors import CORS
from flask import Flask, request

app = Flask(__name__)  
CORS(app)

@app.route("/inference", methods=["POST"])
def predict():
    data = request.get_json()
    return {
        "message": "Data Received",
        "data": data
    }, 200

if __name__ == "__main__":  
    app.run(host="0.0.0.0", port=5000)
