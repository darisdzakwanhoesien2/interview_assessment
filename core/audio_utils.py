import ffmpeg
import os

def extract_audio(input_path, output_path, sr=16000):
    (
        ffmpeg
        .input(input_path)
        .output(output_path, ac=1, ar=sr)
        .overwrite_output()
        .run(quiet=True)
    )
    return output_path