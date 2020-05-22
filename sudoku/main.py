# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testgui.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import numpy as np
from sudoku_table import SudokuTable

import time

table_obj = SudokuTable()
table = table_obj.get_table()
print(np.array(table))

solved_table = table_obj.get_solved()
solved_string = ""

for i in range(9):
    for j in range(9):
        solved_string += str(solved_table[i][j])

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(540, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMaximumSize(QtCore.QSize(608, 640))
        MainWindow.setMinimumSize(QtCore.QSize(608, 640))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.gridGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.gridGroupBox.setGeometry(QtCore.QRect(0, 0, 540, 540))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        self.gridGroupBox.setSizePolicy(sizePolicy)
        self.gridGroupBox.setMaximumSize(QtCore.QSize(540, 540))
        self.gridGroupBox.setObjectName("gridGroupBox")
        self.gridGroupBox.setStyleSheet("#gridGroupBox {background-color: rgb(35, 0, 0); background-image: url(./back.png); border-color: rgb(0, 0, 0);}")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridGroupBox)
        self.gridLayout_2.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.gridLayout_2.setObjectName("gridLayout_2")


        self.boxes = []

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)

        font = QtGui.QFont()
        font.setPointSize(34)

        self.onlyInt = QtGui.QIntValidator()


        for i in range(9):
            for j in range(9):
                self.boxes.append(QtWidgets.QLineEdit(self.gridGroupBox))
                self.boxes[-1].setObjectName(f"Box:{i+1}{j+1}")
                sizePolicy.setHeightForWidth(self.boxes[-1].sizePolicy().hasHeightForWidth())
                self.boxes[-1].setSizePolicy(sizePolicy)
                self.boxes[-1].setMaximumSize(QtCore.QSize(60, 60))
                self.boxes[-1].setAlignment(QtCore.Qt.AlignCenter)
                self.boxes[-1].setEnabled(True)
                self.boxes[-1].setFont(font)
                self.boxes[-1].setMaxLength(1)
                self.boxes[-1].setValidator(self.onlyInt)
                self.boxes[-1].setInputMethodHints(QtCore.Qt.ImhMultiLine | QtCore.Qt.ImhNoTextHandles | QtCore.Qt.ImhPreferNumbers)
                self.boxes[-1].setStyleSheet("background-color: rgb(16, 19, 41);\n"
                               "color: rgb(255, 255, 255);\n"
                               "\n"
                               "border-color: rgb(0,0,0);"
                               "border-style: flat;")
                self.gridLayout_2.addWidget(self.boxes[-1], i, j, 1, 1)

        #  self.solver = QtWidgets.QPushButton(self.gridGroupBox)
        #         self.solver.setStyleSheet("background-color: rgb(149, 18, 18);\n"
        #                                   "color: rgb(241, 241, 241);\n"
        #                                   "font: 20pt \"BigNoodleTitling\";"
        #                                   "border-style: outset;"
        #                                     "border-width: 2px;"
        #                                     "border-radius: 5px;"
        #                                     "border-color: black;")
        #         self.solver.setObjectName("solver")
        #         self.gridLayout_2.addWidget(self.solver, 10, 3, 1, 3)

        self.solver = QtWidgets.QPushButton(self.gridGroupBox)
        self.solver.setStyleSheet("background-color: rgb(149, 18, 18);\n"
                                  "color: rgb(241, 241, 241);\n"
                                  "font: 22pt \"BigNoodleTitling\";")
        self.solver.setObjectName("solver")
        self.gridLayout_2.addWidget(self.solver, 10, 0, 1, 3)

        self.checker = QtWidgets.QPushButton(self.gridGroupBox)
        self.checker.setStyleSheet("background-color: rgb(0, 173, 127);\n"
                                  "color: rgb(241, 241, 241);\n"
                                  "font: 22pt \"BigNoodleTitling\";")
        self.checker.setObjectName("solver")
        self.gridLayout_2.addWidget(self.checker, 10, 3, 1, 3)

        self.mistakes = []

        for i in range(3):
            self.mistakes.append(QtWidgets.QLabel(self.gridGroupBox))
            self.mistakes[-1].setObjectName(f"X:{i+1}")
            self.mistakes[-1].setStyleSheet("background-color: rgb(12, 70, 105);")
            self.gridLayout_2.addWidget(self.mistakes[-1], 10, 6+i, 1, 1)


        MainWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(MainWindow)
        #         self.menubar.setGeometry(QtCore.QRect(0, 0, 540, 21))
        #         self.menubar.setObjectName("menubar")
        #         MainWindow.setMenuBar(self.menubar)
        #         self.statusbar = QtWidgets.QStatusBar(MainWindow)
        #         self.statusbar.setObjectName("statusbar")
        #         MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.checker.clicked.connect(self.check_input)
        self.solver.clicked.connect(self.solve)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.solver.setText(_translate("MainWindow", "SOLVE"))
        self.checker.setText(_translate("MainWindow", "CHECK"))
        MainWindow.setWindowTitle(_translate("MainWindow", "Sudoku"))

        self.counter = 0

        for i in range(9):
            for j in range(9):
                if table[i][j] != 0:
                    self.boxes[self.counter].setText(str(table[i][j]))
                    self.boxes[self.counter].setStyleSheet("background-color: rgb(16, 19, 41);"
                                                           "color: rgb(25, 151, 224);"
                                                           "border-style: flat;")
                self.counter += 1

    def error(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Ooops!")
        msg.setInformativeText('Some number is incorrect!')
        msg.setWindowTitle("Oh no!")
        msg.exec_()

    def victory(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Yaay!")
        msg.setInformativeText('Looks like you did it! :)')
        msg.setWindowTitle("Victory!")
        msg.exec_()

    def check_input(self):
        global solved_string

        self.solved = True

        self.game_input = ""

        for box in self.boxes:
            if box.text() != '':
                self.game_input += box.text()
            else:
                self.solved = False
                self.game_input += '0'

        #print(self.game_input)

        mistakes = False

        for idx, number in enumerate(self.game_input):
            if number != '0':
                if number != solved_string[idx]:
                    mistakes = True

        if mistakes:
            self.error()
        elif self.solved and not mistakes:
            self.victory()

    def solve(self):
        global solved_string
        #print(solved_string)

        for idx, num in enumerate(solved_string):

            if self.boxes[idx].text() == '':
                self.boxes[idx].setText(num)
                self.boxes[idx].update()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
