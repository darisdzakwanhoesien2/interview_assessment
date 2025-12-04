from datetime import timedelta

def merge_diarization_asr(segments, chunks):
    merged = []

    for c in chunks:
        start = c["timestamp"][0]
        end = c["timestamp"][1]
        text = c["text"]

        # find which speaker matches this timestamp
        speaker = "Unknown"
        for seg in segments:
            if seg["start"] <= start <= seg["end"]:
                speaker = seg["speaker"]
                break

        merged.append({
            "speaker": speaker,
            "start": str(timedelta(seconds=start)),
            "end": str(timedelta(seconds=end)),
            "text": text
        })

    return merged