import datetime, time, json


class Notifications:

    def __init__(self, bot, chat_id):

        self.bot = bot
        self.chat_id = chat_id

        with open('json/timers.json', 'r', encoding="utf-8") as tf:
            self.timers = json.load(tf)

    # def check_send(self):
    #     while self.timers:
    #
    #         cur_time = str(datetime.datetime.now().strftime('%H:%M'))
    #
    #         if cur_time in self.timers.keys():
    #             try:
    #                 self.bot.send_message(self.chat_id, self.timers[cur_time])
    #                 time.sleep(60)
    #                 # del self.timers[cur_time]
    #             except:
    #                 print('server might be restarting...hold up')
    #
    #         time.sleep(5)
    #
    #     if not self.timers:
    #         print('No messages left. Exiting...')

    def check_send(self):
        while self.timers:

            cur_time = str(datetime.datetime.now().strftime('%H:%M'))
            cur_date = str(datetime.datetime.now().strftime('%Y-%m-%d'))

            if cur_date in self.timers.keys():
                if cur_time == "20:00":
                    try:
                        self.bot.send_message(self.chat_id, self.timers[cur_date])
                        time.sleep(60)
                        # del self.timers[cur_time]
                    except:
                        print('server might be restarting...hold up')

            time.sleep(5)

        if not self.timers:
            print('No messages left. Exiting...')
