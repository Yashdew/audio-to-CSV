import speech_recognition as sr
import sys
import csv
filename = '7601-291468-0006.wav'


r = sr.Recognizer()


with sr.AudioFile(filename) as source:
    
    audio_data = r.record(source)
    
    text = r.recognize_google(audio_data)
    print(text)

with open('new.csv', 'w') as f:
        f.write(text)
        
