# Цветовая схема:
#   фон = #140226 (тёмно-синий)
#   текст, альт-фон = #f1f3e7 (бежевый)
#   текст, слайдер = #a3124a (вишнёвый)

import tkinter as tk
import break_in as bi
import os
import keygen as kg
import string
from tkinter import filedialog as fd

# Блок основы

root = tk.Tk()
root.wall_lbl = tk.PhotoImage(file='wall.png')
root.label = tk.Label(root, image=root.wall_lbl, bg='white')
root.label.place(x=0, y=0, relwidth=1, relheight=1)
root.overrideredirect(True)
root.geometry("+250+250")
root.lift()
root.wm_attributes("-topmost", True)
root.wm_attributes("-transparentcolor", "white")
root.label.pack()


# Блок адресной строки

def pathbutton():
    fd_path = fd.askdirectory()
    root.path.insert(0, fd_path)

root.path_label = tk.Label(root, text='Path', background='#140226', foreground='#a3124a', font=('Arial', 14, 'bold'),
                           relief='flat')
root.path_label.place(x=38, y=218)

root.path = tk.Entry(root, fg='#140226', background='#a3124a', selectbackground='#140226', selectforeground='#f1f3e7',
                     font='Arial', relief='flat')
root.path.place(x=90, y=222, width=197, height=21)

root.pathbutton = tk.Button(root, text='...', background='#a3124a', foreground='#140226', activebackground='#f1f3e7', command=pathbutton)
root.pathbutton.place(x=289, y=222, width=21, height=22)


# Блок слайдера

root.pass_len = tk.Label(root, text='Length', background='#140226', foreground='#a3124a', font=('Arial', 14, 'bold'),
                         relief='flat')
root.pass_len.place(x=38, y=260)

length = tk.IntVar()

root.scale = tk.Scale(root, relief='flat', sliderrelief='flat', highlightthickness=0, variable=length,
                      background='#140226', foreground='#f1f3e7', activebackground='#a3124a', from_=0, to=16,
                      resolution=1)
root.scale.configure(orient='horizontal', length=180, width=12)
root.scale.place(x=112, y=247, width=199)

# Блок выбора символов

symbols = tk.BooleanVar()
digits = tk.BooleanVar()
letters = tk.BooleanVar()

root.lable_sym = tk.Label(root, text='Symbols', background='#140226', foreground='#f1f3e7', font=('Arial', 11),
                          relief='flat')
root.lable_sym.place(x=38, y=295)

root.rad_sym = tk.Checkbutton(root, background='#140226', foreground='#f1f3e7', selectcolor='#a3124a',
                              activebackground='#140226', variable=symbols, onvalue=True, offvalue=False)
root.rad_sym.place(x=98, y=295)

root.lable_dig = tk.Label(root, text='Digits', background='#140226', foreground='#f1f3e7', font=('Arial', 11),
                          relief='flat')
root.lable_dig.place(x=152, y=295)

root.rad_dig = tk.Checkbutton(root, background='#140226', foreground='#f1f3e7', selectcolor='#a3124a',
                              activebackground='#140226', variable=digits, onvalue=True, offvalue=False)
root.rad_dig.place(x=192, y=295)

root.lable_let = tk.Label(root, text='Letters', background='#140226', foreground='#f1f3e7', font=('Arial', 11),
                          relief='flat')
root.lable_let.place(x=244, y=295)

root.rad_let = tk.Checkbutton(root, background='#140226', foreground='#f1f3e7', selectcolor='#a3124a',
                              activebackground='#140226', variable=letters, onvalue=True, offvalue=False)
root.rad_let.place(x=292, y=295)


# Кнопка Генератор


def Radio():
    test = kg.KeyGen(r'%s\keys' % home.path)

    contents = ''
    if symbols.get():
        contents += string.punctuation

    if digits.get():
        contents += string.digits

    if letters.get():
        contents += string.ascii_letters

    if contents != '':
        test.keygen(length.get(), contents, f'{test.path}/{test.filename}')
    else:
        print("No printables are selected!")

root.generator_lbl = tk.PhotoImage(file='generate.png')
root.generator = tk.Button(image=root.generator_lbl, state='disabled', bg='#140226', relief='flat', command=Radio)
root.generator.place(x=86, y=324)
root.generator.configure(disabledforeground='#140226', activebackground='#140226')


# Кнопка Exit

def Exit():
    root.destroy()


root.exit_lbl = tk.PhotoImage(file='exit.png')
root.exit = tk.Button(image=root.exit_lbl, bg='#140226', relief='flat', command=Exit)
root.exit.place(x=318, y=220)
root.exit.configure(disabledforeground='#140226', activebackground='#140226')


# Блок описывающий перетаскивание основного окна курсором

def StartMove(event):
    root.x = event.x
    root.y = event.y


def StopMove(event):
    root.x = None
    root.y = None


def OnMotion(event):
    deltax = event.x - root.x
    deltay = event.y - root.y
    x = root.winfo_x() + deltax
    y = root.winfo_y() + deltay
    root.geometry("+%s+%s" % (x, y))


root.bind("<ButtonPress-1>", StartMove)
root.bind("<ButtonRelease-1>", StopMove)
root.bind("<B1-Motion>", OnMotion)

# Инициализация папки

home = bi.Space()

root.create_home_lbl = tk.PhotoImage(file='check.png')
root.destroy_home_lbl = tk.PhotoImage(file='check2.png')
root.check = tk.Button(image=root.create_home_lbl, bg='#140226', relief='flat')

def Home():
    if root.path.get() == '':
        print("You didn't enter the path, using default")
    else:
        home.path = root.path.get()
        print(f'Root path = {home.path}')
    if not os.path.exists(r'%s\keys' % home.path):
        home.create_space(home.path)
        root.generator.configure(state='active')
        root.check.configure(image=root.destroy_home_lbl)
        print('Home created!')
    elif os.path.exists(r'%s\keys' % home.path):
        home.clear_space(home.path)
        root.generator.configure(state='disabled')
        root.check.configure(image=root.create_home_lbl)
        print('Home deleted')


root.check.place(x=204, y=324)
root.check.configure(disabledforeground='#140226', activebackground='#140226', command=Home)

# Активация окна

root.mainloop()
