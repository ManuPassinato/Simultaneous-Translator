from TTS.api import TTS
from whisper_mic_main.whisper_mic.whisper_mic import WhisperMic
import click
import torch
import os

if __name__ == '__main__':

    model = 'small' #["tiny","base", "small","medium","large"]
    english = False
    device = "cuda" if torch.cuda.is_available() else "cpu"
    verbose = False
    energy = 300
    pause = 2.0
    dynamic_energy = False
    save_file = False
    mic = WhisperMic(model=model , english=english, verbose=verbose, energy=energy, pause=pause, dynamic_energy=dynamic_energy, save_file=save_file, device=device)
    result = mic.listen()
   
    os.environ['COQUI_STUDIO_TOKEN'] = '2ne56KLglcpcJmSFosnz34Mjdw2QD6oBnXm7xCm9zfKjUc2gKKQce50mB5rLjI48'
    model_name = TTS.list_models()[0]
    tts = TTS(model_name, progress_bar=True, gpu=False)
    tts.tts_to_file(result, speaker_wav="TTS_dev/output/oi.wav", language="en", file_path="output.wav")
    