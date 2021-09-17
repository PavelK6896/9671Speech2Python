import tkinter

import pyperclip
import pyttsx3

pyttsx3_tts = pyttsx3.init()
pyttsx3_tts.setProperty('voice', 'ru')
print("dddd")
pyttsx3_tts.setProperty('rate', 500)
pyttsx3_tts.setProperty('volume', 0.8)
pyttsx3_tts.say('тест voice')
pyttsx3_tts.runAndWait()


def thread_function(name):
    old_buffer = pyperclip.paste()
    while True:
        get = pyperclip.paste()
        if old_buffer != get:
            old_buffer = get


def speak_buffer():
    get = root.clipboard_get()
    pyttsx3_tts.say(get)
    pyttsx3_tts.runAndWait()


root = tkinter.Tk()
root.attributes('-topmost', True)
b1 = tkinter.Button(text="speak", width=5, height=5, command=speak_buffer)
b1.pack()
root.mainloop()
