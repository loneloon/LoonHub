import tkinter as tk
import datetime
from client import Network


net = Network()

print_cash = ''
chat_feed = ''
user_input = ''
message_sent = False
time_sent = None

last_sync = datetime.datetime.now()
token = ''


recent_position = "+550+250"


class Main:
    def __init__(self, orient):
        self.sync_stop = False

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

        root.chat_win = tk.Label(root, text=chat_feed, bg='black', fg='white', relief='flat',
                                 font=('Arial', 12, 'bold'), compound='right', justify='right')
        root.chat_win.place(x=270, y=90, width=400, height=150)

        root.chat_input = tk.Entry(root, bg='red', fg='white', relief='flat',
                                   font=('Arial', 16, 'bold'))
        root.chat_input.place(x=270, y=270, width=400, height=50)

        def Send():
            global message_sent, time_sent, chat_feed, user_input, token, print_cash

            print_cash = root.chat_input.get()
            if print_cash != '':
                user_input += f'\n{print_cash}'
                print_cash = ''

        root.send_button.configure(command=Send)

        def sync():
            global message_sent, time_sent, chat_feed, user_input, token, print_cash

            if user_input != '':
                net.send(user_input)  # withheld messages are sent
                user_input = ''  # user's own message cash wiped

            if net.chat_feed != '':
                token = net.chat_feed[-3:]  # token recovered from the message delivery
                if token == '000':
                    print('\nServer is shutting down!')
                    self.sync_stop = True
                    token = ''
                if token == '666':
                    chat_feed += f"\nServer says:{net.chat_feed[:-3]}"
                    token = ''
                    net.chat_feed = ''
                else:
                    net.send(token)  # token sent back as a validation of receipt
                    token = ''  # token wiped
                    chat_feed += f"\n{net.chat_feed[:-3]}"  # message stripped off its token and added to user's chat history/displayed
                    net.chat_feed = ''  # initial message wiped

            net.read()  # requesting to read the message feed, socket is locked unless the message exists to stop listening

            root.chat_win.configure(text=chat_feed)
            root.after(100, sync)

        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='img/exit.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#df7126', relief='flat', command=Exit)
        root.exit.place(x=656, y=25, width=41, height=45)
        root.exit.configure(activebackground='#000000')

        # Блок описывающий перетаскивание основного окна курсором

        def StartMove(event):
            self.sync_stop = True
            root.x = event.x
            root.y = event.y
            self.sync_stop = False

        def StopMove(event):
            self.sync_stop = True
            root.x = None
            root.y = None
            self.sync_stop = False

        def OnMotion(event):
            self.sync_stop = True
            deltax = event.x - root.x
            deltay = event.y - root.y
            x = root.winfo_x() + deltax
            y = root.winfo_y() + deltay
            root.geometry("+%s+%s" % (x, y))
            self.sync_stop = False

        root.bind("<ButtonPress-1>", StartMove)
        root.bind("<ButtonRelease-1>", StopMove)
        root.bind("<B1-Motion>", OnMotion)

        if not self.sync_stop:
            sync()
        root.mainloop()


Main(recent_position)