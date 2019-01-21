import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from calculate import *
class UiShow_calculate(QMainWindow,Ui_Ui_PyQt_xufang):
    def __init__(self,parent = None):
        super(UiShow_calculate,self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiShow_calculate()
    ex.show()
    sys.exit(app.exec_())