import json
from flask import Flask, request, jsonify
from r import get_prediction

app = Flask(__name__)

@app.route("/get_image", methods=["POST"])
def get_image():
    img = request.files.get("letter_img")
    pred = get_prediction(img)
    return jsonify({"prediction": pred})

if (__name__ == "__main__"):
    app.run(debug=True)