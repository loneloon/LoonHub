import random, json
import telebot

class Quiz:

    def __init__(self):
        # self.level = 0

        # self.answer = ''
        # self.path = ''
        # self.choice = None
        # self.waiting = False
        self.q_out = ''
        # self.run = False
        self.all = {}
        self.keyboard2 = []


        # self.table = {
        # 'Стас':[0, 10],  # [actual, max]
        # 'Аслан':[0, 4],
        # 'Маша': [0, 4],
        # 'Залина': [0, 4],
        # 'Аза':[0, 7],
        # 'Лена':[0, 8],
        # 'Линда':[0, 7],
        # 'Катя':[0, 4],
        # 'Дима': [0, 3],
        # 'Вероника': [0, 3],
        # }


        # self.selected_coach = None

        # self.curators = {
        #     '00': {
        #         'Наставник - более четкий и строгий подход в работе': ['Стас', 'Маша', 'Аза', 'Залина'],
        #         'Друг - свободное общение и эмоции': ['Аслан', 'Вероника', 'Линда', 'Дима', 'Катя'],
        #         'Мотиватор - поддержка и вдохновение к действию': ['Аслан', 'Лена', 'Залина', 'Катя', 'Аза'],
        #         'Наблюдатель - точечные подсказки в работе': ['Маша', 'Линда', 'Вероника', 'Дима'],
        #         'Я не знаю, кто мне нужен и чего я хочу ': ['Аслан', 'Лена', 'Залина'],
        #
        #     },
        #     '01': {
        #         'Наставник - более четкий и строгий подход в работе': ['Стас', 'Маша', 'Аза', 'Залина'],
        #         'Друг - свободное общение и эмоции': ['Аслан', 'Линда'],
        #         'Мотиватор - поддержка и вдохновение к действию': ['Аслан', 'Лена', 'Залина', 'Аза'],
        #         'Наблюдатель - точечные подсказки в работе': ['Маша', 'Линда'],
        #         'Я не знаю, кто мне нужен и чего я хочу ': ['Аслан', 'Лена', 'Залина'],
        #     },
        #     '10': {
        #         'Наставник - более четкий и строгий подход в работе': ['Стас', 'Маша', 'Аза', 'Залина'],
        #         'Друг - свободное общение и эмоции': ['Аслан', 'Вероника', 'Линда', 'Катя', 'Дима'],
        #         'Мотиватор - поддержка и вдохновение к действию': ['Аслан', 'Лена', 'Залина', 'Катя', 'Аза'],
        #         'Наблюдатель - точечные подсказки в работе': ['Маша', 'Линда', 'Вероника', 'Дима'],
        #         'Я не знаю, кто мне нужен и чего я хочу ': ['Аслан', 'Лена', 'Залина'],
        #     },
        #     '11': {
        #         'Наставник - более четкий и строгий подход в работе': ['Стас', 'Маша', 'Аза', 'Залина'],
        #         'Друг - свободное общение и эмоции': ['Аслан', 'Линда'],
        #         'Мотиватор - поддержка и вдохновение к действию': ['Аслан', 'Лена', 'Залина', 'Аза'],
        #         'Наблюдатель - точечные подсказки в работе': ['Маша', 'Линда'],
        #         'Я не знаю, кто мне нужен и чего я хочу ': ['Аслан', 'Лена', 'Залина'],
        #     },
        #
        # }

    def ask_back(self, id, message=None):

        self.q_out = ''

        if self.all[id]['level'] < 2:
            if not self.all[id]['waiting']:
                if self.all[id]['level'] == 0:
                    self.all[id]['waiting'] = True
                    return 'Ты первый раз проходишь курс reLove Intensive?'
                elif self.all[id]['level'] == 1:
                    self.all[id]['waiting'] = True
                    if self.all[id]['path'] == '0':
                        return 'Считаешь ли ты себя открытым человеком? (тем, кто легко может делиться не только своими внешними факторами жизни, но и своими мыслями, ощущениеями, мнением)'
                    else:
                        return 'Считаешь ли ты себя открытым человеком? (тем, кто легко может делиться не только своими внешними факторами жизни, но и своими мыслями, ощущениеями, мнением)'
            else:
                if message is not None:
                    self.all[id]['answer'] = message

                if self.all[id]['answer'] != '':
                    if 'да' in self.all[id]['answer'].lower():
                        self.all[id]['path'] += '0'
                    else:
                        self.all[id]['path'] += '1'

                    self.all[id]['answer'] = ''
                    self.all[id]['level'] += 1
                    self.all[id]['waiting'] = False
        else:
            if not self.all[id]['waiting']:
                counter = 1
                self.keyboard2 = []

                with open('json/curators.json', 'r', encoding='utf-8') as ct:
                    self.curators = json.load(ct)

                with open('json/table.json', 'r', encoding='utf-8') as tb:
                    self.table = json.load(tb)

                print(self.curators)

                for mood, mentor in self.curators.items():
                    for key, val in mentor.items():
                        for person in val:
                            if self.table[person][0] == self.table[person][1]:
                                val.remove(person)

                json.dump(self.curators, open('json/curators.json', 'w+', encoding='utf-8'), indent=2,
                          ensure_ascii=True)

                for key, val in self.curators[self.all[id]['path']].items():
                    if val != []:
                        self.q_out += f'{counter}) {key}\n'
                        self.keyboard2.append(str(counter))
                    counter += 1


                    # else:
                    #     del self.curators[self.all[id]['path']][key]


                json.dump(self.curators, open('json/curators.json', 'w+', encoding='utf-8'), indent=2,
                          ensure_ascii=True)

                self.q_out = 'Выбери тип кураторства,который наиболее актуален для твоего запроса\n\n' + self.q_out
                self.all[id]['waiting'] = True
                return ['list', self.q_out]
            else:
                if message is not None:
                    self.all[id]['answer'] = message

                if self.all[id]['answer'] != '':
                    self.all[id]['choice'] = int(self.all[id]['answer'])
                    self.all[id]['answer'] = ''
                    self.all[id]['run'] = False

                    for idx, (key, value) in enumerate(self.curators[self.all[id]['path']].items()):
                        if (idx + 1) == int(self.all[id]['choice']):
                            self.q_out = ''

                            with open('json/table.json', 'r', encoding='utf-8') as tb:
                                self.table = json.load(tb)

                            print(self.table)

                            with open('json/curators.json', 'r', encoding='utf-8') as ct:
                                self.curators = json.load(ct)

                            self.all[id]['coach'] = random.choice(value)
                            while self.table[self.all[id]['coach']][0] == self.table[self.all[id]['coach']][1]:
                                for mood, mentor in self.curators.items():
                                    for key, val in mentor.items():
                                        while self.all[id]['coach'] in val:
                                            val.remove(self.all[id]['coach'])
                                self.all[id]['coach'] = random.choice(value)

                            json.dump(self.curators, open('json/curators.json', 'w+', encoding='utf-8'), indent=2,
                                      ensure_ascii=True)

                            self.table[self.all[id]['coach']][0] += 1

                            json.dump(self.table, open('json/table.json', 'w+', encoding='utf-8'), indent=2, ensure_ascii=True)

                            self.q_out += f'Спасибо за ваши ответы! Вашим куратором будет {self.all[id]["coach"]}'

                            print(self.curators)
                            break
                    return [self.all[id]["coach"], self.q_out]