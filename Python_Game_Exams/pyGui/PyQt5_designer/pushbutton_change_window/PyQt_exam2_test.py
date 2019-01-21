import PyQt_exam2
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
Ui_XuFang = Py_Qt5Designer_Exam1.Ui_XuFang

class ShowUI(QtWidgets.QMainWindow, Ui_XuFang):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)  # 创建主界面对象
        Ui_XuFang.__init__(self)  # 主界面对象初始化
        self.setupUi(self)  # 配置主界面对象

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = ShowUI()
    win.show()
    sys.exit(app.exec_())