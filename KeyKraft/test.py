import tkinter as tk
from tkinter import filedialog

root = tk.Tk()


def pathdef():
    print(filedialog.askdirectory())


root.button = tk.Button(command=pathdef, width=100)
root.button.pack()

root.mainloop()

