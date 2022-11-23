# %% try1:ひどい出来だがまあ動く
from piano_transcription_inference import PianoTranscription, sample_rate, load_audio
import numpy
import os
import torch

def mp3tomidi(a_mp3path):
    t_mp3path = a_mp3path
    t_outputFile = os.path.splitext(os.path.basename(t_mp3path))[0] + '.mid'
    # Load audio
    (audio, _) = load_audio(t_mp3path, sr=sample_rate, mono=True)

    # Transcriptor
    transcriptor = PianoTranscription(device='cuda', checkpoint_path=None)    # type: ignore # 'cuda' | 'cpu'

    # Transcribe and write out to MIDI file
    transcribed_dict = transcriptor.transcribe(audio, t_outputFile)

