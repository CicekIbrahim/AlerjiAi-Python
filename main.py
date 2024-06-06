from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import time
import os
import json
import torch
from ultralytics import YOLO
from PIL import Image
from llm import get_llm_response, encode_image  
from model import detect_with_yolov9

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})  

def start_ngrok():
    ngrok_process = subprocess.Popen(['ngrok', 'http', '5000'])
    time.sleep(5)
    result = subprocess.run(['curl', '-s', 'http://localhost:4040/api/tunnels'], capture_output=True, text=True)
    result_json = json.loads(result.stdout)
    public_url = result_json['tunnels'][0]['public_url']
    print(f" * ngrok tunnel: {public_url}")

@app.route('/detect', methods=['POST'])
def detect():
    file = request.files['image']
    image_path = "received_image.jpg"
    file.save(image_path)

    detections = detect_with_yolov9(image_path)
    if detections:
        return jsonify({"response": detections[0]})
    else:
        base64_image = encode_image(image_path)
        llm_response = get_llm_response(base64_image)
        return jsonify({"response": llm_response['choices'][0]['message']['content']})

if __name__ == '__main__':
    start_ngrok()
    app.run()
