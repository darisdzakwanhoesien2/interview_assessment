import torch

DEVICE = 0 if torch.cuda.is_available() else -1

ASR_MODEL = "openai/whisper-medium"  
# or "openai/whisper-small" if limited resources
