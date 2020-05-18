from encode import PalmTrees
import tkinter as tk


recent_pos = "+450+250"

class Main:
    def __init__(self, recent_pos):

        self.root = tk.Tk()
        self.root.wall_lbl = tk.PhotoImage(file='gui/nokey.png')
        self.root.wall_lbl2 = tk.PhotoImage(file='gui/wkey.png')
        self.root.label = tk.Label(self.root, image=self.root.wall_lbl, bg='green')
        self.root.label.place(x=0, y=0, relwidth=1, relheight=1)
        self.root.overrideredirect(True)
        self.root.geometry(recent_pos)
        self.root.lift()
        self.root.wm_attributes("-topmost", False)
        self.root.wm_attributes("-transparentcolor", "green")
        self.root.label.pack()

        trans_butt_pic = tk.PhotoImage(file="gui/trans.png")
        trans_butt = tk.Button(self.root, image=trans_butt_pic, width=240, height=70, bg="#8338ec", relief='flat', activebackground="#8338ec", command=self.translate)
        trans_butt.place(x=33, y=392)

        enc_butt_pic = tk.PhotoImage(file="gui/enc.png")
        enc_butt = tk.Button(self.root, image=enc_butt_pic, width=240, height=70, bg="#8338ec", relief='flat', activebackground="#8338ec", command=self.encode)
        enc_butt.place(x=307, y=392)

        feed_butt_pic = tk.PhotoImage(file="gui/feed.png")
        feed_butt = tk.Button(self.root, image=feed_butt_pic, width=240, height=70, bg="#8338ec", relief='flat', activebackground="#8338ec", command=self.feed)
        feed_butt.place(x=588, y=392)


        def Exit():
            self.root.destroy()

        self.root.exit_lbl = tk.PhotoImage(file='gui/exit.png')
        self.root.exit = tk.Button(image=self.root.exit_lbl, bg='#8338ec', relief='flat', command=Exit)
        self.root.exit.place(x=830, y=105)
        self.root.exit.configure(disabledforeground='#8338ec', activebackground='#8338ec', width=45, height=45)


        def get_input(event):
            message = self.root.textwin.get("1.0", 'end-1c')

        self.root.textwin = tk.Text(self.root, bg='#3f3f74', fg='#ffbe0b', font=('Arial', 20), relief='flat')
        self.root.textwin.place(x=40, y=130, width=505, height=225)

        self.root.textwin.bind('<Escape>', get_input)


        def StartMove(event):
            self.root.x = event.x
            self.root.y = event.y

        def StopMove(event):
            self.root.x = None
            self.root.y = None

        def OnMotion(event):
            deltax = event.x - self.root.x
            deltay = event.y - self.root.y
            x = self.root.winfo_x() + deltax
            y = self.root.winfo_y() + deltay
            self.root.geometry("+%s+%s" % (x, y))

        self.root.label.bind("<ButtonPress-1>", StartMove)
        self.root.label.bind("<ButtonRelease-1>", StopMove)
        self.root.label.bind("<B1-Motion>", OnMotion)


        self.root.mainloop()

    def feed(self):
        self.kirbs = KirbyEnc()
        self.encode = PalmTrees(self.kirbs.ni, self.kirbs.san, self.kirbs.yon)
        self.root.label.configure(image=self.root.wall_lbl2)
        self.root.label.update()

    def encode(self):
        self.message = self.root.textwin.get("1.0", 'end-1c')
        self.encode.translate(self.message)
        self.root.textwin.delete("1.0", 'end-1c')

    def translate(self):
        import decode
        self.decoder = decode.PalmLeaves()
        translated = self.decoder.get_translation()
        self.root.textwin.delete("1.0", 'end-1c')
        self.root.textwin.insert("1.0", translated)

class KirbyEnc:
    def __init__(self):
        import scramble


        self.ich = scramble.kirby.prim_range

        self.ni = int(self.ich[0:4])
        if self.ni < 1000:
            self.ni += 1000

        self.san = int(self.ich[4:9])
        if self.san < 1000:
            self.san += 1000

        if self.san < self.ni:
            self.ni, self.san = self.san, self.ni

        self.yon = scramble.kirby.sec_code




test = Main(recent_pos)