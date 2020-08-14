import datetime, time


class Notifications:

    def __init__(self, bot, chat_id):

        self.bot = bot
        self.chat_id = chat_id

        self.timers = {"08:52": 'This is a test notification for 8:34',
                       '08:37': 'This is a test notification for 8:37',
                       '08:43': 'This is a test notification for 8:43'}

    def check_send(self):
        while self.timers:

            cur_time = str(datetime.datetime.now().strftime('%H:%M'))

            if cur_time in self.timers.keys():
                try:
                    self.bot.send_message(self.chat_id, self.timers[cur_time])
                    time.sleep(60)
                    # del self.timers[cur_time]
                except:
                    print('server might be restarting...hold up')

            time.sleep(5)

        if not self.timers:
            print('No messages left. Exiting...')
