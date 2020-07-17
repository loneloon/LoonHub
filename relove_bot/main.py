import telebot
import quiz
import json
from threading import Timer
import time

till_restart = 60

token='1271548938:AAGIVXqquLWCAcwyolSwNr5RDcIYvMmQrc4'

bot = telebot.TeleBot(token=token, threaded=False)

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



        # self.activated = False

        self.admin = 'Korobkovochka'
        self.greeting = '''
        Привет!

Сейчас ты на одном из основополагающих этапов курса – выбор куратора.
Это человек, который не просто будет на связи с тобой 21 день, а будет тебя направлять и поддерживать во всех твоих осознаниях.

Ответь на несколько вопросов, которые приведут тебя к твоему будущему куратору, с которым работа на курсе будет проходить наиболее комфортно и эффективно.


Нажми /quiz, чтобы начать!

Если возникнут трудности, нажми /help.
        '''

        self.help = f'''
        Без паники!
Давай возьмем ситуацию в свои руки.

Я откликаюсь на следующие команды:
/start - приветствие
/quiz - пройти тест
/help - помощь

Если твой тест остановился или ты не получил ответа, повторный /quiz - сделает рестарт.

Если у тебя возникли вопросы, на которые я не могу ответить:
наш администратор @{self.admin} с радостью на них ответит!
        '''

        self.q = quiz.Quiz()

        with open('json/spy.json', 'r', encoding='utf-8') as sd:
            self.spy_data = json.load(sd)

        @bot.message_handler(commands=['start'])
        def start_message(message):

            bot.send_message(message.chat.id, self.greeting)

            print(message.chat.id)

            if message.from_user.username is not None:
                if message.from_user.username not in self.spy_data.keys():
                    self.spy_data[message.from_user.username] = ""

                    json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                              ensure_ascii=True)
            else:
                if f"tg://user?id={message.from_user.id}" not in self.spy_data.keys():
                    self.spy_data[f"tg://user?id={message.from_user.id}"] = ""

                    json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                              ensure_ascii=True)

        @bot.message_handler(commands=['help'])
        def send_help(message):
            bot.send_message(message.chat.id, self.help)

        @bot.callback_query_handler(func=lambda call: True)
        def callback_inline(call):
            print('Сработал хэндлер')

            print(call.data)

            if call.message:
                if call.data == self.q.all[call.message.chat.id]['coach1']:
                    self.q.all[call.message.chat.id]['coach'] = self.q.all[call.message.chat.id]['coach1']
                elif call.data == self.q.all[call.message.chat.id]['coach2']:
                    self.q.all[call.message.chat.id]['coach'] = self.q.all[call.message.chat.id]['coach2']

                self.q.ask_back(id=call.message.chat.id)
                edit_message_callback(call, self.q.all[call.message.chat.id]['coach'])

                bot.send_photo(call.message.chat.id,
                               photo=open(f'photos/{self.q.all[call.message.chat.id]["coach"]}.jpg', 'rb'),
                               caption=f"Спасибо за ваши ответы!\nВашим куратором будет {self.q.all[call.message.chat.id]['coach']}",
                               reply_markup=telebot.types.ReplyKeyboardRemove())

                # json dump

                with open('json/spy.json', 'r', encoding='utf-8') as sd:
                    self.spy_data = json.load(sd)

                if self.q.all[call.message.chat.id]['json'].from_user.username is not None:
                    self.spy_data[self.q.all[call.message.chat.id]['json'].from_user.username] = \
                    self.q.all[call.message.chat.id]['coach']
                    bot.send_message(chat_id=87829324,
                                     text=f"@{self.q.all[call.message.chat.id]['json'].from_user.username} распределен к куратору {self.q.all[call.message.chat.id]['coach']}!")
                else:
                    self.spy_data[f"tg://user?id={self.q.all[call.message.chat.id]['json'].from_user.id}"] = \
                    self.q.all[call.message.chat.id]['coach']
                    bot.send_message(chat_id=87829324,
                                     text=f"tg://user?id={self.q.all[call.message.chat.id]['json'].from_user.id} (без юзернэйма) распределен к куратору {self.q.all[call.message.chat.id]['coach']}!")

                print(self.spy_data)

                json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                          ensure_ascii=True)

                self.q.all[call.message.chat.id]['run'] = False

                del self.q.all[call.message.chat.id]
                print(self.q.table)

                with open('json/spy.json', 'r', encoding='utf-8') as sd:
                    self.spy_data = json.load(sd)

                bot.send_message(call.message.chat.id,
                                 f'Если у Вас остались какие-либо вопросы, наш администратор @{self.admin} с радостью на них ответит!')

        def edit_message_callback(call, sel):
            if call.message:
                bot.edit_message_text(
                    text=f'Выберите куратора:\n✅{sel}',
                    chat_id=call.message.chat.id,
                    message_id=call.message.message_id,
                    reply_markup=telebot.types.InlineKeyboardMarkup(),
                    parse_mode='HTML'
                )
            elif call.inline_message_id:
                bot.edit_message_text(
                    text=f'Выберите куратора:\n✅{sel}',
                    inline_message_id=call.inline_message_id,
                    reply_markup=telebot.types.InlineKeyboardMarkup(),
                    parse_mode='HTML'
                )

        @bot.message_handler(commands=['quiz'])
        def quiz_thread(message):

            with open('json/spy.json', 'r', encoding='utf-8') as sd:
                self.spy_data = json.load(sd)

            coach = ''

            try:
                if message.from_user.username is not None:
                    if self.spy_data[message.from_user.username] != "":
                        coach = self.spy_data[message.from_user.username]
                        self.tested = True
                    else:
                        self.tested = False
                else:
                    if self.spy_data[f"tg://user?id={message.from_user.id}"] != "":
                        coach = self.spy_data[f"tg://user?id={message.from_user.id}"]
                        self.tested = True
                    else:
                        self.tested = False
            except:
                self.tested = False

            if self.tested:
                bot.send_message(message.chat.id, f'Вы уже выбрали куратора! Ваш куратор: {coach}')
            else:

                self.q.all[message.chat.id] = {'level': 0, 'path': '', 'waiting': False, 'choice': None, 'answer': '',
                                               'run': False, 'coach': '', 'coach1': '', 'coach2': '', 'json': message}
                self.q.all[message.chat.id]['run'] = True

                self.kb_1()

                bot.send_message(message.chat.id, self.q.ask_back(id=message.chat.id), reply_markup=self.keyboard1)

        @bot.message_handler(content_types=['text'])
        def send_text(message):

            if ('stats' in message.text.lower()) and (
                    message.from_user.username.lower() in ['loneloon', 'kejloon', self.admin.lower()]):

                with open('json/spy.json', 'r', encoding='utf-8') as sd:
                    self.spy_data = json.load(sd)

                self.report = ''

                self.u_all = len(self.spy_data)
                self.u_tested = 0

                for k, v in self.spy_data.items():
                    if v != '':
                        self.u_tested += 1

                try:
                    self.report += f'Прошли тест:{self.u_tested}/{self.u_all}\n\n'
                except:
                    self.report += f'Прошли тест:{0}/{0}\n\n'

                for curator in self.q.table.keys():
                    self.report += f'{curator} {self.q.table[curator]}: \n'
                    for user, assig in self.spy_data.items():
                        if curator == assig:
                            self.report += f'@{user}\n'

                bot.send_message(message.chat.id, f'❗СТАТИСТИКА❗\n{self.report}')
            elif 'ты здесь?' in message.text.lower():
                bot.send_message(message.chat.id, f'На месте! ✌')
            else:

                try:
                    if self.q.all[message.chat.id]['run']:
                        if not self.q.all[message.chat.id]['waiting']:
                            reply = self.q.ask_back(id=message.chat.id)

                            if reply is None:
                                reply = self.q.ask_back(id=message.chat.id)

                                if type(reply) == list and reply[0] == 'list':
                                    reply = reply[1]

                                    self.kb_2()

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard2)
                                else:

                                    self.kb_1()

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                            else:

                                self.kb_1()

                                bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)

                        else:
                            reply = self.q.ask_back(id=message.chat.id, message=message.text)

                            if reply is None:
                                reply = self.q.ask_back(id=message.chat.id)

                                if type(reply) == list and reply[0] == 'list':
                                    reply = reply[1]

                                    self.kb_2()

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard2)

                                else:
                                    self.kb_1()

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                            else:
                                if type(reply) == list and type(reply[0]) == str:

                                    coach = reply[0]

                                    bot.send_photo(message.chat.id, photo=open(f'photos/{coach}.jpg', 'rb'),
                                                   caption=reply[1],
                                                   reply_markup=telebot.types.ReplyKeyboardRemove())

                                    # json dump

                                    with open('json/spy.json', 'r', encoding='utf-8') as sd:
                                        self.spy_data = json.load(sd)

                                    if message.from_user.username is not None:
                                        self.spy_data[message.from_user.username] = coach
                                        bot.send_message(chat_id=87829324,
                                                         text=f"@{message.from_user.username} распределен к куратору {coach}!")
                                    else:
                                        self.spy_data[f"tg://user?id={message.from_user.id}"] = coach
                                        bot.send_message(chat_id=87829324,
                                                         text=f"tg://user?id={message.from_user.id} (без юзернэйма) распределен к куратору {coach}!")

                                    print(self.spy_data)

                                    json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                                              ensure_ascii=True)

                                    self.q.all[message.chat.id]['run'] = False

                                    del self.q.all[message.chat.id]
                                    print(self.q.table)

                                    with open('json/spy.json', 'r', encoding='utf-8') as sd:
                                        self.spy_data = json.load(sd)

                                    bot.send_message(message.chat.id,
                                                     f'Если у Вас остались какие-либо вопросы, наш администратор @{self.admin} с радостью на них ответит!')
                                elif type(reply) == list and type(reply[0]) == list:

                                    coaches = reply[0]

                                    self.kb_2_inline(coaches)

                                    with open('json/info.json', 'r', encoding='utf-8') as cur_i:
                                        self.cur_info = json.load(cur_i)

                                    bot.send_message(chat_id=message.chat.id, text=(reply[
                                                                                        1] + f'\n\n{coaches[0]}:\n{self.cur_info[coaches[0]]}\n\n{coaches[1]}:\n{self.cur_info[coaches[1]]}'),
                                                     reply_markup=self.inl_2)

                                else:
                                    self.kb_1()

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                except:
                    pass

        # main loop

        bot.polling()

    def kb_1(self):
        self.keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

        self.keyboard1.row('Да', 'Нет')

    def kb_2(self):
        self.keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        print(self.q.keyboard2)

        for i in self.q.keyboard2:
            self.keyboard2.add(i)

    def kb_2_inline(self, coaches):
        self.inl_2 = telebot.types.InlineKeyboardMarkup()
        for i in coaches:
            self.inl_2.add(telebot.types.InlineKeyboardButton(i, callback_data=i))


while True:
    t = Timer(till_restart, time_out)
    t.start()
    res()
