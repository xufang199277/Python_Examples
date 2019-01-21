import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QFileDialog, QAction, QTextEdit, QLineEdit, QFrame, QColorDialog, QInputDialog, QApplication, QSizePolicy, QLabel, QFontDialog)
from PyQt5.QtGui import (QColor,QIcon)
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        col = QColor(0, 0, 0)
        self.btn1 = QPushButton('Dialog', self)
        self.btn1.move(20, 20)
        self.btn1.clicked.connect(self.showDialog)
        self.btn2 = QPushButton('Color', self)
        self.btn2.move(20, 60)
        self.btn2.clicked.connect(self.showColor)
        self.btn3 = QPushButton('Font', self)
        self.btn3.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        self.btn3.move(20, 180)
        self.btn3.clicked.connect(self.showFont)
        self.le = QLineEdit(self)
        self.le.setGeometry(130, 22.5, 100, 20)
        self.frm = QFrame(self)
        self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
        self.frm.setGeometry(130, 62, 100, 100)
        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.setGeometry(130, 180, 200, 30)


        # self.textEdit = QTextEdit()
        # # self.setCentralWidget(self.textEdit)
        # # self.statusBar()
        # openFile = QAction(QIcon('web.jpg'), 'Open', self)
        # openFile.setShortcut('Ctrl+O')
        # openFile.setStatusTip('Open new File')
        # openFile.triggered.connect(self.showDialog2)
        self.btn4 = QPushButton('Color', self)
        self.btn4.move(20, 120)
        self.btn4.clicked.connect(self.showDialog2)
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(openFile)


        self.setGeometry(300, 300, 300, 250)
        self.setWindowTitle('Input dialog')
        self.show()
    def showDialog(self):
        [text, ok] = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')
        if ok:
            self.le.setText(str(text))
    def showColor(self):
        col = QColorDialog.getColor()
        if col.isValid():
            self.frm.setStyleSheet("QWidget { background-color: %s }" % col.name())
    def showFont(self):
        [font, ok] = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)

    def showDialog2(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file','C:/users/admin/desktop/home')
        if fname[0]:
            f = open(fname[0], 'r')
            with f:
                data = f.read()
                self.textEdit.setText(data)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())



##信号与槽
# import sys
# from PyQt5.QtWidgets import QMainWindow, QPushButton, QApplication
# from PyQt5.QtCore import pyqtSignal, QObject
#
# class Communicate(QObject):
#     closeApp = pyqtSignal()
#
# class Example(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         btn1 = QPushButton("Button 1", self)
#         btn1.move(30, 50)
#         btn2 = QPushButton("Button 2", self)
#         btn2.move(150, 50)
#         btn1.clicked.connect(self.buttonClicked)
#         btn2.clicked.connect(self.buttonClicked)
#         self.statusBar()
#         self.c = Communicate()
#         self.c.closeApp.connect(self.close)
#         self.setGeometry(300, 300, 290, 150)
#         self.setWindowTitle('Event sender')
#         self.show()
#
#     def buttonClicked(self):
#         sender1 = self.sender()
#         self.statusBar().showMessage(sender1.text() + ' was pressed')

    # mousePressEvent也是一个已经存在的函数
    # def mousePressEvent(self, event):
    #     self.c.closeApp.emit()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

##菜单栏，状态栏等
# import sys
# from PyQt5.QtWidgets import QMainWindow, QApplication, QAction, qApp
# class Example(QMainWindow):
#
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#
#     def initUI(self):
#         #创建事件
#         exitAction = QAction('Exit1', self)
#         exitAction.setShortcut('Ctrl+Q')
#         exitAction.setStatusTip('Exit application')
#         exitAction.triggered.connect(qApp.quit)
#
#
#         # 创建一个菜单栏
#         menubar = self.menuBar()
#         # 添加菜单
#         fileMenu = menubar.addMenu('File')
#         # 添加事件
#         fileMenu.addAction(exitAction)
#         # 添加一个工具栏
#         self.toolbar = self.addToolBar('Exit2')#这里有问题，显示的是exitAction中的‘Exit1’而不是‘Exit2’
#         self.toolbar.addAction(exitAction)
#         self.statusBar().showMessage('Ready')
#         self.setGeometry(300, 300, 250, 150)
#         self.setWindowTitle('Menubar')
#         self.show()
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     ex = Example()
#     sys.exit(app.exec_())

##多窗口的程序
# import sys
# from PyQt5.QtWidgets import *
# from PyQt5.QtCore import QCoreApplication
#
#
# class TabDemo(QTabWidget):
#     def __init__(self, parent=None):
#         super(TabDemo, self).__init__(parent)
#         self.resize(400, 300)
#         self.tab1 = QWidget()
#         self.tab2 = QWidget()
#         self.tab3 = QWidget()
#         self.addTab(self.tab1, "Tab 1")
#         self.addTab(self.tab2, "Tab 2")
#         self.addTab(self.tab3, "Tab 3")
#         self.tab1UI()
#         self.tab2UI()
#         self.tab3UI()
#         self.setWindowTitle("Tab 例子")
#
#     def tab1UI(self):
#         self.layout = QFormLayout()
#         self.layout.addRow("姓名", QLineEdit())
#         self.layout.addRow("地址", QLineEdit())
#         self.setTabText(0, "联系方式") # 也可以在addTab时进行修改
#         self.tab1.setLayout(self.layout)
#         btn = QPushButton('Button_name', self.tab1)
#         btn.resize(btn.sizeHint())  # 默认尺寸
#         btn.move(100, 100)
#         btn.clicked.connect(QCoreApplication.instance().quit)
#         btn.setToolTip('1')
#
#     def tab2UI(self):
#         layout = QFormLayout()
#         sex = QHBoxLayout()
#         sex.addWidget(QRadioButton("男"))
#         sex.addWidget(QRadioButton("女"))
#         layout.addRow(QLabel("性别"), sex)
#         layout.addRow("生日", QLineEdit())
#         self.setTabText(1, "个人详细信息")
#         self.tab2.setLayout(layout)
#
#     def tab3UI(self):
#         layout = QHBoxLayout()
#         layout.addWidget(QLabel("科目"))
#         layout.addWidget(QCheckBox("物理"))
#         layout.addWidget(QCheckBox("高数"))
#         self.setTabText(2, "教育程度")
#         self.tab3.setLayout(layout)
#
#
# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     demo = TabDemo()
#     demo.show()
#     sys.exit(app.exec_())