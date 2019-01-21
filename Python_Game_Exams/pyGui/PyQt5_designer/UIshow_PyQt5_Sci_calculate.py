import sys
from PyQt5.QtWidgets import (QMainWindow, QApplication)
from PyQt5_Sci_calculate import *
class UiShow_calculate(QMainWindow,Ui_Ui_PyQt_xufang):
    def __init__(self,parent = None):
        super(UiShow_calculate,self).__init__(parent)
        self.setupUi(self)
        # for pBtn_i in range(35):
        #     self.pBtn_Dic['pBtn_' + str(pBtn_i)].clicked.connect(self.pBtn_Click_Function(pBtn_Dic['pBtn_' + str(pBtn_i)]))
    # def pBtn_Click_Function(self):
    #     self.btnStart.clicked.connect(self.slotAdd)
    # def pBtn_Click_Function(self,pBtn_object_Num):
    #     self.Displaytext.setPlainText(pBtn_object_Num.getText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UiShow_calculate()
    ex.show()
    sys.exit(app.exec_())