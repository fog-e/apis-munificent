from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

# Load FAQ data from JSON file
with open("faq_entries.json", "r") as f:
    faq_data = json.load(f)["faq"]

@app.route("/faq", methods=["POST"])
def answer_faq():
    query = request.json.get("query", "").lower()
    for entry in faq_data:
        if query in entry["question"].lower():
            return jsonify({"answer": entry["answer"]})
    return jsonify({"answer": None})

@app.route("/", methods=["GET"])
def index():
    return "Hive-Mind FAQ API is running 🐝"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
