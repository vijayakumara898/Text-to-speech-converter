import playsound
from gtts import gTTS
import os


text = input("Enter your text:")

def speak(text):
    tts = gTTS(text= text, lang = "en", slow= False)
    filename=input("Enter your file name :")
    tts.save(filename+".mp3")

speak(text)