import streamlit as st
from separate_audio import separate_audio
import os

st.set_page_config(page_title="Audio Separator", layout="centered")
st.title("🎵 Audio Vocal & Instrument Splitter")

uploaded_file = st.file_uploader("Upload an audio file (MP3, WAV, etc.)", type=["mp3", "wav", "m4a", "flac"])

if uploaded_file is not None:
    st.audio(uploaded_file, format='audio/mp3')

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.read())

    with st.spinner("Separating vocals and music..."):
        vocals_path, instruments_path = separate_audio(uploaded_file.name)

    st.success("Separation complete!")

    st.subheader("🔊 Vocals")
    st.audio(vocals_path)

    st.download_button("Download Vocals", open(vocals_path, 'rb'), file_name="vocals.wav")

    st.subheader("🎶 Instrumental")
    st.audio(instruments_path)

    st.download_button("Download Instrumental", open(instruments_path, 'rb'), file_name="instrumental.wav")

    # Clean up
    os.remove(uploaded_file.name)
