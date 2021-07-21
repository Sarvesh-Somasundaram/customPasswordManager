from tkinter.constants import COMMAND
from secret import get_secret_key
from menu import menu
import tkinter as tk

secret = get_secret_key()

root = tk.Tk()
root.title("Password Manager")

def check():
    passwd = entry1.get()
    if passwd == secret:
        print('You\'re in')

    else:
        print('Sorry wrong password')
        root.destroy() 

    root.destroy()
    menu()
    

canvas1 = tk.Canvas(root, width = 200, height = 100)
canvas1.grid(row = 0, column = 0)

tk.Label(root, text="Enter the master password: ").grid(row = 0, column = 0)

entry1 = tk.Entry(root, show = "*")
entry1.grid(row = 1, column = 0, pady = (0, 50))

tk.Button(root, text='Enter', command=check).grid(row = 2, column = 0)

root.mainloop()
