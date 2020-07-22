from gtts import gTTS
from googletrans import Translator

translator = Translator()
text1 = 'Customizable speech-specific sentence tokenizer that allows for unlimited ' \
        'lengths of text to be read, all while keeping proper intonation, abbreviations, decimals and more;'
text2 = 'Иван Федорович Крузенштерн. Человек и пароход!'
result1 = translator.translate(text1, src='en', dest='ru')
print(result1.text)

tts = gTTS(result1.text, lang='ru', slow=False)
tts.save('text1.mp3')

tts = gTTS(text2, lang='ru', slow=False)
tts.save('text2.mp3')
