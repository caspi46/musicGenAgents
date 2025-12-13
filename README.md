# musicGenAgents

Fun winter project for multi-agent system to generate short music (30 sec).

## Project Overview

This project implements a multi-agent system for music generation using **LangChain** and **LangGraph**.

### Agents

1.  **Producer Agent**: Orchestrator of the system.
2.  **Composer Agent**: Generates the main melody and chords.
3.  **Arranger Agent**: Arranges the music from the composer.

---

## Workflow

The **Producer Agent** communicates with all agents and coordinates the workflow:

1.  **Producer Agent** receives the user prompt and generates the requirements (JSON).
2.  **Composer Agent** receives the requirements and generates the melody and chords.
3.  **Arranger Agent** receives the requirements, melody, and chords. It arranges the music by adding instruments based on the requirements and enhancing harmony.
4.  **Producer Agent** checks each agent's work.

## Specifications & Requirements

### Parameters

1.  **Genre**: pop, rock, hip hop, electronic, country, jazz, blues, classical, world, metal
2.  **Tempo**: slow, medium, fast
3.  **Mood**: happy, sad, angry, excited, calm, relaxed
4.  **Instruments**: piano, guitar, bass, drums, violin, cello, flute, trumpet, saxophone, trombone
5.  **Key**: C, D, E, F, G, A, B
6.  **Time Signature**: 4/4, 3/4, 5/4, 6/8, 7/8
7.  **Chord Progression**: I, ii, iii, IV, V, vi, vii
8.  **Melody**: simple, complex, original
9.  **Harmony**: simple, complex, original
10. **Rhythm**: simple, complex, original
11. **Combinations**: (Melody+Harmony, Melody+Rhythm, etc.) -> simple, complex, original
12. **Specific Keywords**: list of keywords

### Requirements Example (JSON)

```json
{
    "genre": "pop",
    "tempo": "slow",
    "mood": "happy",
    "instruments": ["piano", "guitar", "bass", "drums"],
    "key": "C",
    "time_signature": "4/4",
    "chord_progression": ["I", "ii", "iii", "IV", "V", "vi", "vii"],
    "meter": "4/4",
    "melody": "simple",
    "harmony": "simple",
    "rhythm": "simple",
    "melody_and_harmony": "simple",
    "melody_and_rhythm": "simple",
    "harmony_and_rhythm": "simple",
    "melody_harmony_and_rhythm": "simple",
    "specific_keywords": ["happy", "sad", "angry", "excited", "calm", "relaxed"]
}
```

## Data Formats

### Composer Agent's Measure Format (JSON)
1.  **Main Melody**: list of notes with measure
2.  **Chords**: list of chords with measure

### Proposed Measure Notation
`|A--B|C---|D--E|F-..|`

*   `|`: Represents the measure
*   `-`: Represents the note (sustain/hold)
*   `.`: Represents a rest (no note)

## Limitations

1.  Music duration is fixed to **30 seconds**.
2.  **Limited Instruments**: piano, guitar, bass, and drums (for now).
