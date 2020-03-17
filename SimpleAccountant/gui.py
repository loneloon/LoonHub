# Цветовая схема:
#  blue bg = #306082
#  dark text = #131119
#  white fg = #fafbf6
#  red selection = #c82e2e


import tkinter as tk
import os
import string
import userlog as ul

# Блок основы

recent_position = "+550+250"


class Main:
    def __init__(self, orient):
        root = tk.Tk()

        root.main_lbl = tk.PhotoImage(file='main.png')
        root.main_wrong = tk.PhotoImage(file='mad.png')
        root.main_happy = tk.PhotoImage(file='happy2.png')
        root.main_reg = tk.PhotoImage(file='reading.png')
        root.m_box = tk.PhotoImage(file='m_box.png')

        root.label = tk.Label(root, image=root.main_lbl, bg='white')
        root.label.place(x=0, y=0, relwidth=1, relheight=1)
        root.overrideredirect(True)
        root.geometry(orient)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", "white")
        root.label.pack()

        # Тайтл на полоске

        root.main_title = tk.Label(root, text='Splinter Auth.', background='#c82e2e', foreground='#fafbf6',
                                   font=('Arial', 40, 'bold'), relief='flat')
        root.main_title.place(x=150, y=105)

        # Логин & Пароль

        root.login_label = tk.Label(root, text='Username:', background='#fafbf6', foreground='#131119',
                                    font=('Arial', 19, 'bold'),
                                    relief='flat')
        root.login_label.place(x=99, y=218)

        root.login_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                  selectforeground='#f1f3e7',
                                  font=('Arial', 19), relief='flat')
        root.login_ent.place(x=238, y=221, width=230, height=30)



        root.pass_label = tk.Label(root, text='Password:', background='#fafbf6', foreground='#131119',
                                   font=('Arial', 19, 'bold'),
                                   relief='flat')
        root.pass_label.place(x=100, y=255)

        root.pass_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                 selectforeground='#f1f3e7',
                                 font=('Arial', 19), relief='flat', show='*')
        root.pass_ent.place(x=238, y=258, width=230, height=30)


        # Кнопки Login/Register

        def SignIn():
            ul.SignIn(root.login_ent.get(), root.pass_ent.get())


        root.signin_label = tk.PhotoImage(file='login.png')
        root.signin_bt = tk.Button(image=root.signin_label, bg='#fafbf6', relief='flat', command=SignIn)
        root.signin_bt.place(x=120, y=330)

        def SwitchToReg():
            recent_position = root.geometry()[7:]
            root.destroy()
            Reg(recent_position)

        root.register_label = tk.PhotoImage(file='register.png')
        root.register_bt = tk.Button(image=root.register_label, bg='#fafbf6', relief='flat', command=SwitchToReg)
        root.register_bt.place(x=300, y=330)

        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='exit.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#fafbf6', relief='flat', command=Exit)
        root.exit.place(x=580, y=78)
        root.exit.configure(activebackground='#fafbf6', height=18, width=18)

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

        root.label.bind("<ButtonPress-1>", StartMove)
        root.label.bind("<ButtonRelease-1>", StopMove)
        root.label.bind("<B1-Motion>", OnMotion)

        # Активация окна

        root.mainloop()


class Reg:
    def __init__(self, orient):
        root = tk.Tk()

        root.main_lbl = tk.PhotoImage(file='main.png')
        root.main_wrong = tk.PhotoImage(file='mad.png')
        root.main_happy = tk.PhotoImage(file='happy2.png')
        root.main_reg = tk.PhotoImage(file='reading.png')
        root.m_box = tk.PhotoImage(file='m_box.png')

        root.label = tk.Label(root, image=root.main_reg, bg='white')
        root.label.place(x=0, y=0, relwidth=1, relheight=1)
        root.overrideredirect(True)
        root.geometry(orient)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", "white")
        root.label.pack()



        # Рег. форма


        # Логин
        root.login_label = tk.Label(root, text='Username:', background='#fafbf6', foreground='#131119',
                                    font=('Arial', 19, 'bold'),
                                    relief='flat')
        root.login_label.place(x=79, y=85)

        root.login_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                  selectforeground='#f1f3e7',
                                  font=('Arial', 19), relief='flat')
        root.login_ent.place(x=228, y=88, width=230, height=30)

        # Пароль
        root.pass_label = tk.Label(root, text='Password:', background='#fafbf6', foreground='#131119',
                                   font=('Arial', 19, 'bold'),
                                   relief='flat')
        root.pass_label.place(x=80, y=125)

        root.pass_reg_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                 selectforeground='#f1f3e7',
                                 font=('Arial', 19), relief='flat')
        root.pass_reg_ent.place(x=228, y=128, width=230, height=30)

        # Имя
        root.fn_label = tk.Label(root, text='First Name:', background='#fafbf6', foreground='#131119',
                                   font=('Arial', 19, 'bold'),
                                   relief='flat')
        root.fn_label.place(x=80, y=165)

        root.fn_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                 selectforeground='#f1f3e7',
                                 font=('Arial', 19), relief='flat')
        root.fn_ent.place(x=228, y=168, width=230, height=30)

        # Фамилия
        root.ln_label = tk.Label(root, text='Last Name:', background='#fafbf6', foreground='#131119',
                                 font=('Arial', 19, 'bold'),
                                 relief='flat')
        root.ln_label.place(x=80, y=205)

        root.ln_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                               selectforeground='#f1f3e7',
                               font=('Arial', 19), relief='flat')
        root.ln_ent.place(x=228, y=208, width=230, height=30)

        # DOB
        root.dob_label = tk.Label(root, text='D.o.B:', background='#fafbf6', foreground='#131119',
                                 font=('Arial', 19, 'bold'),
                                 relief='flat')
        root.dob_label.place(x=80, y=245)

        root.dob_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                               selectforeground='#f1f3e7',
                               font=('Arial', 19), relief='flat')
        root.dob_ent.place(x=228, y=248, width=230, height=30)

        # Email
        root.email_label = tk.Label(root, text='E-mail:', background='#fafbf6', foreground='#131119',
                                  font=('Arial', 19, 'bold'),
                                  relief='flat')
        root.email_label.place(x=80, y=285)

        root.email_ent = tk.Entry(root, fg='#fafbf6', background='#306082', selectbackground='#140226',
                                selectforeground='#f1f3e7',
                                font=('Arial', 19), relief='flat')
        root.email_ent.place(x=228, y=288, width=230, height=30)


        def SwitchToMain():
            recent_position = root.geometry()[7:]
            root.destroy()
            Main(recent_position)


        class MessageBox:
            def __init__(self):
                root.m_box_label = tk.Label(root, image=root.m_box, bg='white')
                root.m_box_label.place(x=-20, y=410)
                root.m_box_label.lift()

                root.pass_message = tk.Label(root, text=f'{ul.pass_check(root.pass_reg_ent.get())}',
                                             background='#fafbf6',
                                             foreground='#140226', font=('Comic Sans MS', 18), wraplength=400)
                root.pass_message.configure(width=40)
                root.pass_message.place(x=80, y=490, width=400)

            def del_message(anykey):
                root.pass_message.destroy()
                root.m_box_label.destroy()


        def Register():
            if ul.pass_check(root.pass_reg_ent.get()):
                MessageBox()

                root.bind("<Key>", MessageBox.del_message)
            else:
                MessageBox()

                root.bind("<Key>", MessageBox.del_message)


        root.back_label = tk.PhotoImage(file='back.png')
        root.back_bt = tk.Button(image=root.back_label, bg='#fafbf6', relief='flat', command=SwitchToMain)
        root.back_bt.place(x=120, y=330)

        root.register_label = tk.PhotoImage(file='register.png')
        root.register_bt = tk.Button(image=root.register_label, bg='#fafbf6', relief='flat', command=Register)
        root.register_bt.place(x=300, y=330)


        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='exit.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#fafbf6', relief='flat', command=Exit)
        root.exit.place(x=580, y=78)
        root.exit.configure(activebackground='#fafbf6', height=18, width=18)

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

        root.label.bind("<ButtonPress-1>", StartMove)
        root.label.bind("<ButtonRelease-1>", StopMove)
        root.label.bind("<B1-Motion>", OnMotion)

        # Активация окна

        root.mainloop()


Main(recent_position)
