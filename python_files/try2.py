import json
import requests
import os

API_TOKEN = os.getenv('TTS_API_KEY')

headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response

output = query({"text_inputs": "Max is the best doggo."})
print(output)