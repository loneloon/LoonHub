import numpy as np
import random
import time
import datetime
import copy
#matrix = np.array([[random.randint() for i in range(9)] for i in range(9)])


class SudokuTable:
    def __init__(self):

        self.ready = False
        self.disrupt = False
        self.total_tables = 0
        self.sync = datetime.datetime.now()

        while not self.ready:
            self.total_tables += 1
            self.disrupt = False

            self.matrix = [[0 for i in range(9)] for j in range(9)]

            for x_box in range(3):
                for y_box in range(3):
                    box_contents = []
                    for x_num in range(3):
                        for y_num in range(3):
                            num = random.randint(1, 9)
                            y_contents = []
                            for i in range(9):
                                y_contents.append(self.matrix[i][y_num + y_box*3])
                            self.counter = 0
                            while (num in box_contents) or (num in self.matrix[x_num + x_box*3]) or (num in y_contents):
                                num = random.randint(1, 9)
                                self.counter += 1
                                if self.counter > 10000:
                                    self.disrupt = True
                                    self.counter = 0
                                    break
                            box_contents.append(num)
                            self.matrix[x_num + x_box * 3][y_num + y_box * 3] = num
                            #time.sleep(0.5)
                            #print(np.array(matrix))
                            if self.disrupt:
                                break
                        if self.disrupt:
                            break
                    if self.disrupt:
                        break
                if self.disrupt:
                    break

            if self.disrupt:
                continue

            self.ready = True

            for i in range(9):
                for j in range(9):
                    if self.matrix[i][j] == 0:
                        self.ready = False
                        break


        #print(np.array(self.matrix))

        self.matrix2 = copy.deepcopy(self.matrix)

        #print(f"Total elapsed time = {(datetime.datetime.now() - self.sync).microseconds/(10**5)} seconds.")
        #print(f"Total attempts = {self.total_tables}!")

    def get_table(self):
        for i in range(53):
            box_x = random.randint(0, 8)
            box_y = random.randint(0, 8)

            while self.matrix2[box_x][box_y] == 0:
                box_x = random.randint(0, 8)
                box_y = random.randint(0, 8)

            if self.matrix2[box_x][box_y] != 0:
                self.matrix2[box_x][box_y] = 0

        return self.matrix2

    def get_solved(self):
        return self.matrix


#test = SudokuTable()
#print(np.array(test.get_table()))
#print(np.array(test.get_solved()))