import random
import playsound
from gtts import gTTS
import os
import datetime
import requests


def city_forecast(city):
    url = "https://community-open-weather-map.p.rapidapi.com/weather"

    querystring = {"callback": "test", "id": "2172797", "units": "metric", "mode": "JSON", "q": city}

    headers = {
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
        'x-rapidapi-key': "06f76070f0msh333e6cde05dfe64p1b4b9cjsn767de85a32e5"
    }

    response = requests.get(f"https://community-open-weather-map.p.rapidapi.com/weather?units=metric&q={city}", headers=headers)
    data = response.json()

    return [data['weather'][0]['description'], data['main']['temp']]


class Jinx0base:
    def __init__(self):
        self.input = ''
        self.output = ''

        self.reciever_name = None

        self.sound = True

        self.moods = {1: 'positive', 0: 'neutral', -1: 'negative'}

        self.conv_progression = - 1  #  {-1: 'start', 0: 'middle', 1: 'end'}

        self.intents = {'greeting': ['hello', 'hi', 'howdy', "hey"],
                   'status check': ["what's up", "how are you"],
                   'weather': ["what's the weather like", 'outside', "weather", "how's the weather"],
                   'time': ['what time is it', "what's the time", "time", "can you tell the time?"],
                   'appreciative': ['thanks', 'thank you', 'thx', 'gracias'],
                   'farewell': ["bye", "goodbye"],
                   'command': []}

        self.responses = {
            'greeting': ["Good day sir!", "Good afternoon sir!"],
            'status check': ["I'm fine, thank you!", "I'm fine!", "Fine.", "Just chilling."],
            'appreciative': ["You're welcome!", 'You are very welcome!', 'No problem sir!', 'My pleasure!'],
            'farewell': ["Bye", "Cya", "Goodbye"],
             'command': []
        }

        self.triggers = []

        self.mood = 0

    def read(self):
        match = 0
        input = self.input.lower()

        m_check = open('lib/bad words', 'r')
        for line in m_check.readlines():
            l = line.replace('\n', '').replace('\r', '').lower()
            if input == l:
                self.mood -= 1
            else:
                for word in input.replace(',', '').split(' '):
                    if word == l:
                        self.mood -= 1
        m_check.close()

        m_check = open('lib/good words', 'r')
        for line in m_check.readlines():
            l = line.replace('\n', '').replace('\r', '').lower()
            if input == l:
                self.mood += 1
            else:
                for word in input.replace(',', '').split(' '):
                    if word == l:
                        self.mood += 1
        m_check.close()

        for w_class, content in self.intents.items():
            for type, resp in self.responses.items():
                for bit in content:
                    if bit in input:
                        if w_class == type and self.conv_progression < 0:
                            self.output = random.choice(resp)
                            self.conv_progression += 1
                            match = 1
                            break
                        elif w_class == 'greeting' and self.conv_progression >= 0:
                            self.output = 'How can i help you?'
                            match = 1
                            break
                        else:
                            if w_class == 'farewell':
                                if w_class == type:
                                    self.output = random.choice(resp)
                                    self.conv_progression = 1
                                    match = 1
                                    break
                            elif w_class == 'time':
                                self.output = 'Hold up, let me check my watch. \n'
                                self.output += f"Oh...... It's {int(str(datetime.datetime.now())[11:13])} hours, {int(str(datetime.datetime.now())[14:16])} minutes. \n"
                                if 0 < int(str(datetime.datetime.now())[11:13]) < 5:
                                    self.output += 'Working late today? sir?'
                                match = 1
                                break

                            elif w_class == 'weather':
                                self.output = 'Why would i know? ...Just kidding!\n'
                                self.output += f'Current local time is {int(str(datetime.datetime.now())[11:13])} hours, {int(str(datetime.datetime.now())[14:16])} minutes. \n'
                                self.output += str(city_forecast('Moscow')[0]).capitalize() + '. ' + f"The temperature is {city_forecast('Moscow')[1]} degrees."
                                match = 1
                                break
                            elif w_class == type:
                                self.output = random.choice(resp)
                                if w_class == 'status check':
                                    self.output += ' ' + 'Mood points:' + ' ' + str(self.mood)
                                match = 1
                                break
                    if match != 0:
                        break
                if match != 0:
                    break


        if match == 0:
            self.output = random.choice(["Sorry. I didn't quite get it.", "Huh?", 'I have no idea, sorry!'])

    def speak(self, text):
        tts = gTTS(text=text, lang="en-au")
        filename = "voice.mp3"
        tts.save(filename)
        playsound.playsound(filename)
        os.remove('voice.mp3')

    def connect(self):
        self.input = input('Talk to me: ')
        self.read()
        if self.mood < -4:
            print('You are horrible! Goodbye!')
            if self.sound:
                self.speak('You are horrible! Goodbye!')
            self.conv_progression = 1
        else:
            print(self.output)
            if self.sound:
                self.speak(self.output)


test = Jinx0base()

if input("Would you like me to speak?(as opposed to only typing)[Y/n]: ") in 'YyYesYES':
    test.sound = True
else:
    test.sound = False

if test.reciever_name is None:
    print("What should i call you?")
    test.reciever_name = input("My name is: ")

while test.conv_progression != 1:
    test.connect()
