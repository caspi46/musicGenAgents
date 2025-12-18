from enum import Enum

class Genre(str, Enum):
    POP = "Pop"
    ROCK = "Rock"
    HIP_HOP = "Hip Hop"
    JAZZ = "Jazz"
    CLASSICAL = "Classical"
    ELECTRONIC = "Electronic"
    RNB = "R&B"
    COUNTRY = "Country"
    BLUES = "Blues"
    REGGAE = "Reggae"

class Tempo(str, Enum):
    SLOW = "Slow"
    MEDIUM = "Medium"
    FAST = "Fast"

class Mood(str, Enum):
    HAPPY = "Happy"
    SAD = "Sad"
    ANGRY = "Angry"
    EXCITED = "Excited"
    CALM = "Calm"
    RELAXED = "Relaxed"

class Instrument(str, Enum):
    PIANO = "Piano"
    ACOUSTIC_GUITAR = "Acoustic Guitar"
    ELECTRIC_GUITAR = "Electric Guitar"
    DRUMS = "Drums"
    ELECTRIC_BASS = "Electric Bass"
    SYNTHESIZER = "Synthesizer"
    PAD = "Pad"
    TAMBOURINE = "Tambourine"

class Key(str, Enum):
    C = "C"
    D = "D"
    E = "E"
    F = "F"
    G = "G"
    A = "A"
    B = "B"
    C_SHARP = "C#"
    D_SHARP = "D#"
    F_SHARP = "F#"
    G_SHARP = "G#"
    A_SHARP = "A#"
    B_FLAT = "Bb"
    D_FLAT = "Db"
    E_FLAT = "Eb"
    G_FLAT = "Gb"
    A_FLAT = "Ab"

# Legacy support lists (optional, can be removed if not needed)
MUSIC_GENRES = [g.value for g in Genre]

TEMPOS = [t.value for t in Tempo]

MOODS = [m.value for m in Mood]

INSTRUMENTS = [i.value for i in Instrument]

KEYS = [k.value for k in Key]


KEYWORDS = [ ]