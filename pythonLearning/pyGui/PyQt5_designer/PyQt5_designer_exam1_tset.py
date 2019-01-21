# Py_Qt5Designer_Exam1_test中使用QWidget
# from PyQt5 import QtWidgets
# import Py_Qt5Designer_Exam1
# import sys
# Ui_XuFang = Py_Qt5Designer_Exam1.Ui_XuFang
# class MyWindow(QtWidgets.QWidget):
#     def __init__(self, parent=None):
#         QtWidgets.QWidget.__init__(self, parent)
#         self.ui = Ui_XuFang()
#         self.ui.setupUi(self)
#         # self.ui.btnQuit.clicked.connect(QtWidgets.qApp.quit)
#
# if __name__ == "__main__":
#     app = QtWidgets.QApplication(sys.argv)
#     win = MyWindow()
#     win.show()
#     sys.exit(app.exec_())


# Py_Qt5Designer_Exam1_test中使用QMainWindow
import Py_Qt5Designer_Exam1
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

