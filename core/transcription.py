from transformers import pipeline
from .config import ASR_MODEL, DEVICE
import torch

def run_asr(audio_path):
    asr = pipeline(
        "automatic-speech-recognition",
        model=ASR_MODEL,
        torch_dtype=torch.float16 if DEVICE == 0 else torch.float32,
        device=DEVICE
    )

    result = asr(audio_path, return_timestamps=True)

    return result["chunks"]