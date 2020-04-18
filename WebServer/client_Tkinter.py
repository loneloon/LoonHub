import tkinter as tk
import datetime
from _thread import *
from client import Network
import client2_copy
import sys

recent_position = "+550+250"



user_input = ''
user_name = f"black_dog58"
chat_text = ''
data = ''


client = client2_copy
p2p = client2_copy.p2p

for peer in p2p.peers:
    try:
        client = client2_copy.Client(peer)
        break
    except KeyboardInterrupt:
        sys.exit(0)

class Main:
    def __init__(self, orient):

        root = tk.Tk()

        root.main_lbl = tk.PhotoImage(file='img/body.png')

        root.label = tk.Label(root, image=root.main_lbl, bg='#CD0074')
        root.label.place(x=0, y=0, relwidth=1, relheight=1)
        root.overrideredirect(True)
        root.geometry(orient)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", "#CD0074")
        root.label.pack()

        root.send_button_pic = tk.PhotoImage(file='img/send.png')
        root.send_button = tk.Button(root, image=root.send_button_pic, bg='#df7126', relief='flat')
        root.send_button.place(x=497, y=340, width=187, height=52)


        root.key_button_pic = tk.PhotoImage(file='img/key.png')
        root.key_button = tk.Button(root, image=root.key_button_pic, bg='#df7126', relief='flat')
        root.key_button.place(x=86, y=272, width=102, height=49)

        root.glasses_button_pic = tk.PhotoImage(file='img/glasses.png')
        root.glasses_button = tk.Button(root, image=root.glasses_button_pic, bg='#df7126', relief='flat')
        root.glasses_button.place(x=86, y=340, width=100, height=35)

        root.chat_win = tk.Label(root, text=chat_text, bg='black', fg='white', relief='flat',
                                 font=('Arial', 20, 'bold'))
        root.chat_win.place(x=270, y=90, width=400, height=150)

        root.chat_input = tk.Entry(root, bg='red', fg='white', relief='flat',
                                 font=('Arial', 20, 'bold'))
        root.chat_input.place(x=270, y=270, width=400, height=50)


        def Submit():
            global user_input

            if root.chat_input.get() != '':
                user_input = root.chat_input.get()

                root.chat_input.delete(0, 'end')

        root.send_button.configure(command=Submit)


        def runclient():
            global data
            data = client.sock.recv(1024)
            if not data:
                pass
            if data[0:1] == b'\x11':
                client.updatePeers(data[1:])
            else:
                print(str(data, 'utf-8'))


        def refresh():
            global chat_text, user_input

            root.chat_win.configure(text=chat_text)
            root.after(100, refresh)

        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='img/exit.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#df7126', relief='flat', command=Exit)
        root.exit.place(x=656, y=25, width=41, height=45)
        root.exit.configure(activebackground='#000000')

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

        root.after_idle(runclient())
        root.after_idle(refresh())
        root.mainloop()


Main(recent_position)