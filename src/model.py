from pydantic import BaseModel
from typing import List 
from .constraints import MUSIC_GENRES 

class SongRequirements(BaseModel): 
    genre: str
    tempo: int 
    mood: str 
    pass 