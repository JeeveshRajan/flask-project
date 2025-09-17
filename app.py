from flask import Flask, jsonify
import random

app = Flask(__name__)

QUOTES = [
    "The best way to get started is to quit talking and begin doing.",
    "Success is not in what you have, but who you are.",
    "Opportunities don't happen, you create them.",
    "Don't let yesterday take up too much of today.",
    "It's not whether you get knocked down, it's whether you get up."
]

@app.route("/")
def home():
    return "I dont like quotes!"

@app.route("/quote")
def quote():
    return jsonify({"quote": random.choice(QUOTES)})

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000) 

# To run the application, use the command: python app.py 
# to check the k8 automation   
