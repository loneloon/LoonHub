
class Timer:
    def __init__(self):
        import datetime

        self.cur_date = datetime.datetime.today()

        self.cd_list = str(self.cur_date).split('-')


        try:
            self.nxt_day = datetime.datetime(int(self.cd_list[0]), int(self.cd_list[1]), int(self.cd_list[2][0:2]) + 1,
                                             0,
                                             0, 0)
        except ValueError:
            self.nxt_day = datetime.datetime(int(self.cd_list[0]), int(self.cd_list[1]) + 1, 1, 0, 0, 0)

    def nextday_in(self):
        return str(self.nxt_day - self.cur_date)[0:-7]



