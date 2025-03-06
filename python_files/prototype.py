from elevenlabs import play, save
from elevenlabs.client import ElevenLabs
import os

client = ElevenLabs(
    api_key=os.getenv("ELEVEN_API_KEY")
)

query = input("Enter your text to convert it into voice:")

response = client(query)
save(response, 'output.mav')