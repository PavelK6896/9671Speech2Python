import pyperclip
import pyttsx3
import time

pyperclip.copy('Hello world!')

tts = pyttsx3.init()
voices = tts.getProperty('voices')
for voice in voices:
    if voice.name == 'russian':
        en2 = voice.id

tts.setProperty('rate', 300)  # Скорость в % (может быть > 100)
tts.setProperty('volume', 1.0)  # Скорость в % (может быть > 100)
tts.setProperty('voice', en2)
tts.say(pyperclip.paste())
tts.runAndWait()

str = pyperclip.paste()

while True:
    if str != pyperclip.paste():

        str = pyperclip.paste()
        tts.say(str)
        tts.runAndWait()

print("close")



