from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry('200x200+100+100')

ttk.Style().configure("TButton", padding=10, relief="flat")


def buttonClick():
    print('destroy')
    root.destroy()


button1 = ttk.Button(text="Button Example", command=buttonClick)
button1.pack(side=BOTTOM)

button2 = ttk.Button(text="Button2", command=buttonClick)
button2.pack(side=TOP)

# root.overrideredirect(1)
root.wm_attributes('-toolwindow', 'True')
root.mainloop()
