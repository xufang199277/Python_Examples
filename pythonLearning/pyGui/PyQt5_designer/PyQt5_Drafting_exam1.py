import sys
from PyQt5.QtWidgets import (QPushButton, QWidget, QLineEdit, QApplication)
class Button(QPushButton):
    def __init__(self, title, parent):
        super().__init__(title, parent)
        self.setAcceptDrops(True)
    def dragEnterEvent(self, a):
    # 重新实现dragEnterEvent()方法，并设置可接受的数据类型（这里是普通文本）
        if a.mimeData().hasFormat('text/plain'):
            a.accept()
        else:
            a.ignore()
    def dropEvent(self, a):
    # 重新实现dropEvent()方法，定义了在drop事件发生时的行为，这里改变了按钮的文字
        self.setText(a.mimeData().text())
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        edit = QLineEdit('', self)
        edit.setDragEnabled(True) # 内置了拖动的操作，只需调用该方法即可
        edit.move(30, 65)
        button = Button("Button", self)
        button.move(190, 65)
        self.setWindowTitle('Simple drag & drop')
        self.setGeometry(300, 300, 300, 150)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    app.exec_()
