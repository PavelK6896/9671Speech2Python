import keyboard

keyboard.add_hotkey('Ctrl + h', lambda: print('Hello с!'))
keyboard.add_hotkey('Ctrl + c', lambda: print('Hello h!'))

keyboard.wait('Ctrl + Q')
