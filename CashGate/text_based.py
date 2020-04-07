import datetime

# setting current date


cur_date = datetime.date.today()

print(f"Today is {cur_date}!")

cd_list = str(cur_date).split('-')

if int(cd_list[1]) < 12:
    nxt_mon = datetime.date(int(cd_list[0]), int(cd_list[1])+1, 1)
else:
    nxt_mon = datetime.date(int(cd_list[0])+1, 1, 1)



days_left = int((str(nxt_mon - cur_date).split(' '))[0])


saved = 0
balance = 0
options = ['1', '2', '3', '4', '5', '6']
allowed_expense = 0
left4td = 0

try:
    register = open("reg_log", "r")
    print("Welcome back!")
    record = register.readlines()
    hist_imp = record[0][0:-1].split("/")
    balance, saved, allowed_expense = int(hist_imp[1]), int(hist_imp[2]), int(hist_imp[3])
    if hist_imp[0] != str(cur_date):
        last_log = datetime.date(int(hist_imp[0].split('-')[0]), int(hist_imp[0].split('-')[1]), int(hist_imp[0].split('-')[2]))
        mia_days = int((str(cur_date-last_log).split(' '))[0])
        if mia_days > 1:
            oneormany = 's'
        else:
            oneormany = ''
        print(f"Your last login was {mia_days} day%s ago." % oneormany)
        leftovers = int(mia_days-1)*allowed_expense + int(hist_imp[4])
        print(f"You saved {leftovers}")
        print("")
        print("What are you willing to do with all that money?")
        print("")
        print("1 - Add to balance and recount allowed expenses")
        print("2 - Add to savings!")
        print("3 - SPEND THEM TODAY!")
        saved_choice = input("Make a choice: ")
        if saved_choice == '1':
            balance += leftovers
            allowed_expense = balance/days_left
        elif saved_choice == '2':
            saved += leftovers
            left4td += allowed_expense
        elif saved_choice == '3':
            left4td += leftovers + allowed_expense
    else:
        print("You've already logged in today!")
        left4td = int(hist_imp[4])
    register.close()
except FileNotFoundError:
    print("Welcome to CashGate! I will help you organise your savings, control your spending and monitor your balance!")


while True:
    print('''
1 = Add cash
2 = Count/Recount allowed expenses
3 = Spend
4 = How much is left for today?
5 = Balance
6 = Exit''')
    choice = input("Choose action: ")
    print("")
    if choice in options:
        if choice == '1':
            balance += int(input("Enter the sum: "))
            saved = int(input("How much do you want to save? "))
            balance -= saved
        elif choice == '2':
            if input("Are we counting until the end of the current month? [Y/N]: ") in 'Yy':
                allowed_expense = int(balance / days_left)
                left4td = allowed_expense
                print("")
                print("Acquired funds were successfully allocated for each day until the end of the month.")
                print(f"Tomday you cam spemd {left4td} moneys.")
            else:
                days_left = int(input("Over the course of how many days are you willing to spread the balance? (including today)"))
                allowed_expense = int(balance / days_left)
                left4td = allowed_expense
                print("")
                print("Acquired funds were successfully allocated for each day until the end of the month.")
                print(f"Tomday you cam spemd {left4td} moneys.")
        elif choice == '3':
            if allowed_expense != 0:
                withdraw = int(input("How much are you spending?: "))
                if withdraw <= left4td:
                    left4td -= withdraw
                    balance -= withdraw
                    print(f"{withdraw} were successfully withdrawn!")
                    print(f"You hamve {left4td} moneys lemft for tomday!")
                else:
                    print("You don't have that many left!")
                    print(f"You only have {left4td} left!")
                    if input("Are you willing to spend that? [Y/N]: ") in 'Yy':
                        balance -= left4td
                        left4td = 0
                    else:
                        if input("Are you willing to withdraw more cash to spend today? (Daily amount will be recounted) [Y/N]: ") in 'Yy':
                            withdraw = int(input("How much?: "))
                            left4td += withdraw
                            print("Recounting expenses!")
                            allowed_expense = int((balance-withdraw)/(days_left-1))
                            print(f"Due to your last withdrawal your new daily max is {allowed_expense}")
                        else:
                            pass
            else:
                print("Please count/recount expenses before spending cash!")
        elif choice == '4':
            print(f"You hamve {left4td} moneys lemft for tomday!")
        elif choice == '5':
            print(f"Your balance: {balance}.")
            print(f"You are saving: {saved}")
            print(f"Your asserted daily max for expenses: {allowed_expense}")
        else:
            break
    else:
        print("'There's no such option!")


register = open("reg_log", "w")
register.write(f'{cur_date}/{balance}/{saved}/{allowed_expense}/{left4td};')
register.close()

