from spleeter.separator import Separator
import os
import shutil
import tempfile
from pydub import AudioSegment

def convert_to_wav(input_audio_path):
    audio = AudioSegment.from_file(input_audio_path)
    wav_path = os.path.splitext(input_audio_path)[0] + "_converted.wav"
    audio.export(wav_path, format="wav")
    return wav_path

def separate_audio(input_audio_path):
    # Convert to WAV if not already
    if not input_audio_path.endswith('.wav'):
        input_audio_path = convert_to_wav(input_audio_path)

    temp_dir = tempfile.mkdtemp()
    separator = Separator('spleeter:2stems')
    separator.separate_to_file(input_audio_path, temp_dir)

    output_folder = os.path.join(temp_dir, os.path.splitext(os.path.basename(input_audio_path))[0])
    vocals_path = os.path.join(output_folder, 'vocals.wav')
    accompaniment_path = os.path.join(output_folder, 'accompaniment.wav')

    return vocals_path, accompaniment_path
