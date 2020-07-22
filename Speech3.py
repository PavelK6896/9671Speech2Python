from datetime import datetime
import pyttsx3
import time

tts = pyttsx3.init()
tts.setProperty('voice', 'ru')  # Наш голос по умолчанию
tts.setProperty('rate', 1500)  # Скорость в % (может быть > 100)
tts.setProperty('volume', 0.8)  # Громкость (значение от 0 до 1)

print(tts.getProperty('volume'))
print(tts.getProperty('rate'))
print(tts.getProperty('voice'))
tts.runAndWait()
print(tts.getProperty('volume'))
print(tts.getProperty('rate'))
print(tts.getProperty('voice'))


def set_voice():
    # Найти и выбрать нужный голос по имени
    voices = tts.getProperty('voices')
    for voice in voices:
        if voice.name == 'Aleksandr':
            tts.setProperty('voice', voice.id)
            tts.say('тест войс')
            tts.runAndWait()
            print(tts.getProperty('volume'))
            print(tts.getProperty('rate'))
            print(tts.getProperty('voice'))
        else:
            pass


set_voice()

while True:
    time_checker = datetime.now()  # Получаем текущее время с помощью datetime
    # print(time_checker)
    time.sleep(0.1)
    print(time_checker.second)
    if time_checker.second >= 50:
        print(time_checker.second)
        tts.say('{s}'.format(s=time_checker.second))
        tts.runAndWait()
        if time_checker.second >= 58:
            tts.say('{h} {m}'.format(h=time_checker.hour, m=time_checker.minute))
            tts.runAndWait()
            print(tts.getProperty('volume'))
            print(tts.getProperty('rate'))
            print(tts.getProperty('voice'))
