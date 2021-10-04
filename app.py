from flask import Flask, request, jsonify
from transformers import pipeline
import os

app = Flask(__name__)

model_path = "distilbert"

def classify(input):
  # Your function
  classify = pipeline("sentiment-analysis", model=model_path, tokenizer=model_path)
  return classify(input)

@app.route("/") # To make our site available at URL:port/
def api():
    return jsonify(classify(str(request.args['text'])))

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
