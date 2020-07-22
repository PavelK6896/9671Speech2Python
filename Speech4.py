import pyttsx3
import platform

system = platform.system()  # Вернет тип системы.
bit = platform.architecture()  # Вернет кортеж, где разрядность — нулевой элемент
print(system)
print(bit)
print(bit[0])

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')  # Наш голос по умолчанию
tts.setProperty('rate', 200)  # Скорость в % (может быть > 100)
tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)
text_file = open("text1.txt", "r")  # w1251

data = text_file.read()
tts.say(data)
tts.runAndWait()
