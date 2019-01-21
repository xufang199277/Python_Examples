import sys
from PyQt5.QtWidgets import QPushButton,QApplication,QWidget

class win1(QWidget):
    def __init__(self):
        super(win1,self).__init__()
        self.UI_init()
    def UI_init(self):
        self.setGeometry(100,300,700,500)
        self.setWindowTitle("windows1")
        quitButton = QPushButton("关闭",self)
        quitButton.setGeometry(100,40,50,50)
        quitButton.setStyleSheet("background-color:red")
        quitButton.clicked.connect(self.close)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Cwin1 = win1()
    Cwin1.show()
    sys.exit(app.exec_())



