# -*- coding: utf-8 -*-

from PyQt4.QtGui import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt_exam2_dialog1 import Dialog1
from PyQt_exam2_dialog2 import Dialog2
# from PyQt4.QtCore import QString
import Py_Qt5Designer_Exam1
Ui_XuFang = Py_Qt5Designer_Exam1.Ui_XuFang


class ContentWidget(QDialog):
    def __init__(self,parent = None ):
        super(ContentWidget, self).__init__(parent)
        # self.setStyleSheet("background: black")

class ShowUI1(QtWidgets.QMainWindow, Ui_XuFang):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_XuFang.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象


class IndexWidget1(QDialog):
    def __init__(self,parent = None ):
        super(IndexWidget1, self).__init__(parent)
        # self.setStyleSheet("background: red")


class TabWidget(QTabWidget):
    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.resize(400, 300)
        self.mContent = ShowUI1()
        self.mIndex = IndexWidget1()
        self.addTab(self.mContent, u"内容")
        self.addTab(self.mIndex, u"索引")


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    t = TabWidget()
    t.show()
    app.exec_()
