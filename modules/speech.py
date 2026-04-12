import speech_recognition as sr

def speech_to_text(audio_file):
    r = sr.Recognizer()
    try:
        with sr.AudioFile(audio_file) as source:
            audio = r.record(source)
        return r.recognize_google(audio)
    except:
        return "Audio not clear or wrong format"
