import telebot
import quiz
import json


class BotBase:

    def __init__(self, token):

        bot = telebot.TeleBot(token)

        # self.activated = False

        self.greeting = '''
        Привет!

Сейчас ты на одном из основополагающих этапов курса – выбор куратора.
Это человек, который не просто будет на связи с тобой 21 день, а будет тебя направлять и поддерживать во всех твоих осознаниях.

Ответь на несколько вопросов, которые приведут тебя к твоему будущему куратору, с которым работа на курсе будет проходить наиболее комфортно и эффективно.


Нажми /quiz, чтобы начать
        '''

        self.q = quiz.Quiz()

        with open('json/spy.json', 'r', encoding='utf-8') as sd:
            self.spy_data = json.load(sd)

        @bot.message_handler(commands=['start'])
        def start_message(message):

            bot.send_message(message.chat.id, self.greeting)


            if message.from_user.username not in self.spy_data.keys():
                self.spy_data[message.from_user.username] = ""

                json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                          ensure_ascii=True)

        @bot.message_handler(commands=['quiz'])
        def quiz_thread(message):


            coach = ''

            self.kb_1()

            try:
                if self.spy_data[message.from_user.username] != "":
                    coach = self.spy_data[message.from_user.username]
                    self.tested = True
                else:
                    self.tested = False
            except:
                self.tested = False

            if self.tested:
                bot.send_message(message.chat.id, f'Вы уже выбрали куратора! Ваш куратор: {coach}')
            else:

                self.q.all[message.chat.id] = {'level': 0, 'path': '', 'waiting': False, 'choice': None, 'answer': '',
                                               'run': False, 'coach': ''}
                self.q.all[message.chat.id]['run'] = True

                bot.send_message(message.chat.id, self.q.ask_back(id=message.chat.id), reply_markup=self.keyboard1)

        @bot.message_handler(content_types=['text'])
        def send_text(message):

            self.kb_1()


            if ('stats' in message.text.lower()) and (message.from_user.username.lower() in ['loneloon', 'kejloon', "Korobkovochka"]):

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

                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                            else:

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
                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                            else:
                                if type(reply) == list and type(reply[0]) == str:

                                    bot.send_message(message.chat.id, reply[1],
                                                     reply_markup=telebot.types.ReplyKeyboardRemove())


                                    coach = reply[0]

                                    # json dump

                                    with open('json/spy.json', 'r', encoding='utf-8') as sd:
                                        self.spy_data = json.load(sd)

                                    self.spy_data[message.from_user.username] = coach

                                    print(self.spy_data)

                                    json.dump(self.spy_data, open('json/spy.json', 'w+', encoding='utf-8'), indent=2,
                                              ensure_ascii=True)

                                    self.q.all[message.chat.id]['run'] = False

                                    del self.q.all[message.chat.id]
                                    print(self.q.table)

                                    bot.send_message(message.chat.id,
                                                     'Если у Вас остались какие-то вопросы наш администратор будет рад вам ответить!')
                                else:
                                    bot.send_message(message.chat.id, reply, reply_markup=self.keyboard1)
                except:
                    pass


        # main loop

        bot.polling()

    def kb_1(self):
        self.keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                           one_time_keyboard=True)

        self.keyboard1.row('Да', 'Нет')

    def kb_2(self):
        self.keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        print(self.q.keyboard2)

        for i in self.q.keyboard2:
            self.keyboard2.add(i)

    def kb_2_inline(self):
        self.inl_2 = telebot.types.InlineKeyboardMarkup()
        for i in self.q.keyboard2:
            self.inl_2.row(telebot.types.InlineKeyboardButton(i, callback_data=i))

while True:
    try:
        BotBase(token='1241217774:AAGrnbja0zr4dK1fIiEVe3SKwsTltyEL3K8')
    except:
        BotBase(token='1241217774:AAGrnbja0zr4dK1fIiEVe3SKwsTltyEL3K8')
