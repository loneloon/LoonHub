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

        with open('json/spy.json', 'r') as sd:
            self.spy_data = json.load(sd)

        @bot.message_handler(commands=['start'])
        def start_message(message):

            bot.send_message(message.chat.id, self.greeting)

        @bot.message_handler(commands=['quiz'])
        def quiz_thread(message):

            self.tested = False
            coach = ''

            self.kb_1()

            # for record in self.spy_data:
            #     if record['user'] == message.from_user.username:
            #         coach = record['curator']
            #         self.tested = True
            #         break

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

            if message.from_user.username.lower() in ['loneloon', 'kejloon']:

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
                            # if type(reply) == list and type(reply[0]) == str:
                            #
                            #     bot.send_message(message.chat.id, reply[1], reply_markup=telebot.types.ReplyKeyboardRemove())
                            #     # bot.edit_message_reply_markup(message.chat.id, reply_markup=self.keyboard3)
                            #
                            #     coach = reply[0]
                            #
                            #     # json dump
                            #
                            #     with open('json/spy.json', 'r') as sd:
                            #         self.spy_data = json.load(sd)
                            #
                            #     self.spy_data.append(
                            #         {"user": message.from_user.username,
                            #          "curator": coach,})
                            #
                            #     print(self.spy_data)
                            #
                            #     json.dump(self.spy_data, open('json/spy.json', 'w+'), indent=2, ensure_ascii=True)
                            #
                            #     self.q.all[message.chat.id]['run'] = False
                            #     print(self.q.all)
                            #     del self.q.all[message.chat.id]
                            #     print(self.q.all)
                            #
                            #     bot.send_message(message.chat.id,
                            #                      'Если у Вас остались какие-то вопросы наш администратор будет рад вам ответить!')
                            # else:


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
                                # bot.edit_message_reply_markup(message.chat.id, reply_markup=self.keyboard3)

                                coach = reply[0]

                                # json dump

                                with open('json/spy.json', 'r', encoding='utf-8') as sd:
                                    self.spy_data = json.load(sd)

                                self.spy_data.append(
                                    {"user": message.from_user.username,
                                     "curator": coach, })

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

        # main loop

        bot.polling()

    def kb_1(self):
        self.keyboard1 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True,
                                                           one_time_keyboard=True)

        self.keyboard1.row('Да', 'Нет')

    def kb_2(self):
        self.keyboard2 = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True, row_width=5)
        print(self.q.keyboard2)
        self.keyboard2.row()
        for i in self.q.keyboard2:
            self.keyboard2.add(i)



while True:
    try:
        BotBase(token='1241217774:AAGrnbja0zr4dK1fIiEVe3SKwsTltyEL3K8')
    except:
        BotBase(token='1241217774:AAGrnbja0zr4dK1fIiEVe3SKwsTltyEL3K8')
