import pyttsx3
print(dir(pyttsx3))

tts = pyttsx3.init()
voices = tts.getProperty('voices')

for voice in voices:
    print('Имя: %s' % voice.name)

    if voice.name == 'russian':
        en2 = voice.id

    if voice.name == 'english-us':
        en3 = voice.id
        # break


tts.setProperty('rate', 500)  # Скорость в % (может быть > 100)
tts.setProperty('volume', 1.0)  # Скорость в % (может быть > 100)
tts.setProperty('voice', en2)
tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
tts.runAndWait()

tts.setProperty('voice', en3)
tts.say("Can you hear me say it's a lovely day?")
tts.runAndWait()





