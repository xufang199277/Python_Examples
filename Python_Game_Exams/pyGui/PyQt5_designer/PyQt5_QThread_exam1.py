## 单线程会导致卡死
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
#
# global sec
# sec = 0
# def setTime():
#     global sec
#     sec += 1 # LED显示数字+1
#     lcdNumber.display(sec)
# def work(): # 计时器每秒计数
#     timer.start(100) # 开始一次非常耗时的计算
#     #  这里用一个2 000 000 000次的循环来模拟
#     for i in range(20000000):
#         pass
#     timer.stop()
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     top = QWidget()
#     top.resize(300, 120) # 垂直布局类QVBoxLayout
#     layout = QVBoxLayout(top) # 添加控件
#     lcdNumber = QLCDNumber()
#     layout.addWidget(lcdNumber)
#     button = QPushButton("测试")
#     layout.addWidget(button)
#     top.setLayout(layout)
#     timer = QTimer() # 每次计时结束，触发setTime
#     timer.timeout.connect(setTime) # 连接测试按钮和槽函数work
#     button.clicked.connect(work)
#     top.show()
#     sys.exit(app.exec_())


# ## 多线程
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# global sec
# sec = 0
# # # 增加了一个继承自QThread类的类，重新写了它的run()函数
# # #  run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
# class WorkThread(QThread):
#     trigger = pyqtSignal()
#     def __int__(self):
#         super(WorkThread, self).__init__()
#     def run(self):  # 这个函数不是自定义函数，所以只能用run，不能用run1等
#         for i in range(2000000000):
#             pass
#         # 循环完毕后发出信号
#         self.trigger.emit()
# #
# class WorkThread2(QThread):
#     trigger2 = pyqtSignal()
#     def __init__(self):
#         super(WorkThread2, self).__init__()
#     def run1(self):
#         # for i in range(5):
#         for i in range(200000000):
#             pass
#         self.trigger2.eamit()
# #
# def LCDdisplay_Time():
#     global sec
#     sec += 1 # LED显示数字+1
#     lcdNumber.display(sec)
# def work():
#     # 计时器每秒计数
#     timer.start(1000)
#     # 计时开始
#     workThread.start()
#     workThread2.start()
#     # 当获得循环完毕的信号时，停止计数
#     workThread.trigger.connect(timeStop)
#     workThread2.trigger2.connect(timePause)
# def timeStop():
#     timer.stop()
#     print("运行结束用时", lcdNumber.value())
#     global sec
#     sec = 0
# def timePause():
#     # timer.stop()
#     # print("运行结束用时", lcdNumber.value())
#     # global  sec
#     # sec=100
#     pass
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     top = QWidget()
#     top.resize(300, 120)
#     # 垂直布局类QVBoxLayout
#     layout = QVBoxLayout(top)
#     # 加个显示屏
#     lcdNumber = QLCDNumber()
#     layout.addWidget(lcdNumber)
#     button = QPushButton("测试")
#     layout.addWidget(button)
#     timer = QTimer()
#     workThread = WorkThread()
#     workThread2 = WorkThread2()
#     button.clicked.connect(work)
#     # 每次计时结束，触发 countTime
#     timer.timeout.connect(LCDdisplay_Time)
#     top.show()
#     sys.exit(app.exec_())


## 双线程
# import sys
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# global sec
# sec = 0
# # 增加了一个继承自QThread类的类，重新写了它的run()函数
# #  run()函数即是新线程需要执行的：执行一个循环；发送计算完成的信号。
# class WorkThread(QThread):
#     trigger = pyqtSignal()
#     def __int__(self):
#         super(WorkThread, self).__init__()
#     def run(self):
#         for i in range(200000000):
#             pass
#         # 循环完毕后发出信号
#         self.trigger.emit()
# def countTime():
#     global sec
#     sec += 1
#     # LED显示数字+1
#     lcdNumber.display(sec)
# def work():
#     # 计时器每秒计数
#     timer.start(1000)
#     # 计时开始
#     workThread.start()
#     # 当获得循环完毕的信号时，停止计数
#     workThread.trigger.connect(timeStop)
# def timeStop():
#     timer.stop()
#     print("运行结束用时", lcdNumber.value())
#     global sec
#     sec = 0
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     top = QWidget()
#     top.resize(300, 120)
#     # 垂直布局类QVBoxLayout
#     layout = QVBoxLayout(top)
#     # 加个显示屏
#     lcdNumber = QLCDNumber()
#     layout.addWidget(lcdNumber)
#     button = QPushButton("测试")
#     layout.addWidget(button)
#     timer = QTimer()
#     workThread = WorkThread()
#     button.clicked.connect(work)
#     # 每次计时结束，触发countTime
#     timer.timeout.connect(countTime)
#     top.show()
#     sys.exit(app.exec_())


## 分离界面显示和数据读取
'''
当在窗口中显示的数据比较简单时，可以把读取数据的业务逻辑放在窗口的初始化代码中；
但如果读取数据的时间比较长，比如网络请求数据的时间比较长，则可以把这部分逻辑放
在QThread线程中，实现界面的数据显示和数据读取的分离
'''
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
class Worker(QThread):
    sinOut = pyqtSignal(str) # 自定义信号，执行run()函数时，从相关线程发射此信号
    trigger = pyqtSignal()
    def __init__(self, parent=None):
        super(Worker, self).__init__(parent)
        self.working = True
        self.num = 0
    def __del__(self):
        self.working = False
        self.wait()
    def run(self):
        # while self.working == True:
        for i in range(5):
            self.file_str = 'xufang {0}'.format(self.num) # str.format()
            self.num += 2
            # 发出信号
            self.sinOut.emit(self.file_str)
            # 线程休眠2秒
            self.sleep(3)
        self.trigger.emit()

class MainWidget(QWidget):
    def __init__(self, parent=None):
        super(MainWidget, self).__init__(parent)
        self.setWindowTitle("QThread 例子")
        # 布局管理
        self.listFile = QListWidget()
        self.btnStart = QPushButton('开始')
        layout = QGridLayout(self)
        layout.addWidget(self.listFile, 0, 0, 1, 2)
        layout.addWidget(self.btnStart, 1, 1)
        # 连接开始按钮和槽函数
        self.btnStart.clicked.connect(self.slotStart)
        # 创建新线程，将自定义信号sinOut连接到slotAdd()槽函数
        self.thread = Worker()
        self.thread.sinOut.connect(self.slotAdd)
        self.thread.trigger.connect(self.buttonTrue)
        # 开始按钮按下后使其不可用，启动线程
    def slotStart(self):
        self.btnStart.setEnabled(False)
        self.thread.start()
        # self.finished.setEnabled(True)
    # 在列表控件中动态添加字符串条目
    def slotAdd(self, file1):
        self.listFile.addItem(file1)
    def buttonTrue(self):
        self.btnStart.setEnabled(True)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    demo = MainWidget()
    demo.show()
    sys.exit(app.exec_())



# ## 事件处理
# '''
# 对于执行很耗时的程序来说，由于PyQt需要等待程序执行完毕才能进行下一步，
# 这个过程表现在界面上就是卡顿，而如果需要执行这个耗时程序时不断的刷新界面。
# 那么就可以使用QApplication.processEvents()，那么就可以一边执行耗时程序，一
# 边刷新界面的功能，给人的感觉就是程序运行很流畅，因此QApplicationEvents（）
# 的使用方法就是，在主函数执行耗时操作的地方，加入QApplication.processEvents()
# '''
# import sys,time
# from PyQt5.QtWidgets import QWidget,QPushButton,QApplication,QListWidget,QGridLayout
# class WinForm(QWidget):
#     def __init__(self,parent=None):
#         super(WinForm, self).__init__(parent)
#         #设置标题与布局方式
#         self.setWindowTitle('实时刷新界面的例子')
#         layout=QGridLayout()
#         #实例化列表控件与按钮控件
#         self.listFile=QListWidget()
#         self.btnStart=QPushButton('开始')
#         #添加到布局中指定位置
#         layout.addWidget(self.listFile,0,0,1,2)
#         layout.addWidget(self.btnStart,1,1)
#         #按钮的点击信号触发自定义的函数
#         self.btnStart.clicked.connect(self.slotAdd)
#         self.setLayout(layout)
#     def slotAdd(self):
#         for n in range(10):
#             #获取条目文本
#             str_n='File index{}'.format(n)
#             #添加文本到列表控件中
#             self.listFile.addItem(str_n)
#             #实时刷新界面
#             QApplication.processEvents()
#             #睡眠一秒
#             time.sleep(1)
# if __name__ == '__main__':
#     app=QApplication(sys.argv)
#     win=WinForm()
#     win.show()
#     sys.exit(app.exec_())
#


