import telebot

import json
from threading import Timer, Thread
from calculator import Sol
import time, os

till_restart = 60

token = '1311710716:AAEl7NThhcj--CNKRRtsHPQwKsRWem7x_3M'

bot = telebot.TeleBot(token=token, threaded=False)

sol_calculus = Sol()


def time_out():
    global till_restart
    bot.stop_polling()
    time.sleep(3)


def res():
    try:
        BotBase()

    except:

        BotBase()


class BotBase:
    global bot

    def __init__(self):
        self.greeting = f"Welcome to Sol12 Project.\n\n" \
                        f"I will help you monitor your activity during the day and provide stats after. " \
                        f"I will help you improve your day-to-day performance as a human."

        self.help = f"Commands:\n/activities - Switch current activity (default=sleep)" \
                    f"\n/task - Display current activity\n/summary - Summarize the day so far" \
                    f"\n/graph - Generate visual graph"


        self.inl_2 = telebot.types.InlineKeyboardMarkup()
        self.inl_2.row(telebot.types.InlineKeyboardButton('Eat', callback_data='1'),
                       telebot.types.InlineKeyboardButton('Hygiene', callback_data='2'))

        self.inl_2.row(telebot.types.InlineKeyboardButton('Exercise', callback_data='3'),
                       telebot.types.InlineKeyboardButton('Work', callback_data='4'))

        self.inl_2.row(telebot.types.InlineKeyboardButton('Study', callback_data='5'),
                       telebot.types.InlineKeyboardButton('Creative', callback_data='6'))

        self.inl_2.row(telebot.types.InlineKeyboardButton('Shopping', callback_data='7'),
                       telebot.types.InlineKeyboardButton('Leisure', callback_data='8'))

        self.inl_2.row(telebot.types.InlineKeyboardButton('Cleaning', callback_data='9'),
                       telebot.types.InlineKeyboardButton('Sleep', callback_data='0'))

        @bot.message_handler(commands=['start'])
        def start_message(message):
            bot.send_message(message.chat.id, self.greeting+"\n\n"+self.help)
            bot.delete_message(chat_id=message.chat.id,
                                  message_id=message.message_id)

        @bot.message_handler(commands=['help'])
        def help_message(message):
            bot.send_message(message.chat.id, self.help)
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)

        @bot.message_handler(commands=['activities'])
        def list_all(message):
            bot.send_message(message.chat.id, "Choose your next activity!", reply_markup=self.inl_2)
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            if call.message:
                bot.send_message(call.message.chat.id, sol_calculus.punch_in(int(call.data), call.message.chat.id),
                                 reply_markup=telebot.types.ReplyKeyboardRemove())
                edit_message_callback(call)

        def edit_message_callback(call):
            bot.delete_message(chat_id=call.message.chat.id,
                               message_id=call.message.message_id)

        @bot.message_handler(commands=['summary'])
        def send_summary(message):
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)
            bot.send_message(message.chat.id, 'Sending your stats:\n')

            temp_mess = "\n"

            for act, time_percent in sol_calculus.count_stats(message.chat.id).items():
                temp_mess += f"{act}: ~{round(time_percent, 1)}%\n"

            bot.send_message(message.chat.id, temp_mess)

        @bot.message_handler(commands=['graph'])
        def show_plot(message):
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)
            bot.send_message(message.chat.id, 'generating summary')
            print(f'Plot requested. Generating graph for {message.chat.id}...')
            sol_calculus.generate_graph(message.chat.id)

            bot.send_photo(message.chat.id,
                           photo=open(f"{message.chat.id}_report.png", 'rb'),
                           caption=f"Here's your performance today.")
            os.remove(f"{message.chat.id}_report.png")

        @bot.message_handler(commands=['task'])
        def view_cur_task(message):
            bot.delete_message(chat_id=message.chat.id,
                               message_id=message.message_id)
            bot.send_message(message.chat.id, f'Activity in progress: {sol_calculus.view_task(message.chat.id)}')

        bot.polling()


while True:
    t = Timer(till_restart, time_out)
    t.start()
    res()
