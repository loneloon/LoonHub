# Цветовая схема
# dark bg = 041B15
# bright bg = 136F63
# pale fg = 22AAA1
# bright fg = 4CE0D2
# orange = ECA400
# buttons bg = E09100
# button text = 002E35

# BANNED COLOR = CD0074

import tkinter as tk
import os
import string
import time
import daily_timer
import cashgate as cage
import sys


recent_position = "+550+250"

# Блок инициализации основного скрипта

cash = cage.Entry()

first_log_at = cash.first_log_at
first_log_today = cash.first_log_today
last_log = cash.last_log
cur_date = cash.cur_date
balance = cash.balance
saved = cash.saved
allowance = cash.allowed_expense
lft4td = cash.left4td
leftovers = cash.leftovers


class Intro:
    def __init__(self, orient, alternative_message=None, alt_size=None, clue=None):
        global first_log_at, first_log_today, last_log, cur_date, balance, saved, allowance, lft4td, leftovers

        root = tk.Tk()

        root.main_lbl = tk.PhotoImage(file='img/welcome_screen_35.png')

        root.label = tk.Label(root, image=root.main_lbl, bg='#CD0074')
        root.label.place(x=0, y=0, relwidth=1, relheight=1)
        root.overrideredirect(True)
        root.geometry(orient)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", "#CD0074")
        root.label.pack()

        self.alternative_font_size = 10

        if alt_size is not None:
            self.alternative_font_size = alt_size

        message_var = tk.StringVar()

        if alternative_message is not None:
            message_var.set(alternative_message)
        else:
            message_var.set("Seems like you're new to CashGate!\r"
                            "It will help you organize your balance,\r"
                            "control your spending and savings.\n\r"
                            "Please consider reading help notes to \rlearn about its functions or dismiss\r if you used it previously.\n\n"
                            ""
                            "Official Cash Gate app. does not store,\r share or record your personal information.\r"
                            "It is merely a calculator that can remember\r variables and spread your active\r funds over a designated time period\r"
                            "Please be aware and use the official version\r in order to evade potential fraud under the veil\r of a seemingly alike third-party distributive.")

        root.message_lbl = tk.Label(root, textvariable=message_var, bg='#000000', font=('Arial', self.alternative_font_size, 'bold'),
                                    fg='#ECA400', relief='flat', justify='center')
        root.message_lbl.place(x=64, y=260)

        def Start():
            recent_position = root.geometry()[7:]
            root.destroy()
            Main(recent_position)

        def toHelp():
            recent_position = root.geometry()[7:]
            root.destroy()
            Main(recent_position, 'help start')

        def toLeft():
            recent_position = root.geometry()[7:]
            root.destroy()
            Main(recent_position, 'leftover start')


        # Кнопка Start

        root.start_but_pic = tk.PhotoImage(file='img/start_welcome_screen_35.png')
        root.start_but_lbl = tk.Button(root, image=root.start_but_pic, bg='#000000', relief='flat', command=Start)
        root.start_but_lbl.place(x=223, y=680)

        if clue == 'leftover start':
            root.start_but_lbl.configure(command=toLeft)

        # Кнопка Help

        root.help_but_pic = tk.PhotoImage(file='img/help_welcome_screen_35.png')
        root.help_but_lbl = tk.Button(root, image=root.help_but_pic, bg='#000000', relief='flat', command=toHelp)
        root.help_but_lbl.place(x=25, y=680)

        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='img/exit_orange_35.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#000000', relief='flat', command=Exit)
        root.exit.place(x=404, y=3)
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

        root.mainloop()


class Main:
    def __init__(self, orient, clue=None):
        global first_log_at, first_log_today, last_log, cur_date, balance, saved, allowance, lft4td, leftovers

        root = tk.Tk()

        root.main_lbl = tk.PhotoImage(file='img/cashgate_35.png')

        root.label = tk.Label(root, image=root.main_lbl, bg='#CD0074')
        root.label.place(x=0, y=0, relwidth=1, relheight=1)
        root.overrideredirect(True)
        root.geometry(orient)
        root.lift()
        root.wm_attributes("-topmost", True)
        root.wm_attributes("-transparentcolor", "#CD0074")
        root.label.pack()


        # Leftover box creation & buttons

        root.leftover_box_pic = tk.PhotoImage(file='img/cash_left_35.png')
        root.leftover_box = tk.Label(root, image=root.leftover_box_pic, bg='#041B15', relief='flat')

        leftover_show_string = tk.StringVar()

        root.leftover_box_path = tk.Label(root, textvariable=leftover_show_string, bg='#000000', fg='white', relief='flat', font=('Arial', 37, 'bold'),
                                          justify='center')

        root.left_to_balance_button_pic = tk.PhotoImage(file='img/TO_BALANCE_AND_RECOUNT_35.png')
        root.left_to_saved_button_pic = tk.PhotoImage(file='img/ADD_TO_SAVED_35.png')
        root.left_to_spend_button_pic = tk.PhotoImage(file='img/SPEND_IT_TODAY_35.png')

        root.left_to_balance_button_lbl = tk.Button(root, image=root.left_to_balance_button_pic, bg='#041B15', relief='flat')
        root.left_to_saved_button_lbl = tk.Button(root, image=root.left_to_saved_button_pic, bg='#041B15', relief='flat')
        root.left_to_spend_button_lbl = tk.Button(root, image=root.left_to_spend_button_pic, bg='#041B15', relief='flat')

        def leftover_buttons_show():
            root.left_to_balance_button_lbl.place(x=30, y=555, width=378, height=56)
            root.left_to_saved_button_lbl.place(x=30, y=625, width=378, height=56)
            root.left_to_spend_button_lbl.place(x=30, y=695, width=378, height=56)

        def leftover_buttons_hide():
            root.left_to_balance_button_lbl.place_forget()
            root.left_to_saved_button_lbl.place_forget()
            root.left_to_spend_button_lbl.place_forget()


        # Amount box creation

        root.m_box_pic = tk.PhotoImage(file='img/AMOUNT_35.png')
        root.m_box_amount = tk.Label(root, image=root.m_box_pic, bg='#041B15', relief='flat')

        root.m_box_amount_path = tk.Entry(root, bg='#000000', fg='white', relief='flat', font=('Arial', 37, 'bold'),
                                          justify='center')

        history_on = False
        display_on = False

        # Подпись к секции баланса

        root.yourbalance_pic = tk.PhotoImage(file='img/banner_lower_35.png')
        root.yourbalance_lbl = tk.Label(root, image=root.yourbalance_pic, background='#FB9300', foreground='#002E35',
                                        font=('Arial', 11, 'bold'), relief='flat', bd=0)
        root.yourbalance_lbl.configure(text=f'your balance  ', compound='center', justify='left')
        root.yourbalance_lbl.place(x=2, y=218, width=154, height=27)

        #balance_today = tk.DoubleVar()
        #balance_today.set(666.0)

        # Часы

        def timer():
            clock = daily_timer.Timer().nextday_in()
            root.yourbalance_lbl.configure(text=f'Renewal in {clock}  ')
            root.yourbalance_lbl.after(1000, timer)

        # Секция с суммой на балансе

        root.balance_num_pic = tk.PhotoImage(file='img/banner_mid_35.png')
        root.balance_num_lbl = tk.Label(root, image=root.balance_num_pic, background='#FB9300', foreground='#002E35',
                                        font=('Arial', 35), relief='flat', bd=0)
        root.balance_num_lbl.configure(text=lft4td, compound='center')
        root.balance_num_lbl.place(x=108, y=125, width=222, height=93)

        # Кнопка Exit

        def Exit():
            root.destroy()

        root.exit_lbl = tk.PhotoImage(file='img/exit_orange_35.png')
        root.exit = tk.Button(image=root.exit_lbl, bg='#000000', relief='flat', command=Exit)
        root.exit.configure(activebackground='#000000')
        root.exit.place(x=404, y=3)

        def History():
            root.history_block_pic = tk.PhotoImage(file='img/body_mid_text_35.png')
            root.history_label = tk.Label(root, image=root.history_block_pic, justify='left', bg='#041B15',
                                          fg='#4CE0D2', relief='flat', compound='center', font=('Arial', 18, 'bold'))

        History()

        def HistoryShow():
            DisplayHide()

            root.history_label.place(x=29, y=276, width=379, height=180)
            history_on = True

        def HistoryHide():
            root.history_label.place_forget()
            history_on = False

        # Дисплей в теле

        def Display():
            root.body_top_left_pic = tk.PhotoImage(file='img/body_mid_text_top_left_35.png')
            root.body_top_right_pic = tk.PhotoImage(file='img/body_mid_text_top_right_35.png')
            root.body_mid_left_pic = tk.PhotoImage(file='img/body_mid_text_mid_left_35.png')
            root.body_mid_right_pic = tk.PhotoImage(file='img/body_mid_text_mid_right_35.png')
            root.body_bot_left_pic = tk.PhotoImage(file='img/body_mid_text_bot_left_35.png')
            root.body_bot_right_pic = tk.PhotoImage(file='img/body_mid_text_bot_right_35.png')

            balance_bod_var = tk.DoubleVar()
            saved_bod_var = tk.DoubleVar()
            dailymax_bod_var = tk.DoubleVar()

            balance_bod_var.set(balance)
            saved_bod_var.set(saved)
            dailymax_bod_var.set(allowance)

            root.body_top_left_lbl = tk.Label(root, image=root.body_top_left_pic, text='Balance:          ',
                                              justify='left', bg='#041B15', fg='#4CE0D2', relief='flat',
                                              compound='center', font=('Arial', 18, 'bold'))

            root.body_top_right_lbl = tk.Label(root, image=root.body_top_right_pic, textvariable=balance_bod_var,
                                               bg='#041B15', fg='#4CE0D2', relief='flat', compound='center',
                                               justify='left', font=('Arial', 18, 'bold'))

            root.body_mid_left_lbl = tk.Label(root, image=root.body_mid_left_pic, text='Saved:             ',
                                              justify='left', bg='#041B15', fg='#4CE0D2', relief='flat',
                                              compound='center', font=('Arial', 18, 'bold'))

            root.body_mid_right_lbl = tk.Label(root, image=root.body_mid_right_pic, textvariable=saved_bod_var,
                                               justify='left', bg='#041B15', fg='#4CE0D2', relief='flat',
                                               compound='center', font=('Arial', 18, 'bold'))

            root.body_bot_left_lbl = tk.Label(root, image=root.body_bot_left_pic, text='Daily Max:       ',
                                              justify='left', bg='#041B15', fg='#4CE0D2', relief='flat',
                                              compound='center', font=('Arial', 18, 'bold'))

            root.body_bot_right_lbl = tk.Label(root, image=root.body_bot_right_pic, textvariable=dailymax_bod_var,
                                               justify='left', bg='#041B15', fg='#4CE0D2', relief='flat',
                                               compound='center', font=('Arial', 18, 'bold'))

        Display()

        def DisplayShow():
            HistoryHide()

            root.body_top_left_lbl.place(x=2, y=278, width=222, height=53)
            root.body_top_right_lbl.place(x=223, y=278, width=214, height=52)
            root.body_mid_left_lbl.place(x=2, y=330, width=222, height=53)
            root.body_mid_right_lbl.place(x=223, y=330, width=214, height=53)
            root.body_bot_left_lbl.place(x=2, y=383, width=222, height=55)
            root.body_bot_right_lbl.place(x=223, y=383, width=214, height=55)

            display_on = True

        DisplayShow()

        def DisplayHide():
            root.body_top_left_lbl.place_forget()
            root.body_top_right_lbl.place_forget()
            root.body_mid_left_lbl.place_forget()
            root.body_mid_right_lbl.place_forget()
            root.body_bot_left_lbl.place_forget()
            root.body_bot_right_lbl.place_forget()

            display_on = False

        def toHelp():
            Help()

        # Mini nav.

        root.history_switch_lbl = tk.Button(root, text='history', bg='#22AAA1', fg='#041B15', font=('Arial', 8),
                                            justify='center', relief='flat', command=HistoryShow)
        root.history_switch_lbl.place(x=20, y=257, width=49, height=12)

        root.display_switch_lbl = tk.Button(root, text='display', bg='#22AAA1', fg='#041B15', font=('Arial', 8),
                                            justify='center', relief='flat', command=DisplayShow)
        root.display_switch_lbl.place(x=80, y=257, width=49, height=12)

        root.help_switch_lbl = tk.Button(root, text='help', bg='#22AAA1', fg='#041B15', font=('Arial', 8),
                                         justify='center', relief='flat', command=toHelp)
        root.help_switch_lbl.place(x=140, y=257, width=49, height=12)

        # Кнопки Add, Cancel

        root.add_button_pic = tk.PhotoImage(file='img/ADD_35.png')
        root.add_button_lbl = tk.Button(root, image=root.add_button_pic, bg='#041B15', relief='flat', command=None)

        root.cancel_button_pic = tk.PhotoImage(file='img/CANCEL_35.png')
        root.cancel_button_lbl = tk.Button(root, image=root.cancel_button_pic, bg='#041B15', relief='flat',
                                           command=None)

        class menuButtons:

            def __init__(self):
                root.deposit_button_pic = tk.PhotoImage(file='img/DEPOSIT_35.png')
                root.deposit_button_lbl = tk.Button(root, image=root.deposit_button_pic, bg='#041B15', relief='flat')

                root.recount_button_pic = tk.PhotoImage(file='img/RECOUNT_35.png')
                root.recount_button_lbl = tk.Button(root, image=root.recount_button_pic, bg='#041B15', relief='flat')

                root.spend_small_button_pic = tk.PhotoImage(file='img/SPEND_35.png')
                root.spend_small_button_lbl = tk.Button(root, image=root.spend_small_button_pic, bg='#041B15',
                                                        relief='flat')

                root.spend_big_button_pic = tk.PhotoImage(file='img/SPEND_big_35.png')
                root.spend_big_button_lbl = tk.Button(root, image=root.spend_big_button_pic, bg='#041B15',
                                                      relief='flat',
                                                      command=None)

                menu_buttons_show()

        def menu_buttons_hide():
            root.deposit_button_lbl.place_forget()
            root.recount_button_lbl.place_forget()
            root.spend_small_button_lbl.place_forget()

        def menu_buttons_show():
            root.deposit_button_lbl.place(x=27, y=470)
            root.recount_button_lbl.place(x=27, y=570)
            root.spend_small_button_lbl.place(x=27, y=670)

        def menu_buttons_disable():
            root.deposit_button_lbl.configure(state='disabled')
            root.recount_button_lbl.configure(state='disabled')
            root.spend_small_button_lbl.configure(state='disabled')

        def menu_buttons_enable():
            root.deposit_button_lbl.configure(state='normal')
            root.recount_button_lbl.configure(state='normal')
            root.spend_small_button_lbl.configure(state='normal')

        menuButtons()

        def mini_nav_disable():
            root.history_switch_lbl.configure(state='disabled')
            root.display_switch_lbl.configure(state='disabled')
            root.help_switch_lbl.configure(state='disabled')

        def mini_nav_enable():
            root.history_switch_lbl.configure(state='normal')
            root.display_switch_lbl.configure(state='normal')
            root.help_switch_lbl.configure(state='normal')

        # Warning Message

        root.warning_pic = tk.PhotoImage(file='img/warning_35.png')
        root.warning_lbl = tk.Label(root, image=root.warning_pic, bg='#041B15', relief='flat')
        root.warning_text = tk.Label(root, bg='#000000', fg='white')

        def warning_box(message: string, pos: list):
            warning_contents = tk.StringVar()
            warning_contents.set(message)

            root.warning_text.configure(textvariable=warning_contents, compound='center', font=('Arial', 19, 'bold'))

            root.warning_lbl.place(x=14, y=330)
            root.warning_text.place(x=pos[0], y=pos[1])

        def hide_warning():
            root.warning_lbl.place_forget()
            root.warning_text.place_forget()
            menu_buttons_enable()
            mini_nav_enable()

        def recount_warn():
            mini_nav_disable()
            warning_box("Please RECOUNT before\n spending funds!", [70, 425])
            menu_buttons_disable()
            root.warning_lbl.after(3000, hide_warning)

        root.recount_button_lbl.configure(command=recount_warn)  # Binding warning command

        class BalanceAddBox:

            def __init__(self):
                menu_buttons_hide()

                mini_nav_disable()

                DisplayHide()
                HistoryHide()

                root.m_box_amount.place(x=14, y=330, width=411, height=137)

                root.m_box_amount_path.place(x=26, y=380, width=387, height=76)

                root.add_button_lbl.place(x=27, y=570)
                root.cancel_button_lbl.place(x=27, y=670)

                def MExit():
                    root.m_box_amount.place_forget()
                    root.m_box_amount_path.place_forget()

                    root.add_button_lbl.place_forget()
                    root.cancel_button_lbl.place_forget()

                    menu_buttons_show()

                    mini_nav_enable()

                    DisplayShow()

                root.cancel_button_lbl.configure(command=MExit)

        class SpendBox:

            def __init__(self):
                DisplayHide()
                HistoryHide()

                menu_buttons_hide()

                mini_nav_disable()

                root.m_box_amount.place(x=14, y=330, width=411, height=137)

                root.m_box_amount_path.place(x=26, y=380, width=387, height=76)

                root.spend_big_button_lbl.place(x=27, y=570)
                root.cancel_button_lbl.place(x=27, y=670)

                def MExit():
                    root.m_box_amount.place_forget()
                    root.m_box_amount_path.place_forget()

                    root.spend_big_button_lbl.place_forget()
                    root.cancel_button_lbl.place_forget()

                    menu_buttons_show()

                    mini_nav_enable()

                    DisplayShow()

                root.cancel_button_lbl.configure(command=MExit)

        # Init Button commands

        root.spend_small_button_lbl.configure(command=SpendBox)
        root.deposit_button_lbl.configure(command=BalanceAddBox)

        # Окно помощи

        class Help:
            def __init__(self):
                root.help_screen_pic = tk.PhotoImage(file='img/help_screen_35.png')

                root.help_screen_lbl = tk.Label(root, image=root.help_screen_pic, bg='#CD0074')
                root.help_screen_lbl.place(x=0, y=0, relwidth=1, relheight=1)

                message_var = tk.StringVar()
                message_var.set("Seems like you're new to CashGate!\r"
                                "It will help you organize your balance,\r"
                                "control your spending and savings.\n\r"
                                "Please consider reading help notes to \rlearn about its functions or dismiss\r if you used it previously.\n\n"
                                ""
                                "Official Cash Gate app. does not store,\r share or record your personal information.\r"
                                "It is merely a calculator that can remember\r variables and spread your active\r funds over a designated time period\r"
                                "Please be aware and use the official version\r in order to evade potential fraud under the veil\r of a seemingly alike third-party distributive.")

                root.message_lbl = tk.Label(root, textvariable=message_var, bg='#000000', font=('Arial', 10, 'bold'),
                                            fg='#ECA400', relief='flat', justify='center')
                root.message_lbl.place(x=64, y=260)

                def BacktoMain():
                    root.exit_overhelp.destroy()
                    root.help_screen_lbl.destroy()
                    root.message_lbl.destroy()
                    root.left_but_lbl.destroy()
                    root.right_but_lbl.destroy()
                    root.start_but_lbl.destroy()

                def PageLeft():
                    pass

                def PageRight():
                    pass

                # Left

                root.left_but_pic = tk.PhotoImage(file='img/left_help_35.png')
                root.left_but_lbl = tk.Button(root, image=root.left_but_pic, bg='#000000', relief='flat',
                                              command=PageLeft(),
                                              bd=0)
                root.left_but_lbl.place(x=20, y=682)

                # Right

                root.right_but_pic = tk.PhotoImage(file='img/right_help_35.png')
                root.right_but_lbl = tk.Button(root, image=root.right_but_pic, bg='#000000', relief='flat',
                                               command=PageRight(),
                                               bd=0)
                root.right_but_lbl.place(x=305, y=682)

                # Кнопка Start

                root.start_but_pic = tk.PhotoImage(file='img/start_welcome_screen_35.png')
                root.start_but_lbl = tk.Button(root, image=root.start_but_pic, bg='#000000', relief='flat',
                                               command=BacktoMain)
                root.start_but_lbl.place(x=120, y=680)

                # Дубликат оригинального exit, т.к. Help - оверлэй

                def Exit():
                    root.destroy()

                root.exit_lbl_overhelp = tk.PhotoImage(file='img/exit_orange_35.png')
                root.exit_overhelp = tk.Button(image=root.exit_lbl_overhelp, bg='#000000', relief='flat', command=Exit)
                root.exit_overhelp.configure(activebackground='#000000')
                root.exit_overhelp.place(x=404, y=3)


        class Leftovers:
            def __init__(self):
                menu_buttons_hide()

                mini_nav_disable()

                DisplayHide()
                HistoryHide()

                leftover_show_string.set(leftovers)

                root.leftover_box.place(x=14, y=280, width=411, height=249)
                root.leftover_box_path.place(x=26, y=360, width=387, height=76)

                leftover_buttons_show()

                def MExit():
                    root.leftover_box.place_forget()
                    root.leftover_box_path.place_forget()

                    leftover_buttons_hide()

                    #root.spend_big_button_lbl.place_forget()
                    #root.cancel_button_lbl.place_forget()

                    menu_buttons_show()

                    mini_nav_enable()

                    DisplayShow()

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

        # Активация окна
        if clue == 'help start':
            Help()
        elif clue == 'leftover start':
            Leftovers()

        root.after_idle(timer)
        root.mainloop()


# First login check

if not first_log_at:
    Intro(recent_position, 'u idit lol, ur mani stolen', 20, 'leftover start')
else:
    Intro(recent_position)