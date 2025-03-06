import requests, os

TTS_API_KEY = os.getenv('TTS_PEAK_KEY')
API_URL = "https://api-inference.huggingface.co/models/microsoft/speecht5_tts"
headers = {"Authorization": f"Bearer {TTS_API_KEY}"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.content

audio_bytes = query({
	"inputs": "The answer to the universe is 42",
})
# You can access the audio with IPython.display for example
# from IPython.display import Audio
# Audio(audio_bytes)