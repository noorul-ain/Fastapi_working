from pydantic import BaseModel
from typing import List

class TextToSpeechRequest(BaseModel):
    text: str
    languages: List[str]
