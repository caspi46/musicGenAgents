from pydantic import BaseModel
from typing import List 
from .constraints import Genre, Tempo, Mood, Key, Instrument

class SongRequirements(BaseModel): 
    genre: List[Genre]
    tempo: Tempo 
    mood: List[Mood]
    key: Key

class Track(BaseModel):
    instrument: Instrument
    notes: List[str] 
    audio_file_path: str

class Song(BaseModel):
    tracks: List[Track]
    requirements: SongRequirements
    total_duration: int 