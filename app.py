import speech_recognition as sr
from pydub import AudioSegment

recognizer = sr.Recognizer()

def recognize_speech(audio_file, language="hi-IN"):
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        text = recognizer.recognize_google_cloud(audio, language=language)
        print(f"Recognized Speech: {text}")
    except sr.UnknownValueError:
        print("Sorry, couldn't understand the audio.")
    except sr.Request:
        print("Couldn't request results; check your network connection.")


recognize_speech("path_to_audio_file.wav", language="mr-IN")

def convert_to_wav(input_file):
    audio = AudioSegment.from_file(input_file)
    wav_file = input_file.replace(".mp3", ".wav")
    audio.export(wav_file, format="wav")
    return wav_file