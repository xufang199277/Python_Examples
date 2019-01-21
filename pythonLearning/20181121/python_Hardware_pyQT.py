#!/usr/bin/python
# _*_ coding: utf-8 _*_
#Function: 使用PyQt4模块画界面
#Author: xufang

import  sys
from PyQt4 import QtGui

class GuiExample(QtGui.QWidget):
    def __init__(self):
        super(GuiExample, self).__init__()
        self.initGui()
    def initGui(self):
        QtGui.QToolTip.setFont(QtGui.QFont('sansSerif',10))
        self.setToolTip("This is a <b>QWidget</b> widget")
        button1 = QtGui.QPushButton('Button1',self)
        button1.setToolTip("This is a <b>QPushButton</b> widget")
        button1.resize(button1.sizeHint())
        button1.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle("Tooltips")
        self.show()

def pyqtTooltip():
    app = QtGui.QApplication(sys.argv)
    ExGui = GuiExample()
    sys.exit(app.exec_())

if __name__ == "__main__":
    pyqtTooltip()

