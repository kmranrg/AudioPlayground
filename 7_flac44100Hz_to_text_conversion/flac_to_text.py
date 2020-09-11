#pip install SpeechRecognition

import speech_recognition as s

r = sr.Recognizer()

harvard = sr.AudioFile('myfile.flac')

with harvard as source:
    audio = r.record(source)

print(type(audio))
print(r.recognize_google(audio))
