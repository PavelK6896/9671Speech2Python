import pyperclip
import pyttsx3
from tkinter import *
import keyboard


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

def onWord(name, location, length):
    print('word', name, location, length)

    if location > 50:
        print("10 stop stop")
        print(dir(tts))
        tts.stop()
        tts.proxy.stop()
        tts.proxy._driver.stop()
        tts._driver.stop()
        tts.disconnect()
        pyttsx3._driver.stop()
        pyttsx3.proxy.stop()


    if keyboard.is_pressed("esc"):
        print("esc")
        tts.stop()



# //кнопка
def helloCallBack():
    str = pyperclip.paste()
    tts.say(str)
    tts.connect('started-word', onWord)
    tts.runAndWait()

# //кнопка2
# def copy_clipboard():
#     print("copy_clipboard")
#     # pya.doubleClick(pya.position())
#     # pya.hotkey('ctrl', 'a')
#     pya.hotkey('ctrl', 'c')
#     print(pyperclip.paste())
#     time.sleep(.01)
#     return pyperclip.paste()


# def readCallBack():
#     print("read")
#     str = copy_clipboard()
#     tts.say(str)
#     tts.runAndWait()

# //кнопка3
def stopCallBack():
    print("stop")
    tts.stop()


root = Tk()
# поверх всех окон
root.attributes('-topmost', True)
# root.update()
# root.attributes('-topmost', False)

b1 = Button(text="speak", width=5, height=5, command=helloCallBack)
# b2 = Button(text="read", width=5, height=5, command=readCallBack)
# b3 = Button(text="stop", width=5, height=5, command=stopCallBack)
b1.pack()
# b2.pack()
# b3.pack()
root.mainloop()


print("close")

