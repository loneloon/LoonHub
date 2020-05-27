
class Entry:
    def __init__(self):
        import datetime

        # setting current date

        self.cur_date = datetime.date.today()

        self.cd_list = str(self.cur_date).split('-')

        if int(self.cd_list[1]) < 12:
            nxt_mon = datetime.date(int(self.cd_list[0]), int(self.cd_list[1]) + 1, 1)
        else:
            nxt_mon = datetime.date(int(self.cd_list[0]) + 1, 1, 1)

        self.days_left = int((str(nxt_mon - self.cur_date).split(' '))[0])

        self.saved = 0
        self.balance = 0
        self.allowed_expense = 0
        self.left4td = 0
        self.last_log = self.cur_date
        self.leftovers = 0

        try:
            register = open("reg_log", "r")
            self.first_log_at = False    # first log all time
            record = register.readlines()
            hist_imp = record[0][0:-1].split("/")
            self.balance, self.saved, self.allowed_expense = round(float(hist_imp[1]), 2), round(float(hist_imp[2]), 2), round(float(hist_imp[3]), 2)
            if hist_imp[0] != str(self.cur_date):
                self.first_log_today = True
                self.last_log = datetime.date(int(hist_imp[0].split('-')[0]), int(hist_imp[0].split('-')[1]),
                                         int(hist_imp[0].split('-')[2]))
                self.mia_days = int((str(self.cur_date - self.last_log).split(' '))[0])

                #if self.mia_days > 1:
                #    oneormany = 's'
                #else:
                #    oneormany = ''
                #print(f"Your last login was {self.mia_days} day%s ago." % oneormany)

                self.leftovers = round(float(self.mia_days - 1) * self.allowed_expense + float(hist_imp[4]), 2)
                if self.leftovers > self.balance:
                    self.leftovers = self.balance
                    self.balance = 0
                #print(f"You saved {self.leftovers}")

            else:
                print("You've already logged in today!")
                self.first_log_today = False
                self.left4td = round(float(hist_imp[4]), 2)
            register.close()
        except FileNotFoundError:
            hist = open("history", "w+")
            hist.close()
            self.first_log_at = True
            self.first_log_today = True
            print(
                "Welcome to CashGate! I will help you organise your savings, control your spending and monitor your balance!")

    def add_to_history(self, action):
        hist = open("history", "a+")
        hist.write(f"{action}\n")
        hist.close()

    def left_add_to_balance(self):
        self.add_to_history(f"+{self.leftovers} added to balance")
        self.balance += self.leftovers
        self.allowed_expense = self.balance / self.days_left
        self.leftovers = 0
        self.left4td += self.allowed_expense


    def left_add_to_saved(self):
        self.add_to_history(f"+{self.leftovers} saved")
        self.saved += self.leftovers
        self.left4td += self.allowed_expense
        self.leftovers = 0

    def left_spend_today(self):
        if self.balance > self.allowed_expense:
            self.left4td += self.leftovers + self.allowed_expense
        else:
            self.left4td += self.leftovers
        self.add_to_history(f"+{self.leftovers} + daily {self.allowed_expense} allocated to spend today")
        self.leftovers = 0

    def deposit(self, amount):
        self.add_to_history(f"+{amount} added to balance")
        self.balance += amount

    def recount(self, custom_days=None):
        if custom_days is None:
            self.allowed_expense = round(float(self.balance / self.days_left), 2)
            self.left4td = self.allowed_expense
        else:
            self.allowed_expense = round(float(self.balance / custom_days), 2)
            self.left4td = self.allowed_expense
            self.add_to_history(f"+{self.allowed_expense} allocated to spend today")

    def simple_spend(self, amount):
        if self.allowed_expense != 0:
            if amount <= self.left4td:
                self.left4td -= amount
                self.balance -= amount
                self.add_to_history(f"-{amount} spent")
                return [amount, self.left4td]
            else:
                return "      Not enough left!"
        else:
            return "Please count/recount expenses before spending cash!"

    def save_quit(self):
        if self.leftovers == 0:
            register = open("reg_log", "w")
            register.write(f'{self.cur_date}/{self.balance}/{self.saved}/{self.allowed_expense}/{self.left4td};')
            register.close()






