import streamlit as st
import tempfile
from core.audio_utils import extract_audio
from core.diarization import run_diarization
from core.transcription import run_asr
from core.merge import merge_diarization_asr
from ui.layout import header

st.set_page_config(page_title="Speaker Transcriber", layout="wide")

header()

hf_token = st.sidebar.text_input("HuggingFace Token for diarization", type="password")

uploaded = st.file_uploader("Upload audio/video", type=["mp3", "wav", "mp4", "mov", "m4a"])

if uploaded:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded.read())
        input_path = tmp.name

    audio_path = input_path + ".wav"
    extract_audio(input_path, audio_path)

    # Step 1 — diarization
    if hf_token:
        with st.spinner("Running diarization…"):
            segments = run_diarization(audio_path, hf_token)
        st.success(f"Diarization complete! Found {len(segments)} segments.")
        st.json(segments)

    # Step 2 — transcription
    with st.spinner("Running ASR…"):
        chunks = run_asr(audio_path)
    st.success("Transcription complete!")

    # Step 3 — merge
    merged = merge_diarization_asr(segments, chunks)

    st.subheader("Final Transcript")
    for m in merged:
        st.write(f"**{m['speaker']} [{m['start']}]:** {m['text']}")

    st.download_button("Download JSON", data=str(merged), file_name="transcript.json")