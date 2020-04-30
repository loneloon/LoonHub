import random
import time
from threading import Timer

class Problems:
    def __init__(self):
        self.operations = ['+', '-', '*', '/']
        self.left = 0
        self.right = 0
        self.prob_string = None
        self.result = None

    def choose_op(self):
        return random.choice(self.operations)

    def new_problem(self, operation):
        if operation in '+-':
            if operation == '+':
                self.left, self.right = random.randint(0, 200), random.randint(0, 200)
                self.result = self.left + self.right
            else:
                self.left, self.right = random.randint(0, 200), random.randint(0, 200)
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

        self.prob_string = f'{self.left} {operation} {self.right} = ?'





