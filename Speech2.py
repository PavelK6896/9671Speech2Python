import pyttsx3

tts = pyttsx3.init()
voices = tts.getProperty('voices')
# Задать голос по умолчанию
tts.setProperty('voice', 'ru')
# Попробовать установить предпочтительный голос
en2 = 0
ru2 = 0
for voice in voices:
    ru = voice.id.find('Aleksandr')
    if ru > -1:
        print('Aleksandr')
    en = voice.id.find('Alan')
    if en > -1:
        print('Alan')

    if voice.name == 'Alan':
        en2 = voice.id

    if voice.name == 'Aleksandr':
        ru2 = voice.id
        tts.setProperty('voice', voice.id)
        tts.setProperty('rate', 500)  # Скорость в % (может быть > 100)
        tts.setProperty('volume', 0.9)  # Скорость в % (может быть > 100)
# очередь из текста
tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
tts.runAndWait()
print(tts.getProperty("volume"))
# print(tts.getPropert("rate"))
print(tts.getProperty('voices'))

tts.setProperty('voice', en2)
tts.say("Can you hear me say it's a lovely day?")
# Теперь — русский

tts.setProperty('voice', ru2)
tts.say("А напоследок я скажу")
tts.runAndWait()
