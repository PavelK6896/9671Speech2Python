from tkinter import *
import pyperclip
import threading

import pyttsx3

print("start---------------")




# voice---------------------------------------------------------

pyttsx3_tts = pyttsx3.init()
pyttsx3_tts.setProperty('voice', 'ru')
pyttsx3_tts.setProperty('rate', 1500)
pyttsx3_tts.setProperty('volume', 0.8)
pyttsx3_tts.say('тест voice')
pyttsx3_tts.runAndWait()




# thread---------------------------------------------------

def thread_function(name):

    old_buffer = pyperclip.paste()
    print("Thread %s: starting", name)

    while True:
        get = pyperclip.paste()
        if old_buffer != get:
            print(get)
            old_buffer = get
            # print(pyperclip.sizeof())
            # print(pyperclip.c_wchar)
            # print(pyperclip.PY2)


# x = threading.Thread(target=thread_function, args=(1,))
# x.start()




# buffer-------------------------------------------------------------

def speak_buffer():
    get = root.clipboard_get()
    pyttsx3_tts.say(get)
    pyttsx3_tts.runAndWait()
    print(get)




# ui-------------------------------------------------------------------

root = Tk()

root.attributes('-topmost', True)
b1 = Button(text="speak", width=5, height=5, command=speak_buffer)
# b2 = Button(text="pause", width=5, height=5, command=pause1)
# b3 = Button(text="resume", width=5, height=5, command=resume1)
# b4 = Button(text="stop", width=5, height=5, command=stop1)
b1.pack()
# b2.pack()
# b3.pack()
# b4.pack()

root.mainloop() #Меньший


print("end****************")





