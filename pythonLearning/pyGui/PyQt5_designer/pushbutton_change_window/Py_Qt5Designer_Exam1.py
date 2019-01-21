# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Py_Qt5Designer_Exam1.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_XuFang(object):
    def setupUi(self, XuFang):
        XuFang.setObjectName("XuFang")
        XuFang.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(XuFang)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(120, 60, 141, 381))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.timeEdit = QtWidgets.QTimeEdit(self.verticalLayoutWidget)
        self.timeEdit.setObjectName("timeEdit")
        self.verticalLayout.addWidget(self.timeEdit)
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        XuFang.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(XuFang)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        XuFang.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(XuFang)
        self.statusbar.setObjectName("statusbar")
        XuFang.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(XuFang)
        QtCore.QMetaObject.connectSlotsByName(XuFang)

    def retranslateUi(self, XuFang):
        _translate = QtCore.QCoreApplication.translate
        XuFang.setWindowTitle(_translate("XuFang", "MainWindow"))
        self.pushButton_3.setText(_translate("XuFang", "PushButton"))
        self.menu.setTitle(_translate("XuFang", "综合布局实例"))

