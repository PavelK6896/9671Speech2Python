import os

os.system(""" echo "Проверка синтезатора речи" | spd-say -r 100 -p -20 -m none -o rhvoice -l ru -e -t female2 """)

# sudo apt install python3-speechd

import speechd
tts_d = speechd.SSIPClient('test')
tts_d.set_output_module('rhvoice')
tts_d.set_language('ru')
tts_d.set_rate(100)
print(tts_d.get_rate())
tts_d.set_punctuation(speechd.PunctuationMode.SOME)
tts_d.speak('И нежный вкус родимой речи так чисто губы холодит')
tts_d.close()

import platform
system = platform.system() # Вернет тип системы.
bit = platform.architecture() # Вернет кортеж, где разрядность — нулевой элемент
print(system)
print(bit[0])


