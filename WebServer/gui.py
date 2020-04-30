import tkinter as tk
import datetime
from client import Network
import string

net = Network()

print_cash = ''
chat_feed = ''
user_input = ''
message_sent = False
time_sent = None

last_sync = datetime.datetime.now()
token = ''

username = 'golden_goose66'

chat_history = open("chat_history", "w")
chat_history.write(f'=Recorded on {str(datetime.datetime.now())[0:10]}=\r\n')
chat_history.close()

try:
    lvl1codes = net.getCode()[:-3]
    print(f'Got primary codes. Size: {len(lvl1codes)}')
except:
    print("No connection to server. Didn't get codes!")

symbols = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' + string.printable[:-4]
pc_List = []
pc_Dict = {}
encoder_state = True


def primary_code_to_list():
    global pc_List

    pc_List = []

    c_line = ''

    for i in lvl1codes:
        if len(c_line) == 4:
            pc_List.append(c_line)
            c_line = ''
        c_line += i


def primary_codelist_to_dict():
    global symbols, pc_List, pc_Dict

    pc_Dict = {i: j for i, j in zip(pc_List, symbols)}


try:
    primary_code_to_list()
    primary_codelist_to_dict()

    print('Primary codes allocated')
    print('Encoding enabled.')
except:
    encoder_state = False
    print('Warning! Encoding was not enabled due to an internal error!\r\nENCODING IS OFF!')


def prim_encode(text_input):
    global pc_Dict

    message = ''

    for i in text_input:
        for code, symb in pc_Dict.items():
            if i == symb:
                message += code

    return message


def prim_decode(message):
    global pc_Dict, lines

    readcode = True
    translate = ''
    line = ''

    for i in message:
        if i == '\n' or i == '\r':
            translate += i
        else:
            if i == '=':
                translate += i

                if readcode:
                    readcode = False
                elif not readcode:
                    readcode = True

                continue
            if not readcode:
                translate += i
            else:
                if i in string.digits:
                    line += i
                if len(line) == 4:
                    for j, k in pc_Dict.items():
                        if line == j:
                            translate += k
                            line = ''

    return translate


hist_temp = []

recent_position = "+550+250"


def write_to_his(message):
    global username

    chat_history = open("chat_history", "a+")
    chat_history.write(f"={str(datetime.datetime.now())[11:-7]}=\r{message}\r\n")
    chat_history.close()


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

        root.chat_win = tk.Label(root, text=chat_feed, bg='white', fg='black', relief='flat',
                                 font=('Arial', 10, 'bold'), anchor='e', justify='right')
        root.chat_win.place(x=270, y=90, width=400, height=150)

        root.chat_input = tk.Entry(root, bg='white', fg='black', relief='flat',
                                   font=('Arial', 16, 'bold'))
        root.chat_input.place(x=270, y=270, width=400, height=50)

        def HistoryUpdate():
            global hist_temp, chat_feed

            hist_temp = ['\n']

            with open("chat_history", "r") as h:
                tot = len(h.readlines())
            with open("chat_history", "r") as h:
                for idx, i in enumerate(h.readlines()):
                    if tot > 5:
                        if idx > (tot - 6):
                            hist_temp.append(i)
                    else:
                        hist_temp.append(i)
            h.close()

            chat_feed = prim_decode("\r".join(hist_temp))

        def Send():
            global message_sent, time_sent, chat_feed, user_input, token, print_cash

            print_cash = root.chat_input.get()
            root.chat_input.delete(0, "end")
            if print_cash != '':
                if encoder_state:
                    user_input += prim_encode(f'{print_cash}')
                else:
                    user_input += f'{print_cash}'
                print_cash = ''

        root.send_button.configure(command=Send)

        def sync():
            global message_sent, time_sent, chat_feed, user_input, token, print_cash, lvl1codes

            if user_input != '':
                net.send(user_input)  # withheld messages are sent
                user_input = ''  # user's own message cash wiped

            if net.chat_feed != '':
                token = net.chat_feed[-3:]  # token recovered from the message delivery
                if token == '000':
                    write_to_his(net.chat_feed[:-3])
                    self.sync_stop = True
                    token = ''
                    net.chat_feed = ''
                if token == '666':
                    write_to_his(net.chat_feed[:-3])
                    token = ''
                    net.chat_feed = ''
                else:
                    net.send(token)  # token sent back as a validation of receipt
                    token = ''  # token wiped
                    write_to_his(net.chat_feed[:-3])  # message stripped off its token and added to user's chat history/displayed
                    net.chat_feed = ''  # initial message wiped

            net.read()  # requesting to read the message feed, socket is locked unless the message exists to stop listening

            HistoryUpdate()
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