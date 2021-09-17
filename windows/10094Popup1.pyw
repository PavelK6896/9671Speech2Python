from ctypes import windll, wintypes, byref
from threading import Thread
from tkinter import *

import keyboard
import pyperclip
import pyttsx3

pyttsx3_tts = pyttsx3.init()
pyttsx3_tts.setProperty('voice', 'ru')
pyttsx3_tts.setProperty('rate', 500)
pyttsx3_tts.setProperty('volume', 0.8)
pyttsx3_tts.say('test voice')
pyttsx3_tts.runAndWait()
print(pyperclip.paste())


def clearTm():
    while (True):
        if (tm[0].is_alive() == False):
            tm.pop(0)
            break


# Out of memory
# Increases memory consumption
def action():
    print("action")
    root = Tk()

    def speak_buffer():
        print('speak_buffer')
        get = root.clipboard_get()
        print(get)
        pyttsx3_tts.say(get)

    def buttonClick():
        print('destroy')
        speak_buffer()
        root.destroy()
        t = Thread(target=clearTm)
        t.setDaemon(True)
        t.start()

    cursor = wintypes.POINT()
    windll.user32.GetCursorPos(byref(cursor))
    root.geometry('200x200+' + str(cursor.x) + '+' + str(cursor.y))

    button1 = Button(text="Button Example", command=buttonClick)
    button1.pack(side=BOTTOM)
    button2 = Button(text="Button2", command=buttonClick)
    button2.pack(side=TOP)

    root.overrideredirect(1)
    root.attributes("-topmost", True)
    root.mainloop()


tm = []


def creat():
    print(len(tm))
    if (len(tm) == 0):
        t = Thread(target=action)
        t.setDaemon(True)
        t.start()
        print(t)
        tm.append(t)
    else:
        print(tm[0].is_alive())


keyboard.add_hotkey('Ctrl + c', creat)
keyboard.wait('Ctrl + q')
