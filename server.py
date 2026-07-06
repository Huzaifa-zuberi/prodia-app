from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from dotenv import load_dotenv
import requests
import base64
import time
import os

load_dotenv()

app = Flask(__name__, static_folder="public")
CORS(app)

HF_TOKEN = os.environ.get("HF_API_TOKEN", "")
HF_BASE = "https://api-inference.huggingface.co/models"


@app.route("/")
def index():
    return send_from_directory("public", "index.html")


@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    prompt = data.get("prompt")

    if not HF_TOKEN:
        return jsonify({"error": "HF_API_TOKEN not set on server"}), 500
    if not prompt:
        return jsonify({"error": "Prompt is required"}), 400

    model = data.get("model", "stabilityai/stable-diffusion-xl-base-1.0")
    headers = {"Authorization": f"Bearer {HF_TOKEN}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "negative_prompt": data.get("negative", ""),
            "num_inference_steps": data.get("steps", 25),
            "guidance_scale": data.get("cfg", 7.5),
        },
    }

    for _ in range(30):
        resp = requests.post(
            f"{HF_BASE}/{model}",
            json=payload,
            headers=headers,
        )

        if resp.status_code == 200:
            b64 = base64.b64encode(resp.content).decode("utf-8")
            return jsonify({"imageUrl": f"data:image/png;base64,{b64}"})

        if resp.status_code == 503:
            time.sleep(5)
            continue

        try:
            err = resp.json()
        except Exception:
            err = resp.text
        return jsonify({"error": err}), resp.status_code

    return jsonify({"error": "Model still loading, try again"}), 504


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 3000)), debug=True)
