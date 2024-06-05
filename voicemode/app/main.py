from fastapi import FastAPI, HTTPException
from gtts import gTTS
import os

app = FastAPI()

@app.get("/tts/",tags=["Text2voice"])
async def text_to_speech(text: str, lang: str = "en"):
        # Check if language is supported

    supported_languages =  ["en", "fr", "es", "de", "it", "pt"] 
    if lang not in supported_languages:
        raise HTTPException(status_code=400, detail="Unsupported language")

    # Generate speech
    tts = gTTS(text=text, lang=lang)
    speech_folder = os.path.join(os.getcwd(), "speech", lang) 
    os.makedirs(speech_folder, exist_ok=True)
    speech_file = os.path.join(speech_folder, "output.mp3")
    tts.save(speech_file)

    return {"speech_path": speech_file}
