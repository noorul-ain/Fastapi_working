from fastapi import FastAPI, HTTPException
from gtts import gTTS
import os
from app.schemas import TextToSpeechRequest

app = FastAPI()

# Ensure the voices directory exists
voices_dir = os.path.join(os.path.dirname(__file__), '..', 'voices')
os.makedirs(voices_dir, exist_ok=True)

@app.post("/convert_text_to_speech/")
async def convert_text_to_speech(request: TextToSpeechRequest):
    response = {}
    for lang in request.languages:
        try:
            tts = gTTS(text=request.text, lang=lang)
            filename = f"speech_{lang}.mp3"
            filepath = os.path.join(voices_dir, filename)
            tts.save(filepath)
            response[lang] = filename
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    return response
