import random
import time
from threading import Timer
import os
import signal

timeleft = 60
solved = 0

def time_out():
    global timeleft
    timeleft = 0
    print(f"\nTime's up! You got {solved} points.")
    os.kill(os.getpid(), signal.SIGINT)


class Game:
    def __init__(self):
        global timeleft, solved

        self.solved = solved


    def loop(self):
        global timeleft, solved

        print("Try to solve as many problems as possible. You have 60 seconds!\n")
        input("Press any key to start: \n")

        while timeleft > 0:
            result = self.Problems().new_problem(self.Problems().choose_op())
            if timeleft > 0:
                timeleft -= result[1]
                if result[0] == 1:
                    solved += 1


        print(f'Time is up! You gained {self.solved} points.')

    class Problems:
        def __init__(self):
            self.operations = ['+', '-', '*', '/']
            self.left = 0
            self.right = 0
            self.result = 0
            self.start = 0
            self.end = 0
            self.timepassed = 0
            self.user_answer = 0

        def choose_op(self):
            return random.choice(self.operations)

        def new_problem(self, operation):
            global timeleft

            if operation in '+-':
                self.left, self.right = random.randint(0, 200), random.randint(0, 200)
                if operation == '+':
                    self.result = self.left + self.right
                else:
                    self.result = self.left - self.right
            else:
                if operation == '*':
                    self.left, self.right = random.randint(0, 10), random.randint(0, 10)
                    self.result = self.left * self.right

                else:
                    self.left = random.randint(27, 101)
                    self.right = random.randint(1, 9)
                    while (self.left % self.right != 0):
                        self.left = random.randint(27, 101)
                        self.right = random.randint(1, 9)
                    self.result = int(self.left / self.right)

            print(f'{self.left} {operation} {self.right} = ?')

            self.start = time.time()
            try:
                t = Timer(timeleft, time_out)
                t.start()
                self.user_answer = int(input('Your answer: '))
                t.cancel()
            except ValueError:
                self.user_answer = None
            self.end = time.time()
            self.timepassed = round((self.end - self.start), 2)

            if self.user_answer == self.result:
                print('Correct!\n')
                return [1, self.timepassed]
            else:
                print('False!\n')
                return [0, self.timepassed]


Game().loop()