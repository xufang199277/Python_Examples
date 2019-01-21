# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calculate.ui'
# Author : XuFang
from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial

class Ui_Ui_PyQt_xufang(object):
    def setupUi(self, Ui_PyQt_xufang):
        Ui_PyQt_xufang.setObjectName("Ui_PyQt_xufang")
        Ui_PyQt_xufang.setEnabled(True)
        Ui_PyQt_xufang.resize(416, 645)
        Ui_PyQt_xufang.setMaximumSize(QtCore.QSize(419, 645))
        Ui_PyQt_xufang.setWindowTitle("科学计算器_许放")
            self.centralwidget = QtWidgets.QWidget(Ui_PyQt_xufang)
            self.centralwidget.setObjectName("centralwidget")
            self.Displaytext = QtWidgets.QTextEdit(self.centralwidget)
            self.Displaytext.setGeometry(QtCore.QRect(0, 0, 418, 321))
            self.Displaytext.setObjectName("Displaytext")
            font = QtGui.QFont()
            font.setPointSize(24)
            font.setBold(True)
            font.setWeight(75)
            self.Displaytext.setFont(font)
            font.setPointSize(12)
            # font.setBold(True)
            font.setWeight(75)
            self.pBtn_Dic = {}
            Geometry_X = -83
            Geometry_Y = 275
            pBtn_row = 1
            self.pBtn_TextList = ["2nd", "deg", "sin", "cos", "tan", "Xy", "lg", "ln", "(", ")", "√x", "C", "del", "%", "/",
                             "X!", "7", "8", "9", "*", "1/X", "4", "5", "6", "-", "pi", "1", "2", "3", "+", "change", "e", "0", ".", "="]
            for pBtn_i in range(35):
                if pBtn_i-int(pBtn_i/5) <= 4*pBtn_row:
                    Geometry_X = Geometry_X + 83
                    if pBtn_i-5*int(pBtn_i/5) == 0:
                        Geometry_X = 0
                        Geometry_Y = Geometry_Y + 46
                        pBtn_row = pBtn_row + 1
                self.pBtn_Dic['pBtn_' + str(pBtn_i)] = QtWidgets.QPushButton(self.centralwidget)
                self.pBtn_Dic['pBtn_' + str(pBtn_i)].setGeometry(QtCore.QRect(Geometry_X, Geometry_Y, 85, 48))
                self.pBtn_Dic['pBtn_' + str(pBtn_i)].setFont(font)
                self.pBtn_Dic['pBtn_' + str(pBtn_i)].setText(self.pBtn_TextList[pBtn_i])
            self.pBtn_Dic['pBtn_' + str(2)].clicked.connect(partial(self.pBtn_Click_Function, self.pBtn_Dic['pBtn_' + str(1)]))

        Ui_PyQt_xufang.setCentralWidget(self.centralwidget)
        # QtCore.QMetaObject.connectSlotsByName(Ui_PyQt_xufang)
    def pBtn_Click_Function(self,Ui_PyQt_xufang, pBtn_Object_Num):
        # self.Displaytext.setPlainText(pBtn_Object_Num)
        pBtn_Object_Num.setText("100")
        # self.Displaytext.setPlainText(pBtn_Object_Num.Text())



