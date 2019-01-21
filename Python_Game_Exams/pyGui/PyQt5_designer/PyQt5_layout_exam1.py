'''
PyQt的布局方式分为3种，一种是绝对位置布局，缺点是调整窗口大小后，布局会乱
另外有两种盒子布局，一种框布局（QBoxLayout）,一种网格布局（QGridLayout）
'''

## 1 框布局
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QApplication)
from PyQt5.QtCore import Qt
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        okButton = QPushButton("OK")
        cancelButton = QPushButton("Cancel")
        hbox = QHBoxLayout() # 水平（Horizontal）布局
        # hbox.addStretch(1)
        hbox.addWidget(okButton, 0, Qt.AlignLeft|Qt.AlignTop)
        # hbox.addStretch(1)
        hbox.addWidget(cancelButton)
        # hbox.addStretch(1)
        hbox.addWidget(QPushButton('Quit'), 0, Qt.AlignLeft|Qt.AlignTop)
        hbox.setSpacing(10)
        vbox = QVBoxLayout() # 垂直（Vertical）布局
        vbox.addStretch(2) # 如果要查看对齐方式的效果，把这两行注释掉
        vbox.addLayout(hbox)# 垂直布局下嵌套水平布局
        vbox.addStretch(1) # 如果要查看对齐方式的效果，把这两行注释掉
        self.setLayout(hbox)
        self.setGeometry(300, 300, 300, 150)
        self.setWindowTitle('Buttons')
        self.show()
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
