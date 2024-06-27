from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
import os


client = ElevenLabs(
  api_key= os.getenv('ELEVEN_API_KEY') , # Defaults to ELEVEN_API_KEY
)

audio = client.generate(
  text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
  voice="Rachel",
  model="eleven_multilingual_v2"
)

save(audio, "hello.mp3")

#Streaming audio

from elevenlabs.client import ElevenLabs
from elevenlabs import stream

client = ElevenLabs(
  api_key="YOUR_API_KEY", # Defaults to ELEVEN_API_KEY
)

audio_stream = client.generate(
  text="This is a... streaming voice!!",
  stream=True
)

stream(audio_stream)


#Streaming input

from elevenlabs.client import ElevenLabs
from elevenlabs import stream

client = ElevenLabs(
  api_key="YOUR_API_KEY", # Defaults to ELEVEN_API_KEY
)

def text_stream():
    yield "Hi there, I'm Eleven "
    yield "I'm a text to speech API "

audio_stream = client.generate(
    text=text_stream(),
    voice="Nicole",
    model="eleven_monolingual_v1",
    stream=True
)

stream(audio_stream)