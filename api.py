import gradio as gr
from gradio_client import Client, handle_file

def api(text: str):
    client = Client("tonyassi/voice-clone")
    try:
        print("Starting prediction...")
        audio_file = './tanishka.wav'
        print(f"Audio file handled: {audio_file}")
        result = client.predict(
            text=text,
            audio=audio_file,
            api_name="/predict"
        )
        print(f"Prediction result: {result}")
        return result['audio']
    except Exception as e:
        gr.Error("Error during prediction: {e}")
        print(f"Error during prediction: {e}")
        return None

gr.Interface(fn=api, inputs="text", outputs=gr.Audio(type='filepath')).launch(show_error=True, debug=True)
