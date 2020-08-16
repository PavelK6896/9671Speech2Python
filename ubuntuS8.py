import speechd
from tkinter import *
import pyperclip
import threading
import time
from tkinter import messagebox as mb


tts_d = speechd.SSIPClient('test')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
tts_d.set_voice('female1')
tts_d.set_rate(100)
tts_d.set_punctuation(speechd.PunctuationMode.SOME)

tts_d.speak('готов')


def thread_function(name):
    sdf = pyperclip.paste()
    print("Thread %s: starting", name)

    while True:
        if sdf != pyperclip.paste():
            answer = mb.askyesno(title="а", message="читать",)
            if answer == True:
                tts_d.speak(pyperclip.paste())
            else:
                print("nn")

        sdf = pyperclip.paste()


x = threading.Thread(target=thread_function, args=(1,))
x.start()


def hello_Call_Back():
    tts_d.speak(pyperclip.paste())


def pause1():
    print("ps")
    tts_d.pause()


def resume1():
    print("cn")
    tts_d.resume()


def stop1():
    print("cn")
    tts_d.stop()


root = Tk()
root.attributes('-topmost', True)
b1 = Button(text="speak", width=5, height=5, command=hello_Call_Back)
b2 = Button(text="pause", width=5, height=5, command=pause1)
b3 = Button(text="resume", width=5, height=5, command=resume1)
b4 = Button(text="stop", width=5, height=5, command=stop1)
b1.pack()
b2.pack()
b3.pack()
b4.pack()
root.mainloop()

tts_d.speak('конец')
tts_d.close()
