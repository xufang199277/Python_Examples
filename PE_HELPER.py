# -*- coding: utf-8 -*-
import sys, os, time
time1 = time.time()
##给任务栏加图标，配合self.setWindowIcon(QIcon(r'D:\Python\PE_Work\PE_HELPER\PE_HELPER_REV43\tb.ico'))使用
import ctypes
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")
import pythoncom
from win32com.client import DispatchEx
import re
import PyQt5
dirname = os.path.dirname(PyQt5.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QVBoxLayout, QHBoxLayout, QLabel, QTableView, QAbstractItemView, \
    QWidget, QDialog, QGridLayout, QPushButton, QApplication, QLineEdit, QTextBrowser, QFileDialog, QTreeWidget, QTreeWidgetItem,\
    QRadioButton, QCheckBox, QAction, QMenu, QShortcut, QComboBox
from PyQt5.QtGui import QIcon,  QStandardItem, QStandardItemModel, QColor, QKeySequence
from PyQt5.QtCore import Qt, QThread, pyqtSignal, QAbstractTableModel
from PyQt5 import QtCore, QtGui
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import itertools
import qdarkstyle
from functools import wraps
import matplotlib as mpl
mpl.use('QT5Agg')
import seaborn as sns


__Author__ = 'Andy Xu'
__Copyright__ = 'Copyright (c) 2019'



class Traceview(QMainWindow):
    simple_mode = 0
    colors_mode = 0

    def __init__(self):
        super(Traceview, self).__init__()
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        # 给窗口左上角加图标
        self.setWindowIcon(QIcon(r'D:\Python\PE_Work\PE_HELPER\PE_HELPER_REV43\tb.ico'))
        #
        self.file_menu = self.menuBar().addMenu('FileName')
        self.testclass_menu = self.menuBar().addMenu('TestClass')
        self.para_menu = self.menuBar().addMenu('Parameter')
        self.CH_menu = self.menuBar().addMenu('CH')
        self.Time_menu = self.menuBar().addMenu('Time')

        self.new_action = QAction('New', self)
        self.open_action = QAction('Open', self)
        self.save_action = QAction('Save', self)
        self.save_as_action = QAction('Save As', self)
        self.close_action = QAction('Close', self)
        self.cut_action = QAction('Cut', self)
        self.copy_action = QAction('Copy', self)
        self.paste_action = QAction('Paste', self)
        self.font_action = QAction('Font', self)
        self.color_action = QAction('Color', self)
        self.about_action = QAction('Qt', self)

        self.menu_init()

        self._main = QWidget()
        self.setCentralWidget(self._main)

        sys.stdout = EmittingStream(textWritten=self.normalOutputWritten)
        sys.stder = EmittingStream(textWritten=self.normalOutputWritten)
        self.resize(1080, 640)
        self.setFixedHeight(640)


        self.setWindowTitle("PE_HELPER")
        self.initUI()
        self._main.label_specfile = QLabel("Specfile")
        self._main.label_specfile.setAlignment(Qt.AlignCenter)
        self._main.label_traceview = QLabel("Traceview")
        self._main.label_traceview.setAlignment(Qt.AlignCenter)
        self._main.label_txtsave = QLabel("Txtsave")
        self._main.label_txtsave.setAlignment(Qt.AlignCenter)
        self._main.label_excelsave = QLabel("Excelsave")
        self._main.label_excelsave.setAlignment(Qt.AlignCenter)
        self._main.label_para = QLabel("Parameter")
        self._main.label_para.setAlignment(Qt.AlignCenter)
        self._main.label_sheet = QLabel("Sheetname")
        self._main.label_sheet.setAlignment(Qt.AlignCenter)
        self._main.edit_specfile = QLineEdit()
        self._main.edit_traceview = QLineEdit()
        self._main.edit_txtsave = QLineEdit()
        self._main.edit_excelsave = QLineEdit()
        self._main.edit_para = QTextEdit()
        self._main.edit_sheet = QLineEdit()
        self._main.tbrowser_log = QTextBrowser()
        self._main.tree_spec = QTreeWidget()
        self._main.button_specfile = QPushButton("open")
        self._main.button_traceview = QPushButton("open")
        self._main.button_txtsave = QPushButton("open")
        self._main.button_excelsave = QPushButton("open")
        self._main.button_testinfo = QRadioButton("R_M")
        self._main.checkBox_savemode = QCheckBox("S_M")
        self._main.checkBox_colormode = QCheckBox("C_M")
        self._main.checkBox_tablemode = QCheckBox("T_M")
        self._main.button_start = QPushButton("提取")
        self._main.button_excel = QPushButton("整理")

        # 创建布局框架
        self._main.label_Vlayout = QVBoxLayout()
        self._main.edit_Vlayout = QVBoxLayout()
        self._main.openbtn_Vlayout = QVBoxLayout()
        self._main.part_Hlayout = QHBoxLayout()
        self._main.para_Glayout = QGridLayout()
        self._main.part_input_Hlayout = QHBoxLayout()
        self._main.output_Glayout = QGridLayout()
        self._main.all_Vlayout = QVBoxLayout()
        self._main.set_Glayout = QGridLayout()
        self._main.all_Hlayout = QHBoxLayout()

        self.part_init()
        self.part_position()
        self.part_qss()
        self.my_thread_0 = MyThread_0()
        self._main.button_start.clicked.connect(lambda: self.thread_fun(1))
        self._main.button_excel.clicked.connect(lambda: self.thread_fun(2))
        self._main.button_specfile.clicked.connect(lambda: self.get_open_file_name(1))
        self._main.button_traceview.clicked.connect(lambda: self.get_open_file_name(2))
        self._main.button_txtsave.clicked.connect(lambda: self.get_open_file_name(3))
        self._main.button_excelsave.clicked.connect(lambda: self.get_open_file_name(4))
        self._main.button_testinfo.clicked.connect(lambda: self.thread_fun(0))
        self._main.checkBox_savemode.stateChanged.connect(self.save_mode)
        self._main.checkBox_tablemode.stateChanged.connect(self.table_mode)
        self._main.checkBox_colormode.stateChanged.connect(self.color_mode)
        # self._main.edit_plot_func.stateChanged.connect(self.save_mode)
        self._main.tree_spec.itemClicked.connect(self.my_thread_0.checklist_change_func)

    def fn_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            t0 = time.time()
            result = function(*args, **kwargs)
            t1 = time.time()
            print("Total time running %s: %s seconds" %
                  (function.func_name, str(t1 - t0))
                  )
            return result
        return function_timer

    ##给程序加启动界面
    def load_worker_finished(self):
        self.load_thread.quit()
        self.load_thread.wait()

    ##给程序加启动界面
    def set_message(self, message):
        self.splash.showMessage(message, 1 | 1, Qt.white)

    # 给菜单加子菜单
    def menu_init(self):
        self.file_menu.addAction(self.new_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addAction(self.save_action)
        self.file_menu.addAction(self.save_as_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.close_action)

        self.testclass_menu.addAction(self.cut_action)
        self.testclass_menu.addAction(self.copy_action)
        self.testclass_menu.addAction(self.paste_action)
        self.testclass_menu.addSeparator()
        self.testclass_menu.addAction(self.font_action)
        self.testclass_menu.addAction(self.color_action)

        self.para_menu.addAction(self.new_action)

        self.CH_menu.addAction(self.about_action)

    def __del__(self):
        # Restore sys.stdout
        sys.stdout = sys.__stdout__
        sys.stderr = sys.__stderr__

    ## 用于重定向输出到文本框
    def normalOutputWritten(self, text):
        cursor = self._main.tbrowser_log.textCursor()
        cursor.movePosition(QtGui.QTextCursor.End)
        cursor.insertText(text)
        self._main.tbrowser_log.setTextCursor(cursor)
        self._main.tbrowser_log.ensureCursorVisible()

    def thread_fun(self, thread_num):
        if thread_num == 0:  ## 分析testclass的线程
            self.my_thread_0.thread_Num = 0
            self.my_thread_0.start()
        elif thread_num == 1:  ## 数据处理线程
            self.my_thread_0.thread_Num = 1
            self.my_thread_0.start()
        elif thread_num == 2:  ## specfile整理线程
            self.my_thread_0.thread_Num = 2
            self.my_thread_0.start()
        else:
            pass

    def initUI(self):
        # 去窗口边框
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setWindowFlags(QtCore.Qt.CustomizeWindowHint)
        pass

    ## 用于窗口任意位置的拖动
    ######################################################################
    def mousePressEvent(self, event):
        try:
            if event.button() == Qt.LeftButton:
                self.m_drag = True
                self.m_DragPosition = event.globalPos() - self.pos()
                event.accept()
        except:
            pass

    def mouseMoveEvent(self, QMouseEvent):
        try:
            if QMouseEvent.buttons() and Qt.LeftButton:
                self.move(QMouseEvent.globalPos() - self.m_DragPosition)
                QMouseEvent.accept()
        except:
            pass

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag = False

    ###########################################################################

    def part_init(self):
        self._main.edit_traceview.setPlaceholderText("请输入Traceview文档存放路径")
        self._main.edit_specfile.setPlaceholderText("请输入Specfile文档存放路径")
        self._main.edit_txtsave.setPlaceholderText("请输入TXT结果存放路径")
        self._main.edit_excelsave.setPlaceholderText("请输入Excel结果存放路径")
        self._main.edit_para.setPlaceholderText(
            "Traceview信息提取功能：\n请输入需要提取的参数名称，以回车键隔开" + '\n' + "Specfile格式整理功能：\n请输入测试温度，以回车键隔开")
        self._main.edit_sheet.setPlaceholderText("请输入Specfile中对应的sheet名称")
        self._main.tree_spec.setHeaderLabels(['Test Information'])
        self._main.tbrowser_log.setPlaceholderText("Note:" + '\n'
                                                             "Please finish all content of inputdialog above" + '\n' +
                                                   "Please prepare specfile and check" + '\n' +
                                                   "Please prepare traceview and check" + '\n' +
                                                   "Please confirm sheet name match the specfile" + '\n' +
                                                   "Please confirm parameter match the traceview" + '\n' +
                                                   "Now you can click the start button and begin to data analysis program")

    def part_position(self):
        self._main.label_traceview.setFixedHeight(35)
        self._main.label_specfile.setFixedHeight(35)
        self._main.label_txtsave.setFixedHeight(35)
        self._main.label_excelsave.setFixedHeight(35)
        self._main.label_sheet.setFixedHeight(35)
        self._main.label_para.setFixedHeight(35)
        self._main.label_traceview.setFixedWidth(102)
        self._main.label_specfile.setFixedWidth(102)
        self._main.label_txtsave.setFixedWidth(102)
        self._main.label_excelsave.setFixedWidth(102)
        self._main.label_sheet.setFixedWidth(102)
        self._main.label_para.setFixedWidth(102)
        self._main.tbrowser_log.setFixedHeight(240)
        self._main.button_traceview.setFixedWidth(80)
        self._main.button_specfile.setFixedWidth(80)
        self._main.button_txtsave.setFixedWidth(80)
        self._main.button_excelsave.setFixedWidth(80)
        self._main.button_testinfo.setFixedWidth(89)
        self._main.checkBox_savemode.setFixedWidth(80)
        self._main.checkBox_tablemode.setFixedWidth(80)
        self._main.checkBox_colormode.setFixedWidth(80)
        self._main.button_traceview.setFixedHeight(30)
        self._main.button_specfile.setFixedHeight(30)
        self._main.button_txtsave.setFixedHeight(30)
        self._main.button_excelsave.setFixedHeight(30)
        self._main.button_testinfo.setFixedHeight(30)
        self._main.checkBox_savemode.setFixedHeight(30)
        self._main.checkBox_tablemode.setFixedHeight(30)
        self._main.checkBox_colormode.setFixedHeight(30)
        self._main.button_start.setFixedWidth(100)
        self._main.button_excel.setFixedWidth(100)
        self._main.button_start.setFixedHeight(40)
        self._main.button_excel.setFixedHeight(40)
        self._main.edit_traceview.setFixedHeight(30)
        self._main.edit_specfile.setFixedHeight(30)
        self._main.edit_txtsave.setFixedHeight(30)
        self._main.edit_excelsave.setFixedHeight(30)
        self._main.edit_sheet.setFixedHeight(30)
        self._main.edit_para.setFixedWidth(150)
        # 添加组件
        self._main.label_Vlayout.addWidget(self._main.label_specfile)
        self._main.label_Vlayout.addSpacing(18)
        self._main.label_Vlayout.addWidget(self._main.label_traceview)
        self._main.label_Vlayout.addSpacing(18)
        self._main.label_Vlayout.addWidget(self._main.label_txtsave)
        self._main.label_Vlayout.addSpacing(18)
        self._main.label_Vlayout.addWidget(self._main.label_excelsave)
        self._main.label_Vlayout.addSpacing(18)
        self._main.label_Vlayout.addWidget(self._main.label_sheet)
        self._main.label_Vlayout.addSpacing(18)
        self._main.label_Vlayout.setAlignment(Qt.AlignTop)

        # 添加组件
        self._main.edit_Vlayout.addSpacing(3)
        self._main.edit_Vlayout.addWidget(self._main.edit_specfile)
        self._main.edit_Vlayout.addSpacing(23)
        self._main.edit_Vlayout.addWidget(self._main.edit_traceview)
        self._main.edit_Vlayout.addSpacing(23)
        self._main.edit_Vlayout.addWidget(self._main.edit_txtsave)
        self._main.edit_Vlayout.addSpacing(23)
        self._main.edit_Vlayout.addWidget(self._main.edit_excelsave)
        self._main.edit_Vlayout.addSpacing(23)
        self._main.edit_Vlayout.addWidget(self._main.edit_sheet)
        self._main.edit_Vlayout.addSpacing(3)
        self._main.edit_Vlayout.setAlignment(Qt.AlignTop)

        # 添加组件
        self._main.openbtn_Vlayout.addSpacing(3)
        self._main.openbtn_Vlayout.addWidget(self._main.button_specfile)
        self._main.openbtn_Vlayout.addSpacing(23)
        self._main.openbtn_Vlayout.addWidget(self._main.button_traceview)
        self._main.openbtn_Vlayout.addSpacing(23)
        self._main.openbtn_Vlayout.addWidget(self._main.button_txtsave)
        self._main.openbtn_Vlayout.addSpacing(23)
        self._main.openbtn_Vlayout.addWidget(self._main.button_excelsave)
        self._main.openbtn_Vlayout.addSpacing(23)
        self._main.openbtn_Vlayout.addWidget(self._main.button_testinfo)
        self._main.openbtn_Vlayout.addSpacing(3)
        self._main.openbtn_Vlayout.setAlignment(Qt.AlignTop)

        # 添加组件
        self._main.part_Hlayout.addLayout(self._main.label_Vlayout)
        self._main.part_Hlayout.addLayout(self._main.edit_Vlayout)
        self._main.part_Hlayout.addLayout(self._main.openbtn_Vlayout)
        self._main.part_Hlayout.setStretch(0, 1)
        self._main.part_Hlayout.setStretch(1, 4)
        self._main.part_Hlayout.setStretch(2, 1)

        # 添加组件
        self._main.para_Glayout.addWidget(self._main.label_para, 0, 0, 1, 1)
        self._main.para_Glayout.addWidget(self._main.edit_para, 1, 0, 5, 2)

        # 添加组件
        self._main.part_input_Hlayout.addLayout(self._main.part_Hlayout)
        self._main.part_input_Hlayout.addSpacing(10)
        self._main.part_input_Hlayout.addLayout(self._main.para_Glayout)

        self._main.output_Glayout.addWidget(self._main.tbrowser_log, 0, 0, 3, 4)
        self._main.output_Glayout.addWidget(self._main.button_start, 3, 1, 1, 1)
        self._main.output_Glayout.setHorizontalSpacing(40)
        self._main.output_Glayout.setVerticalSpacing(10)
        self._main.output_Glayout.addWidget(self._main.button_excel, 3, 2, 1, 1)

        self._main.set_Glayout.addWidget(self._main.checkBox_savemode, 0, 0, 1, 1)
        self._main.set_Glayout.addWidget(self._main.checkBox_colormode, 0, 1, 1, 1)
        self._main.set_Glayout.addWidget(self._main.checkBox_tablemode, 0, 2, 1, 1)
        self._main.set_Glayout.addWidget(self._main.tree_spec, 1, 0, 5, 3)

        self._main.all_Vlayout.addLayout(self._main.part_input_Hlayout)
        self._main.all_Vlayout.addLayout(self._main.output_Glayout)

        self._main.all_Hlayout.addLayout(self._main.all_Vlayout)
        self._main.all_Hlayout.addSpacing(10)
        self._main.all_Hlayout.addLayout(self._main.set_Glayout)

        self._main.setLayout(self._main.all_Hlayout)

    def part_qss(self):
        self.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
        label_qss = 'font:22px;background-color:#505F69;font-family:Times New Roman;color:white;border: 1px solid black;border-radius: 3px'
        tbrowser_log_qss = 'QTextBrowser{font:23px;font-family:Times New Roman;;color:white;border: 1px solid White;border-radius: 3px}' \
                           'QTextBrowser:hover{font:23px;font-family:Times New Roman;;color:white;border: 1px solid #D990FB;border-radius: 3px}'
        edit_para_qss = 'QTextEdit{font:19px;font-family:SimSun;color:#FFFFFF;border: 1px solid White;;border-radius: 2px}' \
                        'QTextEdit:hover{font:19px;font-family:SimSun;color:#FFFFFF;border: 1px solid #D990FB;;border-radius: 2px}'
        edit_line_qss = 'QLineEdit{font:19px;font-family:SimSun;color:#FFFFFF;border: 1px solid White;;border-radius: 2px}' \
                        'QLineEdit:hover{font:19px;font-family:SimSun;color:#FFFFFF;border: 1px solid #D990FB;;border-radius: 2px}'
        button_qss = 'QPushButton{font:26px;background-color:#5F9DC2;font-family:SimSun;color:#FFFFFF;border-radius: 2px;border-bottom:2px outset #000010;border-right:2px outset #000020}' \
                     'QPushButton:hover{font:26px;background-color:#5F9DC2;font-family:SimSun;color:#FFFFFF;border-radius: 2px;border:1px outset #FCFCFC}' \
                     'QPushButton:pressed{font:26px;background-color:#5F9DC2;font-family:SimSun;color:#FFFFFF;border-radius: 2px;border-left:2px outset #000010;border-top:2px outset #000020}'
        button_open_qss = 'QPushButton{text-align:bottom;font:25px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-bottom:2px outset #000010;border-right:2px outset #000010}' \
                          'QPushButton:hover{font:25px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border:1px outset #FCFCFC}' \
                          'QPushButton:pressed{font:25px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-left:2px outset #000010;border-top:2px outset #000010}'
        button_mode_qss = 'QRadioButton{font:22px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-bottom:2px outset #000010;border-right:2px outset #000010}' \
                          'QRadioButton:hover{font:22px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border:1px outset #FCFCFC}' \
                          'QRadioButton:pressed{font:22px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-left:2px outset #000010;border-top:2px outset #000010}'
        checkBox_mode_qss = 'QCheckBox{font:21px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;}' \
                            'QCheckBox:hover{font:21px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border:1px outset #FCFCFC}' \
                            'QCheckBox:pressed{font:21px;background-color:#5F9DC2;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-left:2px outset #000010;border-top:2px outset #000010}'
        self._main.label_traceview.setStyleSheet(label_qss)
        self._main.label_specfile.setStyleSheet(label_qss)
        self._main.label_txtsave.setStyleSheet(label_qss)
        self._main.label_excelsave.setStyleSheet(label_qss)
        self._main.label_para.setStyleSheet(label_qss)
        self._main.label_sheet.setStyleSheet(label_qss)
        self._main.tbrowser_log.setStyleSheet(tbrowser_log_qss)
        self._main.edit_para.setStyleSheet(edit_para_qss)
        self._main.edit_traceview.setStyleSheet(edit_line_qss)
        self._main.edit_specfile.setStyleSheet(edit_line_qss)
        self._main.edit_sheet.setStyleSheet(edit_line_qss)
        self._main.edit_txtsave.setStyleSheet(edit_line_qss)
        self._main.edit_excelsave.setStyleSheet(edit_line_qss)
        self._main.button_traceview.setStyleSheet(button_open_qss)
        self._main.button_specfile.setStyleSheet(button_open_qss)
        self._main.button_excelsave.setStyleSheet(button_open_qss)
        self._main.button_testinfo.setStyleSheet(button_mode_qss)
        self._main.checkBox_savemode.setStyleSheet(checkBox_mode_qss)
        self._main.checkBox_tablemode.setStyleSheet(checkBox_mode_qss)
        self._main.checkBox_colormode.setStyleSheet(checkBox_mode_qss)
        self._main.button_txtsave.setStyleSheet(button_open_qss)
        self._main.button_start.setStyleSheet(button_qss)
        self._main.button_excel.setStyleSheet(button_qss)

    def save_mode(self):
        if self._main.checkBox_savemode.isChecked() is True:
            print("Choose excel file save mode: filename horizontal")
            Traceview.simple_mode = 1
        else:
            print("Choose excel file save mode: filename Vertical")
            Traceview.simple_mode = 0

    def table_mode(self):
        if self._main.checkBox_tablemode.isChecked() is True:
            print("result show in table")
            self.Mywin1 = TableWin()
            self.Mywin1.show()
        else:
            print("close table result")
            self.Mywin1.close()

    def color_mode(self):
        if self._main.checkBox_colormode.isChecked() is True:
            print("Choose excel file color mode: No color")
            Traceview.colors_mode = 1
        else:
            print("Choose excel file color mode: Color")
            Traceview.colors_mode = 0

    def get_open_file_name(self, editnum):
        path_filedir = QFileDialog.getExistingDirectory(self, '选择文件夹', './')
        if editnum == 1:
            self._main.edit_specfile.setText(str(path_filedir.replace("/", "\\")))
        elif editnum == 2:
            self._main.edit_traceview.setText(str(path_filedir.replace("/", "\\")))
        elif editnum == 3:
            self._main.edit_txtsave.setText(str(path_filedir.replace("/", "\\")))
        elif editnum == 4:
            self._main.edit_excelsave.setText(str(path_filedir.replace("/", "\\")))
        else:
            pass


class EmittingStream(QtCore.QObject):
    textWritten = QtCore.pyqtSignal(str)

    def write(self, text):
        self.textWritten.emit(str(text))

    def flush(self):
        pass


class MyThread_0(QThread):
    my_signal_0 = pyqtSignal(str)
    fun_mode = 1
    pos_er = 0
    run_mode = 0
    column = 0
    use_define_range = 0
    checklist_sheet = []
    checklist_all_item = []
    sheet_checklist_all_para = []
    path_para_input_vmin = []
    path_para_input_vmax = []
    result_useinfo_allfile = []
    list_cH_para_allfile = []
    list_testclassname_allfile = []
    list_allfilename = []
    path_para = []
    path_txtsave_image = ''

    def __init__(self):
        super(MyThread_0, self).__init__()
        self.thread_Num = 0

    def run(self):
        if self.thread_Num == 0:
            MyThread_0.fun_mode = 1
            self.test_info()
            self.my_signal_0.emit(str(0))
        elif self.thread_Num == 1:
            MyThread_0.fun_mode = 0
            self.start_dataprocess()
            self.my_signal_0.emit(str(1))
        elif self.thread_Num == 2:
            MyThread_0.fun_mode = 1
            self.excel_process()
            self.my_signal_0.emit(str(2))
        elif self.thread_Num == 3:
            pass
        else:
            pass

    def fn_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            t0 = time.time()
            result = function(*args, **kwargs)
            t1 = time.time()
            print("Total time running %s: %s seconds" %
                  (function.func_name, str(t1 - t0))
                  )
            return result
        return function_timer

    def test_info(self):
        MyThread_0.pos_er = 0
        if demo._main.button_testinfo.isChecked() is True:
            MyThread_0.run_mode = 1
            print("choose run mode: partial analysis ")
            list_sheet_all_para_measure = []
            path_specfile = demo._main.edit_specfile.text()
            if path_specfile.strip() == '':
                MyThread_0.pos_er = 1
                print('please check input information, somewhere input null' + '\n')
                return
            else:
                try:
                    path_xlsxfile = ''.join(self.xlstoxlsx(path_specfile)[0])
                    print('Get testclass information from specfile, please wait...')
                    pythoncom.CoInitialize()
                    excel_testinfo = DispatchEx('excel.application')
                    excel_testinfo.Visible = 0
                    excel_testinfo.DisplayAlerts = False
                    # excel.DisplayAlerts = 0  # 关闭系统警告
                    excel_testinfo.ScreenUpdating = 0  # 关闭屏幕刷新
                    wb_spec = excel_testinfo.Workbooks.Open(path_xlsxfile)
                except:
                    MyThread_0.pos_er = 1
                    print('please check specfile in: ' + path_specfile + '\n')
                    try:
                        excel_testinfo.Application.Quit()
                        pythoncom.CoUninitialize()
                        return
                    except:
                        print('Can not close excel application')
                        return
                sheet_edit = demo._main.edit_sheet.text().strip()
                if not sheet_edit:
                    sheet_count = wb_spec.Worksheets.Count
                    for sheet_id in range(sheet_count):
                        sheet_id = sheet_id + 1
                        sheetname = wb_spec.Worksheets(sheet_id).Name
                        itemlist = []
                        pos_itemlist = []
                        list_all_para_measure = []
                        pos_testname = 4
                        pos_measure = 1
                        sheet_ignore = 0
                        # del_item = 0
                        try:
                            ws_spec = wb_spec.Worksheets(sheet_id)
                        except:
                            MyThread_0.pos_er = 1
                            excel_testinfo.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('please check your Sheet parameter see if it match specfile' + '\n')
                            return
                        try:
                            maxrow_spec, maxcol_spec = self.getRowsClosNum(ws_spec, index = 1)
                        except:
                            MyThread_0.pos_er = 1
                            excel_testinfo.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Can not get the maxrow and maxcol of specfile sheet' + '\n')
                            return
                        for col, cell_value in enumerate(ws_spec.Range(ws_spec.Cells(3,1), ws_spec.Cells(3,maxcol_spec + 1)).Value[0]):
                            if not cell_value:
                                pass
                            else:
                                if 'Measurement Parameter' in str(cell_value):
                                    pos_measure = col + 1
                                    sheet_ignore = 0
                                    break
                                else:
                                    sheet_ignore = 1
                        if sheet_ignore == 1:
                            pass
                        else:
                            try:
                                if maxrow_spec == 5:
                                    pos_testname = pos_testname + 1
                                    cell_value = ws_spec.Cells(5, 1).Value
                                    if not cell_value:
                                        pass
                                    else:
                                        itemlist.append(cell_value)
                                        pos_itemlist.append(pos_testname)
                                else:
                                    for row in ws_spec.Range(ws_spec.Cells(5, 1), ws_spec.Cells(maxrow_spec, 1)).Value:
                                        cell_value = row[0]
                                        pos_testname = pos_testname + 1
                                        if not cell_value:
                                            pass
                                        else:
                                            itemlist.append(cell_value)
                                            pos_itemlist.append(pos_testname)
                                cell_value_list = ws_spec.Range(ws_spec.Cells(pos_itemlist[0], pos_measure), ws_spec.Cells(maxrow_spec, pos_measure)).Value
                                for k in range(len(pos_itemlist)):
                                    list_para_measure = []
                                    if k == len(pos_itemlist)-1:
                                        for row in cell_value_list[(pos_itemlist[k]-pos_itemlist[0]):(maxrow_spec-pos_itemlist[0]+1)]:
                                            cell_value = row[0]
                                            if not cell_value:
                                                pass
                                            else:
                                                list_para_measure.append(cell_value)
                                    else:
                                        for row in cell_value_list[(pos_itemlist[k]-pos_itemlist[0]):(pos_itemlist[k+1]-pos_itemlist[0])]:
                                            cell_value = row[0]
                                            if not cell_value:
                                                pass
                                            else:
                                                list_para_measure.append(cell_value)

                                    ## 使用注释掉的语句可以屏蔽掉没有measurement parameter的test class
                                    # if list_para_measure == []:
                                    #     itemlist.pop(k - del_item)
                                    #     del_item = del_item + 1
                                    # else:
                                    #     list_all_para_measure.append(list_para_measure)
                                    list_all_para_measure.append(list_para_measure)
                                if list_all_para_measure == []:
                                    pass
                                else:
                                    list_sheet_all_para_measure.append([sheetname, itemlist,list_all_para_measure])
                            except:
                                MyThread_0.pos_er = 1
                                excel_testinfo.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('Error to extract test class name' + '\n')
                                pass
                else:
                    sheet_edit_list = sheet_edit.split(';')
                    for sheet in sheet_edit_list:
                        if sheet.strip():
                            itemlist = []
                            pos_itemlist = []
                            list_all_para_measure = []
                            pos_testname = 4
                            pos_measure = 1
                            sheet_ignore = 0
                            # del_item = 0
                            try:
                                sheet = int(sheet)
                            except:
                                pass
                            try:
                                ws_spec = wb_spec.Worksheets(sheet)
                            except:
                                MyThread_0.pos_er = 1
                                excel_testinfo.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('please check your Sheet parameter see if it match specfile' + '\n')
                                return
                            try:
                                maxrow_spec, maxcol_spec = self.getRowsClosNum(ws_spec, index=1)
                            except:
                                MyThread_0.pos_er = 1
                                excel_testinfo.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('Can not get the maxrow and maxcol of specfile sheet' + '\n')
                                return
                            for col, cell_value in enumerate(
                                    ws_spec.Range(ws_spec.Cells(3, 1), ws_spec.Cells(3, maxcol_spec + 1)).Value[0]):
                                if not cell_value:
                                    pass
                                else:
                                    if 'Measurement Parameter' in str(cell_value):
                                        pos_measure = col + 1
                                        sheet_ignore = 0
                                        break
                                    else:
                                        sheet_ignore = 1
                            if sheet_ignore == 1:
                                pass
                            else:
                                try:
                                    if maxrow_spec == 5:
                                        pos_testname = pos_testname + 1
                                        cell_value = ws_spec.Cells(5, 1).Value
                                        if not cell_value:
                                            pass
                                        else:
                                            itemlist.append(cell_value)
                                            pos_itemlist.append(pos_testname)
                                    else:
                                        for row in ws_spec.Range(ws_spec.Cells(5, 1), ws_spec.Cells(maxrow_spec, 1)).Value:
                                            cell_value = row[0]
                                            pos_testname = pos_testname + 1
                                            if not cell_value:
                                                pass
                                            else:
                                                itemlist.append(cell_value)
                                                pos_itemlist.append(pos_testname)
                                    cell_value_list = ws_spec.Range(ws_spec.Cells(pos_itemlist[0], pos_measure),
                                                                    ws_spec.Cells(maxrow_spec, pos_measure)).Value
                                    for k in range(len(pos_itemlist)):
                                        list_para_measure = []
                                        if k == len(pos_itemlist) - 1:
                                            for row in cell_value_list[(pos_itemlist[k] - pos_itemlist[0]):(
                                                    maxrow_spec - pos_itemlist[0] + 1)]:
                                                cell_value = row[0]
                                                if not cell_value:
                                                    pass
                                                else:
                                                    list_para_measure.append(cell_value)
                                        else:
                                            for row in cell_value_list[(pos_itemlist[k] - pos_itemlist[0]):(
                                                    pos_itemlist[k + 1] - pos_itemlist[0])]:
                                                cell_value = row[0]
                                                if not cell_value:
                                                    pass
                                                else:
                                                    list_para_measure.append(cell_value)

                                        ## 使用注释掉的语句可以屏蔽掉没有measurement parameter的test class
                                        # if list_para_measure == []:
                                        #     itemlist.pop(k - del_item)
                                        #     del_item = del_item + 1
                                        # else:
                                        #     list_all_para_measure.append(list_para_measure)
                                        list_all_para_measure.append(list_para_measure)
                                    if list_all_para_measure == []:
                                        pass
                                    else:
                                        sheetname = wb_spec.Worksheets(sheet).Name
                                        list_sheet_all_para_measure.append([sheetname, itemlist, list_all_para_measure])
                                except:
                                    MyThread_0.pos_er = 1
                                    excel_testinfo.Application.Quit()
                                    pythoncom.CoUninitialize()
                                    print('Error to extract test class name' + '\n')
                                    pass
                        else:pass
                wb_spec.Close()
                excel_testinfo.Application.Quit()
                pythoncom.CoUninitialize()
            MyThread_0.checklist_sheet = []
            MyThread_0.checklist_all_item = []
            MyThread_0.sheet_checklist_all_para = []
            for i, sheet in enumerate(list_sheet_all_para_measure):
                item1 = QTreeWidgetItem(demo._main.tree_spec)
                item1.setText(0, str(sheet[0]))
                item1.setCheckState(0, Qt.Unchecked)
                MyThread_0.checklist_sheet.append(item1)
                checklist_item = []
                checklist_all_para = []
                for j, item in enumerate(list_sheet_all_para_measure[i][1]):
                    item2 = QTreeWidgetItem(item1)
                    item2.setText(0, str(item))
                    item2.setCheckState(0, Qt.Unchecked)
                    checklist_item.append(item2)
                    checklist_para = []
                    for k, para_measure in enumerate(list_sheet_all_para_measure[i][2][j]):
                        item3 = QTreeWidgetItem(item2)
                        item3.setText(0, str(para_measure))
                        item3.setCheckState(0, Qt.Unchecked)
                        checklist_para.append(item3)
                    checklist_all_para.append(checklist_para)
                MyThread_0.checklist_all_item.append(checklist_item)
                MyThread_0.sheet_checklist_all_para.append(checklist_all_para)
            print('Get testclass successful')
        else:
            MyThread_0.run_mode = 0
            print("choose run mode: global analysis ")
            demo._main.tree_spec.clear()
            pass

    def checklist_change_func(self, item, column):
        MyThread_0.column = column
        para_null = []
        if item in MyThread_0.checklist_sheet:
            if item.checkState(0) == Qt.Checked:
                demo._main.edit_sheet.setText(item.text(MyThread_0.column))
                print("Choose sheet: ", item.text(MyThread_0.column))
                [x.setCheckState(0, Qt.Checked) for x in
                 MyThread_0.checklist_all_item[MyThread_0.checklist_sheet.index(item)]]
                for x in MyThread_0.sheet_checklist_all_para[MyThread_0.checklist_sheet.index(item)]:
                    para_null.extend(x)
                for x in para_null:
                    x.setCheckState(0, Qt.Checked)
                    demo._main.edit_para.append(x.text(MyThread_0.column))
            else:
                if item.text(MyThread_0.column) in list(demo._main.edit_sheet.text().split(" ")):
                    print("Remove sheet: ", item.text(MyThread_0.column))
                    list1 = list(demo._main.edit_sheet.text().split(" "))
                    s = 1
                    while (s):
                        list1.remove(item.text(MyThread_0.column))
                        demo._main.edit_sheet.setText(' '.join(list1))
                        if item.text(MyThread_0.column) in list(demo._main.edit_sheet.text().split(" ")):
                            pass
                        else:
                            s = 0
                [x.setCheckState(0, Qt.Unchecked) for x in
                 MyThread_0.checklist_all_item[MyThread_0.checklist_sheet.index(item)]]
                for x in MyThread_0.sheet_checklist_all_para[MyThread_0.checklist_sheet.index(item)]:
                    para_null.extend(x)
                for x in para_null:
                    x.setCheckState(0, Qt.Unchecked)
                    if x.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                        list1 = list(demo._main.edit_para.toPlainText().split("\n"))
                        s = 1
                        while (s):
                            list1.remove(x.text(MyThread_0.column))
                            demo._main.edit_para.setText('\n'.join(list1))
                            if x.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                pass
                            else:
                                s = 0
        else:
            for i, check_item in enumerate(MyThread_0.checklist_all_item):
                if item in check_item:
                    if item.checkState(0) == Qt.Checked:
                        print("Choose testclass: ", item.text(MyThread_0.column))
                        [x.setCheckState(0, Qt.Checked) for x in
                         MyThread_0.sheet_checklist_all_para[i][check_item.index(item)]]
                        for x in MyThread_0.sheet_checklist_all_para[i][check_item.index(item)]:
                            if x.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                pass
                            else:
                                demo._main.edit_para.append(x.text(MyThread_0.column))

                        state_item_to_check_all = 0
                        for item_to_check_all in check_item:
                            if item_to_check_all.checkState(0) == Qt.Checked:
                                state_item_to_check_all = state_item_to_check_all + 1
                            else:
                                pass
                        if state_item_to_check_all == len(check_item):
                            MyThread_0.checklist_sheet[i].setCheckState(0, Qt.Checked)
                        else:
                            MyThread_0.checklist_sheet[i].setCheckState(0, Qt.Unchecked)
                    else:
                        print("Remove testclass: ", item.text(MyThread_0.column))
                        [x.setCheckState(0, Qt.Unchecked) for x in
                         MyThread_0.sheet_checklist_all_para[i][check_item.index(item)]]
                        for x in MyThread_0.sheet_checklist_all_para[i][check_item.index(item)]:
                            if x.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                list1 = list(demo._main.edit_para.toPlainText().split("\n"))
                                s = 1
                                while (s):
                                    list1.remove(x.text(MyThread_0.column))
                                    demo._main.edit_para.setText('\n'.join(list1))
                                    if x.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                        pass
                                    else:
                                        s = 0
                                demo._main.edit_para.setText('\n'.join(list1))
                            else:
                                pass
                        state_item_to_check_all = 0
                        for item_to_check_all in check_item:
                            if item_to_check_all.checkState(0) == Qt.Checked:
                                state_item_to_check_all = state_item_to_check_all + 1
                            else:
                                pass
                        if state_item_to_check_all == len(check_item):
                            MyThread_0.checklist_sheet[i].setCheckState(0, Qt.Checked)
                        else:
                            MyThread_0.checklist_sheet[i].setCheckState(0, Qt.Unchecked)
                else:
                    pass
            for j, check_sheet_para in enumerate(MyThread_0.sheet_checklist_all_para):
                for k, check_item_para in enumerate(check_sheet_para):
                    if item in check_item_para:
                        if item.checkState(0) == Qt.Checked:
                            print("Choose parameter: ", item.text(MyThread_0.column))
                            if item.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                pass
                            else:
                                demo._main.edit_para.append(item.text(MyThread_0.column))
                            state_para_to_check_all = 0
                            for para_to_check_all in check_item_para:
                                if para_to_check_all.checkState(0) == Qt.Checked:
                                    state_para_to_check_all = state_para_to_check_all + 1
                                else:
                                    pass
                            if state_para_to_check_all == len(check_item_para):
                                MyThread_0.checklist_all_item[j][k].setCheckState(0, Qt.Checked)
                            else:
                                MyThread_0.checklist_all_item[j][k].setCheckState(0, Qt.Unchecked)
                        else:
                            print("Remove parameter: ", item.text(MyThread_0.column))
                            if item.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                list1 = list(demo._main.edit_para.toPlainText().split("\n"))
                                s = 1
                                while (s):
                                    list1.remove(item.text(MyThread_0.column))
                                    demo._main.edit_para.setText('\n'.join(list1))
                                    if item.text(MyThread_0.column) in list(demo._main.edit_para.toPlainText().split("\n")):
                                        pass
                                    else:
                                        s = 0
                                demo._main.edit_para.setText('\n'.join(list1))
                            else:
                                pass
                            state_para_to_check_all = 0
                            for para_to_check_all in check_item_para:
                                if para_to_check_all.checkState(0) == Qt.Checked:
                                    state_para_to_check_all = state_para_to_check_all + 1
                                else:
                                    pass
                            if state_para_to_check_all == len(check_item_para):
                                MyThread_0.checklist_all_item[j][k].setCheckState(0, Qt.Checked)
                            else:
                                MyThread_0.checklist_all_item[j][k].setCheckState(0, Qt.Unchecked)

                        state_all_item_check = 0
                        for all_item_check in MyThread_0.checklist_all_item[j]:
                            if all_item_check.checkState(0) == Qt.Checked:
                                state_all_item_check = state_all_item_check + 1
                            else:
                                pass
                        if state_all_item_check == len(MyThread_0.checklist_all_item[j]):
                            MyThread_0.checklist_sheet[j].setCheckState(0, Qt.Checked)
                        else:
                            MyThread_0.checklist_sheet[j].setCheckState(0, Qt.Unchecked)
                    else:
                        pass
                    
    def start_dataprocess(self):
        MyThread_0.pos_er = 0
        timestart = time.time()
        print('The begining of data process procedure' + '\n')
        self.path_txtsave, self.path_specfile, self.path_traceview, self.path_excelsave,\
                MyThread_0.path_para, self.path_sheet = self.callback_input()
        if MyThread_0.run_mode == 0 and (self.path_specfile.strip() == '' or self.path_traceview.strip() == '' or self.path_sheet.strip() == '' or MyThread_0.path_para == []):
            MyThread_0.pos_er = 1
            print('please check input information, somewhere input null1' + '\n')
            return
        elif MyThread_0.run_mode == 1 and (self.path_specfile.strip() == '' or self.path_traceview.strip() == ''):
            MyThread_0.pos_er = 1
            print('please check input information, somewhere input null2' + '\n')
            return
        else:
            MyThread_0.result_useinfo_allfile, MyThread_0.list_cH_para_allfile, MyThread_0.list_testclassname_allfile, MyThread_0.list_allfilename, paralist, self.vmin_para_allfile, self.vmax_para_allfile = \
                self.info_extract_process(self.path_txtsave, self.path_specfile,
                                          self.path_traceview, MyThread_0.path_para, self.path_sheet)
            if MyThread_0.pos_er == 1:
                return
            else:
                pass
            if MyThread_0.run_mode == 0:
                pass
            else:
                if MyThread_0.path_para == []:
                    MyThread_0.path_para = paralist
                else:
                    pass
            self.value_write_excel(self.path_excelsave, MyThread_0.result_useinfo_allfile, MyThread_0.list_cH_para_allfile,
                                   MyThread_0.list_testclassname_allfile, MyThread_0.path_para, MyThread_0.list_allfilename, self.vmin_para_allfile, self.vmax_para_allfile)
            if MyThread_0.pos_er == 1:
                return
            else:
                pass
        timeend = time.time()
        if MyThread_0.pos_er == 0:
            print('The end of data process procedure, successful' + '\n')
            print('Path to save txt file: ' + self.path_txtsave + '\n')
            print('Path to save excel file: ' + self.path_excelsave + '\n')
        elif MyThread_0.pos_er == 1:
            print('The end of data process procedure, Fail' + '\n')
        else:
            pass
        print('Total time for data process: ' + str(timeend - timestart) + 's')
    
    def info_extract_process(self, path_txtsave, path_specfile, path_traceview, path_para, path_sheet):
        itemlist = []
        paralist = []
        if MyThread_0.run_mode == 0:
            try:
                path_xlsxfile = ''.join(self.xlstoxlsx(path_specfile))
                pythoncom.CoInitialize()
                excel_extract = DispatchEx('excel.application')
                excel_extract.Visible = 0
                excel_extract.DisplayAlerts = False
                # excel.DisplayAlerts = 0  # 关闭系统警告
                excel_extract.ScreenUpdating = 0  # 关闭屏幕刷新
                wb_spec = excel_extract.Workbooks.Open(path_xlsxfile)
            except:
                MyThread_0.pos_er = 1
                print('please check specfile in: ' + path_specfile + '\n')
                return None, None, None, None, None, None, None

            try:
                ws_spec = wb_spec.Worksheets(path_sheet)
            except:
                MyThread_0.pos_er = 1
                print('please check your Sheet parameter see if it match specfile' + '\n')
                return None, None, None, None, None, None, None
            try:
                maxrow_spec, maxcol_spec = self.getRowsClosNum(ws_spec, index=1)
            except:
                MyThread_0.pos_er = 1
                print('Can not get the maxrow and maxcol of specfile sheet' + '\n')
                return None, None, None, None, None, None, None

            try:
                if maxrow_spec == 5:
                    cell_value = ws_spec.Cells(5, 1).Value
                else:
                    for row in ws_spec.Range(ws_spec.Cells(5, 1), ws_spec.Cells(maxrow_spec, 1)).Value:
                        for cell_value in row:
                            if not cell_value:
                                pass
                            else:
                                itemlist.append(cell_value)
                wb_spec.Close()
                excel_extract.Application.Quit()
                pythoncom.CoUninitialize()
            except:
                MyThread_0.pos_er = 1
                print('Error in get testclass name' + '\n')
                pass
            self.list_para_re = self.para_re(path_para)
        else:
            sheetlist, itemlist, paralist = self.para_check_state()
            if path_para == []:
                self.list_para_re = self.para_re(paralist)
            else:
                self.list_para_re = self.para_re(path_para)

        self.name_testclass = self.listaddstr(itemlist, r'Testing ')
        if self.name_testclass == []:
            MyThread_0.pos_er = 1
            print('please check the test class from specfile, No test class' + '\n')
            return None, None, None, None, None, None, None
        else:
            pass

        if self.list_para_re == []:
            MyThread_0.pos_er = 1
            print('please check the input parameter, you can not input nothing' + '\n')
            return None, None, None, None, None, None, None
        else:
            pass

        try:
            self.txtfile_write = open(path_txtsave + r'\useful_info_save.txt', 'a')
        except:
            MyThread_0.pos_er = 1
            print('please check the path to save txt file of result' + '\n')
            return None, None, None, None, None, None, None

        # File-by-file analysis
        #
        self.result_useinfo_allfile_save = []
        self.list_cH_para_allfile_save = []
        self.list_testclassname_allfile_save = []
        self.list_fliename = []
        self.vmin_para_allfile_save = []
        self.vmax_para_allfile_save = []
        try:
            if not os.listdir(path_traceview):
                MyThread_0.pos_er = 1
                print('No traceview file in folder, please check' + '\n')
                return None, None, None, None, None, None, None
            else:
                pass

            for info in os.listdir(path_traceview):
                # obtain full path name of every files
                if info.endswith('.txt'):
                    print('Start working on traceview: ' + info + '\n')
                    pre_path = os.path.abspath(path_traceview)
                    info1 = os.path.join(pre_path, info)
                    self.list_fliename.append(info.strip())
                    filetoread = open(info1, mode='r')
                    testitem_txt = filetoread.read()
                    #
                    # write file name to document
                    self.txtfile_write.write(info1 + '\n')
                    # Key parameter we need to extract
                    # list[0] is the regular expression format of parameter and list[1] is the parameter name
                    #
                    # Parameter-by-parameter extraction
                    self.result_useinfo_singlefile_save = []
                    self.list_cH_singlefile = []
                    self.list_testclassname_singlefile = []
                    self.vmin_para_singlefile = []
                    self.vmax_para_singlefile = []
                    for list in self.list_para_re:
                        self.txtfile_write.write("KEY_PARAMETER: " + list[1] + '\n')
                        try:
                            # QApplication.processEvents()
                            self.result_useinfo_para_save, self.list_cH_para, self.list_testclassname_para, self.vmin_para, self.vmax_para = self.Txtreadlinesfunc(self.txtfile_write, testitem_txt,
                                                    self.name_testclass, list[0], list[1])
                        except:
                            MyThread_0.pos_er = 1
                            print('Fail to get data from traceview: ' + info)
                            print('Fail to get data of parameter: ' + list[1] + '\n')
                            return None, None, None, None, None, None, None
                        self.result_useinfo_singlefile_save.append(self.result_useinfo_para_save)
                        self.list_cH_singlefile.append(self.list_cH_para)
                        self.list_testclassname_singlefile.append(self.list_testclassname_para)
                        # if self.vmin_para == []:
                        #     vmin_count = []
                        # else:
                        #     vmin_count = [max(self.vmin_para, key=self.vmin_para.count)]
                        # if self.vmax_para == []:
                        #     vmax_count = []
                        # else:
                        #     vmax_count = [max(self.vmax_para, key=self.vmax_para.count)]
                        self.vmin_para_singlefile.append(self.vmin_para)
                        self.vmax_para_singlefile.append(self.vmax_para)
                    print('Finish process traceview: ' + info + '\n')
                    try:
                        filetoread.close()
                    except:
                        MyThread_0.pos_er = 1
                        print('Fail to close the reading process of traceview: ' + info + '\n')
                        return None, None, None, None, None, None, None
                    self.result_useinfo_allfile_save.append(self.result_useinfo_singlefile_save)
                    self.list_cH_para_allfile_save.append(self.list_cH_singlefile)
                    self.list_testclassname_allfile_save.append(self.list_testclassname_singlefile)
                    self.vmin_para_allfile_save.append(self.vmin_para_singlefile)
                    self.vmax_para_allfile_save.append(self.vmax_para_singlefile)
                else:
                    pass
        except:
            MyThread_0.pos_er = 1
            print('Fail to process traceview file' + '\n')
            return None, None, None, None, None, None, None
        # txt file write complete
        if MyThread_0.pos_er == 0:
            print('Finish process all traceview file' + '\n')
        else:
            print('Finish process all traceview file, but Failed' + '\n')
        try:
            self.txtfile_write.close()
        except:
            MyThread_0.pos_er = 1
            print('Fail to close txt write process' + '\n')
            return None, None, None, None, None, None, None
        return self.result_useinfo_allfile_save, self.list_cH_para_allfile_save, self.list_testclassname_allfile_save, self.list_fliename, paralist, self.vmin_para_allfile_save, self.vmax_para_allfile_save
    
    def para_check_state(self):
        list_checked_para = []
        list_checked_item = []
        list_checked_sheet = []
        for i, check_sheet_para in enumerate(MyThread_0.sheet_checklist_all_para):
            for j, check_item_para in enumerate(check_sheet_para):
                for k, para in enumerate(check_item_para):
                    if para.checkState(0) == Qt.Checked:
                        list_checked_para.append(para.text(MyThread_0.column))
                        list_checked_sheet.append(MyThread_0.checklist_sheet[i].text(MyThread_0.column))
                        list_checked_item.append(MyThread_0.checklist_all_item[i][j].text(MyThread_0.column))
                    else:
                        pass

        list_checked_para = sorted(set(list_checked_para), key=list_checked_para.index)
        list_checked_item = sorted(set(list_checked_item), key=list_checked_item.index)
        list_checked_sheet = sorted(set(list_checked_sheet), key=list_checked_sheet.index)
        return list_checked_sheet, list_checked_item, list_checked_para
    
    def value_write_excel(self, path_excelsave, data_allfile_allpara, cH_allfile_allpara, testname_allfile_allpara, name_para, list_allfilename, vmin_para_allfile, vmax_para_allfile):
        if demo.simple_mode == 1:
            try:
                print('Start write result to excel file' + '\n')
                pythoncom.CoInitialize()
                excel_write = DispatchEx('excel.application')
                excel_write.Visible = 0
                excel_write.DisplayAlerts = False
                # excel.DisplayAlerts = 0  # 关闭系统警告
                excel_write.ScreenUpdating = 0  # 关闭屏幕刷新
                wb_excelsave = excel_write.Workbooks.Add()
                ws_excelsave = wb_excelsave.ActiveSheet
                ws_excelsave.Name = "info_useful"
                print('excel file name: info_useful\n')
                value_col_CH_None = 0
                value_col_CH_Num = 0
                for file_num in range(len(data_allfile_allpara)):
                    value_row_CH_None = 0
                    value_row_CH_Num = 0
                    for para_num in range(len(data_allfile_allpara[file_num])):
                        if data_allfile_allpara[file_num][para_num] == []:
                            pass
                        else:
                            if cH_allfile_allpara[file_num][para_num][0] == 'None':
                                ws_excelsave.Cells(1, value_col_CH_None + 1).Value = list_allfilename[file_num]
                                ws_excelsave.Cells(value_row_CH_None + 2, value_col_CH_None + 2).Value = name_para[para_num]
                                para_positon = 0
                                for cell in ws_excelsave.Range(ws_excelsave.Cells(3 + value_row_CH_None,
                                                                            value_col_CH_None + 2),
                                                              ws_excelsave.Cells(len(data_allfile_allpara[file_num]
                                                        [para_num]) + 2 + value_row_CH_None, value_col_CH_None + 2)):
                                    cell.Value = data_allfile_allpara[file_num][para_num][para_positon]
                                    para_positon = para_positon + 1

                                testname_positon = 0
                                for cell in ws_excelsave.Range(ws_excelsave.Cells(3 + value_row_CH_None,
                                                                                  value_col_CH_None + 1),
                                                               ws_excelsave.Cells(len(testname_allfile_allpara[file_num]
                                                                                    [para_num]) + 2 + value_row_CH_None,
                                                                                  value_col_CH_None + 1)):
                                    cell.Value = testname_allfile_allpara[file_num][para_num][testname_positon]
                                    testname_positon = testname_positon + 1

                            else:
                                ws_excelsave.Cells(1, value_col_CH_Num + 1).Value = list_allfilename[file_num]
                                ws_excelsave.Cells(2 + value_row_CH_Num, value_col_CH_Num + 3).Value = name_para[para_num]

                                para_positon = 0
                                for cell in ws_excelsave.Range(ws_excelsave.Cells(3 + value_row_CH_Num,
                                                                            value_col_CH_Num + 3),
                                                              ws_excelsave.Cells(len(data_allfile_allpara[file_num]
                                                                                     [para_num])+2 + value_row_CH_Num,
                                                                                 value_col_CH_Num + 3)):
                                    cell.Value = data_allfile_allpara[file_num][para_num][para_positon]
                                    para_positon = para_positon + 1

                                CH_positon = 0
                                for cell in ws_excelsave.Range(ws_excelsave.Cells(3 + value_row_CH_Num,
                                                                                  value_col_CH_Num + 2),
                                                               ws_excelsave.Cells(len(cH_allfile_allpara[file_num]
                                                                                    [para_num])+2 + value_row_CH_Num,
                                                                                  value_col_CH_Num + 2)):
                                    cell.Value = 'CH' + cH_allfile_allpara[file_num][para_num][CH_positon]
                                    CH_positon = CH_positon + 1

                                testname_positon = 0
                                for cell in ws_excelsave.Range(ws_excelsave.Cells(3 + value_row_CH_Num,
                                                                                  value_col_CH_Num + 1),
                                                               ws_excelsave.Cells(len(testname_allfile_allpara[file_num][para_num])+2 + value_row_CH_Num,
                                                                                  value_col_CH_Num + 1)):
                                    if cH_allfile_allpara[file_num][para_num][testname_positon] == '0':
                                        cell.Value = testname_allfile_allpara[file_num][para_num][testname_positon]
                                    else:
                                        pass
                                    testname_positon = testname_positon + 1

                        value_row_CH_None = value_row_CH_None + len(data_allfile_allpara[file_num][para_num]) + 1
                        value_row_CH_Num = value_row_CH_Num + len(data_allfile_allpara[file_num][para_num]) + 1
                    value_col_CH_None = value_col_CH_None + len(data_allfile_allpara[file_num]) * 2
                    value_col_CH_Num = value_col_CH_Num + len(data_allfile_allpara[file_num]) * 3
                wb_excelsave.SaveAs(path_excelsave + r'\result_info_useful.xlsx')
                wb_excelsave.Close()
                excel_write.Application.Quit()
                pythoncom.CoUninitialize()
                print('Finish save result to excel file' + '\n')
            except:
                MyThread_0.pos_er = 1
                excel_write.Application.Quit()
                pythoncom.CoUninitialize()
                print('Error in function value_write_excel' + '\n')
                return
        else:
            try:
                print('Start write result to excel file, please wait...' + '\n')
                pythoncom.CoInitialize()
                excel_write = DispatchEx('excel.application')
                excel_write.Visible = 0
                excel_write.DisplayAlerts = False
                # excel.DisplayAlerts = 0  # 关闭系统警告
                excel_write.ScreenUpdating = 0  # 关闭屏幕刷新
                wb_excelsave = excel_write.Workbooks.Add()
                ws_excelsave = wb_excelsave.ActiveSheet
                ws_excelsave.Name = "info_useful"
                print('excel file name: info_useful\n')

                ## 综合所有文件确定testname的总体情况
                testname_para_total = []
                len_testname_total = 0
                len_testname_para_total = [0]
                for para_num in range(len(name_para)):
                    testname_total = []
                    for file_num, file_data in enumerate(testname_allfile_allpara):
                        testname_total = testname_total + file_data[para_num]
                    sort_testname_total = sorted(set(testname_total), key=testname_total.index)
                    dict_testname_total = dict(zip(sort_testname_total,range(len(sort_testname_total))))
                    testname_para_total.append(dict_testname_total)
                    len_testname_total = len_testname_total + len(sort_testname_total)
                    len_testname_para_total.append(len_testname_total)

                ## 综合所有文件确定CH的总体情况
                CH_total = []
                for para_num in range(len(name_para)):
                    for file_num, file_data in enumerate(cH_allfile_allpara):
                        if file_num < 20: #最多只查找20个文件，为了节省时间
                            CH_total.extend(file_data[para_num])
                        else:
                            break
                sort_CH_total = sorted(set(CH_total), key=CH_total.index)
                len_CH = len(sort_CH_total)

                range_CHNone_list = []
                range_CHNum_list = []

                for i in range(1+len(list_allfilename)):
                    range_CHNone_list.append([])
                    for j in range(2 * len_testname_total + len(name_para)):
                        range_CHNone_list[i].append(None)

                for i in range(2+len(list_allfilename)):
                    range_CHNum_list.append([])
                    for j in range((len_CH + 1) * len_testname_total + len(name_para)):
                        range_CHNum_list[i].append(None)
                ## 根据CH的类型来写参数名称和位置
                if len_CH == 1:
                    range_CHNone_list[0][0] = "SN"
                    range_CHNone_list[0][1] = "Parameter"
                    value_col_paraname_None = 3
                    for para_num , para_data in enumerate(name_para):
                        range_CHNone_list[0][value_col_paraname_None-1] = para_data
                        value_col_paraname_None = value_col_paraname_None + 1 + (len_CH+1) * (len(testname_para_total[para_num]))
                else:
                    range_CHNum_list[0][0] = "SN"
                    range_CHNum_list[0][1] = "Parameter"
                    range_CHNum_list[1][1] = "Channel"
                    value_col_paraname_Num = 3
                    value_col_CH_Num = 3
                    for para_num, para_data in enumerate(name_para):
                        range_CHNum_list[0][value_col_paraname_Num-1] = para_data
                        value_col_paraname_Num = value_col_paraname_Num + 1 + (len_CH+1) * (len(testname_para_total[para_num]))
                    for test_num, test_data in enumerate(testname_para_total):
                        for col in range(len_CH * len(testname_para_total[test_num])):
                            range_CHNum_list[1][value_col_CH_Num + col + col//len_CH - 1] = 'CH' + str(col % len_CH)
                        value_col_CH_Num = value_col_CH_Num + (len_CH+1) * len(testname_para_total[test_num]) + 1
                ## 根据CH的类型来确定数据的位置
                value_row_CH_None = 0
                value_row_CH_Num = 0
                if len_CH == 1: # 当为单通道时
                    for file_num, file_data in enumerate(data_allfile_allpara):
                        range_CHNone_list[1 + value_row_CH_None][0] = list_allfilename[file_num]
                        for para_num, para_data in enumerate(file_data):
                            if para_data == []:
                                pass
                            else:
                                for col, data in enumerate(para_data):
                                    # 写数据
                                    range_CHNone_list[1 + value_row_CH_None][2 +
                                    (len_CH+1)*(int(testname_para_total[para_num].
                                                    get(testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH+1)*len_testname_para_total[para_num] + para_num] = data
                                    #填充颜色
                                    if demo.colors_mode == 0:
                                        try:
                                            if MyThread_0.use_define_range == 1:
                                                if (MyThread_0.path_para_input_vmin[para_num] is None or float(data) >
                                                    MyThread_0.path_para_input_vmin[para_num]) and \
                                                        (MyThread_0.path_para_input_vmax[para_num] is None or float(
                                                    data) <MyThread_0.path_para_input_vmax[para_num]):
                                                        pass
                                                else:
                                                    ws_excelsave.Cells(2 + value_row_CH_None, 3 +
                                                        (len_CH + 1) * (int(testname_para_total[para_num].get(
                                                        testname_allfile_allpara[file_num][para_num][col]))) +
                                                        (len_CH + 1) *len_testname_para_total[para_num] +
                                                                       para_num).Interior.Color = 0xFFF68F
                                            else:
                                                if (vmin_para_allfile[file_num][para_num][col] is None or
                                                    float(data) > vmin_para_allfile[file_num][para_num][col]) \
                                                    and (vmax_para_allfile[file_num][para_num][col] is None or
                                                         float(data) < vmax_para_allfile[file_num][para_num][col]):
                                                    pass
                                                else:
                                                    ws_excelsave.Cells(2 + value_row_CH_None, 3 +
                                                    (len_CH + 1) * (int(testname_para_total[para_num].
                                                    get(testname_allfile_allpara[file_num][para_num][col]))) +
                                                    (len_CH + 1) *len_testname_para_total[para_num] + para_num).\
                                                    Interior.Color = 0xFFF68F
                                        except:
                                            pass
                                    else:
                                        pass
                                     # 写testclass
                                    range_CHNone_list[1 + value_row_CH_None][1 +
                                    (len_CH+1)*(int(testname_para_total[para_num].
                                                    get(testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH+1)*len_testname_para_total[para_num] + para_num] = testname_allfile_allpara[file_num][para_num][col]
                        value_row_CH_None = value_row_CH_None + 1
                else: # 当为多通道时
                    for file_num, file_data in enumerate(data_allfile_allpara):
                        range_CHNum_list[2 + value_row_CH_Num][0] = list_allfilename[file_num]
                        for para_num, para_data in enumerate(file_data):
                            if para_data == []:
                                pass
                            else:
                                for col, data in enumerate(para_data):
                                    #写数据
                                    range_CHNum_list[2 + value_row_CH_Num][2 +
                                    (len_CH+1)*(int(testname_para_total[para_num].
                                                    get(testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH+1)*len_testname_para_total[para_num] +
                                    int(cH_allfile_allpara[file_num][para_num][col]) + para_num] = data
                                    # 填充颜色
                                    time1 = time.time()
                                    if demo.colors_mode == 0:
                                        try:
                                            if MyThread_0.use_define_range == 1:
                                                if (MyThread_0.path_para_input_vmin[para_num] is None or float(data) >
                                                    MyThread_0.path_para_input_vmin[para_num]) and \
                                                        (MyThread_0.path_para_input_vmax[para_num] is None or float(
                                                    data) <MyThread_0.path_para_input_vmax[para_num]):
                                                        pass
                                                else:
                                                    ws_excelsave.Cells(3 + value_row_CH_Num, 3 +
                                                            (len_CH + 1) * (int(testname_para_total[para_num].get(
                                                        testname_allfile_allpara[file_num][para_num][col]))) +
                                                            (len_CH + 1) *len_testname_para_total[para_num] + int(
                                                        cH_allfile_allpara[file_num][para_num][
                                                            col]) + para_num).Interior.Color = 0xFFF68F
                                            else:
                                                if (vmin_para_allfile[file_num][para_num][col] is None or float(data) >
                                                    vmin_para_allfile[file_num][para_num][col]) \
                                                        and (vmax_para_allfile[file_num][para_num][col] is None or float(data) <
                                                             vmax_para_allfile[file_num][para_num][col]):
                                                    pass
                                                else:
                                                    ws_excelsave.Cells(3 + value_row_CH_Num, 3 +
                                                    (len_CH + 1) * (int(testname_para_total[para_num].
                                                            get(testname_allfile_allpara[file_num][para_num][col]))) +
                                                    (len_CH + 1) *len_testname_para_total[para_num] +
                                                    int(cH_allfile_allpara[file_num][para_num][col]) +
                                                                       para_num).Interior.Color = 0xFFF68F
                                        except:
                                            pass
                                    else:
                                        pass
                                    time2 = time.time()
                                    print('time: ', time2 - time1)
                                    #写testclass
                                    range_CHNum_list[2 + value_row_CH_Num][1 +
                                    (len_CH+1)*(int(testname_para_total[para_num].get(testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH+1)*len_testname_para_total[para_num] + para_num] = testname_allfile_allpara[file_num][para_num][col]
                        value_row_CH_Num = value_row_CH_Num + 1
                if len_CH == 1:
                    ws_excelsave.Range(ws_excelsave.Cells(1, 1), ws_excelsave.Cells((1 + len(list_allfilename)),
                                         (1 + 2 * len_testname_total + len(name_para) - 1))).Value = range_CHNone_list
                else:
                    ws_excelsave.Range(ws_excelsave.Cells(1, 1), ws_excelsave.Cells((2 + len(list_allfilename)),
                                (1 + (len_CH + 1) * len_testname_total + len(name_para)-1))).Value = range_CHNum_list
                wb_excelsave.SaveAs(path_excelsave + r'\result_info_useful.xlsx')
                wb_excelsave.Close()
                excel_write.Application.Quit()
                pythoncom.CoUninitialize()
                print('Finish save result to excel file' + '\n')
            except:
                MyThread_0.pos_er = 1
                excel_write.Application.Quit()
                pythoncom.CoUninitialize()
                print('Error in function value_write_excel' + '\n')
                return
            
    def callback_input(self):
        # 这部分用于将用户在对话框中的输入传递给数据处理程序部分
        MyThread_0.pos_er = 0
        path_txtsave = demo._main.edit_txtsave.text()
        path_specfile = demo._main.edit_specfile.text()
        path_traceview = demo._main.edit_traceview.text()
        path_excelsave = demo._main.edit_excelsave.text()
        path_sheet = demo._main.edit_sheet.text()
        path_para_input = list(demo._main.edit_para.toPlainText().split("\n"))
        path_para_input_value = []
        MyThread_0.path_para_input_vmin = []
        MyThread_0.path_para_input_vmax = []
        for para in path_para_input:
            para_value_range = list(para.split(";"))
            path_para_input_value.append(para_value_range[0].strip())
            if len(para_value_range) == 3:
                MyThread_0.use_define_range = 1
                if para_value_range[1].strip() == '':
                    MyThread_0.path_para_input_vmin.append(None)
                else:
                    try:
                        MyThread_0.path_para_input_vmin.append(float(para_value_range[1]))
                    except:
                        print("the input min range of parameter is not number")
                        return None, None, None, None, None, None
                if para_value_range[2].strip() == '':
                    MyThread_0.path_para_input_vmax.append(None)
                else:
                    try:
                        MyThread_0.path_para_input_vmax.append(float(para_value_range[2]))
                    except:
                        print("the input max range of parameter is not number")
                        return None, None, None, None, None, None
            else:
                MyThread_0.path_para_input_vmin.append(None)
                MyThread_0.path_para_input_vmax.append(None)
        path_para = []
        for para in path_para_input_value:
            if para == '':
                pass
            else:
                path_para.append(para.strip())
        path_para = sorted(set(path_para), key=path_para.index)

        if MyThread_0.fun_mode == 0:
            try:
                if str(path_txtsave).strip() == '':
                    try:
                        cur_dir = str(path_specfile) + '\\'
                        folder_name = 'txt_result_save'
                        if os.path.isdir(cur_dir):
                            path_txtsave = os.path.join(cur_dir, folder_name)
                            if os.path.isdir(path_txtsave):
                                pass
                            else:
                                os.mkdir(path_txtsave)
                    except:
                        cur_dir = str(path_specfile) + '/'
                        folder_name = 'txt_result_save'
                        if os.path.isdir(cur_dir):
                            path_txtsave = os.path.join(cur_dir, folder_name)
                            if os.path.isdir(path_txtsave):
                                pass
                            else:
                                os.mkdir(path_txtsave)
                else:
                    pass
                if str(path_excelsave).strip() == '':
                    try:
                        cur_dir = str(path_traceview) + '\\'
                        folder_name = 'excel_result_save'
                        if os.path.isdir(cur_dir):
                            path_excelsave = os.path.join(cur_dir, folder_name)
                            if os.path.isdir(path_excelsave):
                                pass
                            else:
                                os.mkdir(path_excelsave)
                    except:
                        cur_dir = str(path_traceview) + '/'
                        folder_name = 'excel_result_save'
                        if os.path.isdir(cur_dir):
                            path_excelsave = os.path.join(cur_dir, folder_name)
                            if os.path.isdir(path_excelsave):
                                pass
                            else:
                                os.mkdir(path_excelsave)
                else:
                    pass
            except:
                MyThread_0.pos_er = 1
                print('Error: can not creat txt and excel filedir to save results' + '\n')
                return None, None, None, None, None, None,
        else:
            pass
        MyThread_0.path_txtsave_image = path_txtsave
        return(path_txtsave, path_specfile, path_traceview, path_excelsave, path_para, path_sheet)

    def Txtreadlinesfunc(self, filetowrite, testitem_txt, itemlist, reformat, KEY_TSET_PARAMETER_NAME):
        '''
        Function: extract key information from traceview files
        :param testitem_txt: original file, str format
        :param itemlist: list of test item name from specfile, of course add some additional str for better match
        :param reformat: the pattern adapted from key parameters
        :param KEY_TSET_PARAMETER_NAME: key parameter name, use for writing into savefile, and distinguish
        :return: None
        '''
        # Two pattern
        # key_parameter_pattern is use to extract values of key parameters
        # and testitempattern is use to extract test item name and test corner name
        #
        try:
            result_useinfo_para_save = []
            vmin_para = []
            vmax_para = []
            list_cH_para = []
            list_testclassname_para = []
            key_parameter_pattern = re.compile(reformat)
            testitempattern = re.compile(r'(?<=Testing)\s+.*?(?<=\.)')
            #
            # combine every two nearby item pattern 'in testitem_reformat' list to form new pattern
            # And use these new pattern to divide 'testitem_txt'
            # After above steps, we can get str format content for every corner test item
            #
            try:
                testitem_reformat, list_len_itemname, list_testname, itemchannellist_start_result = self.FindActualItemFullPattern(testitem_txt, itemlist)
            except:
                MyThread_0.pos_er = 1
                print('can not find the test class name' + '\n')
                return None, None, None, None, None
            for i, testitem_number in enumerate(testitem_reformat):
                if i < len(list_testname) - 1:
                    if list_testname[i] == list_testname[i+1]:
                        testclass_repeat = 1
                    else:
                        testclass_repeat = 0
                else:
                    testclass_repeat = 0
                testitem_pattern = re.compile(testitem_number, re.DOTALL)
                testitem_txt_use = testitem_txt[
                                   (itemchannellist_start_result[i]):-1]
                try:
                    testitem_result = testitem_pattern.search(testitem_txt_use).group()
                except:
                    testitem_number = testitem_number[0:(len(list_testname[i])+2)]
                    testitem_pattern = re.compile(testitem_number, re.DOTALL)
                    testitem_result = testitem_pattern.search(testitem_txt_use).group()
                    pass
                #split by row, have'\n' at the end of each line
                txtrowlist = testitem_result.split("\n")
                #
                # extract values of every key parameter from every line by using regular expression
                # usually the values are numbers, so also we extract the range of every values,
                # then compare them see if the values within the range, and output some information about these
                #
                for line in txtrowlist:  # read line-by-line
                    line = ' ' + line + ' '
                    result = key_parameter_pattern.findall(line)
                    if result:
                        testclassname = testitempattern.search(testitem_number).group()[:-1].strip()
                        # the fifth char of every line is channel number,([0][here is channel number])
                        if line[2].isdigit() and line[5].isdigit():
                            CHnumber = line[5]
                            #
                            if CHnumber == "0":
                                # before every CH0, write test item and corner name
                                filetowrite.write(KEY_TSET_PARAMETER_NAME + ' TEST Corner: ' +
                                                             testclassname + '\n')
                            else:
                                pass
                        else:
                            # before every CH0, write test item and corner name
                            CHnumber = 'None'
                            filetowrite.write(KEY_TSET_PARAMETER_NAME + ' TEST Corner: ' +
                                              testclassname + '\n')
                        result = (''.join(result)).replace('=', '').strip()
                        # extract min and max of values and judge what to write
                        valuemin, valuemax = self.getrange_para(line)
                        if testclass_repeat == 0:
                            result_useinfo_para_save.append(result)
                            list_cH_para.append(CHnumber)
                            list_testclassname_para.append(testclassname)
                            vmin_para.append(valuemin)
                            vmax_para.append(valuemax)
                        else:
                            pass
                        #
                        self.value_judge_write_txt(result, filetowrite, KEY_TSET_PARAMETER_NAME, valuemin,
                                                     valuemax, CHnumber)
                        #
                    else:
                        pass
            return result_useinfo_para_save, list_cH_para, list_testclassname_para, vmin_para, vmax_para
        except:
            MyThread_0.pos_er = 1
            print('Error in function Txtreadlinesfunc' + '\n')
            pass

    def getRowsClosNum(self, ws, index = 0):
        try:
            if index == 0:
                rows = ws.max_row
                columns = ws.max_column
                j = 1
                i = 0
                k = 0
                max_row = 0
                max_column = 0
                while(j):
                    row = rows + 50 - i  # 50与10是任意选的，为了防止openpyxl检测到的最大行列有问题，向下探测50单元格，向右探测10单元格，看是否还有内容
                    if row > 0:
                        if not ws.cell(row, 1).value:
                            i = i + 1
                        else:
                            max_row = row
                            j = 0
                    else:
                        j = 0
                maxrow = max(max_row, rows)
                j = 1
                while(j):
                    column = columns + 10 - k
                    if column > 0:
                        if not ws.cell(3, column).value:
                            k = k + 1
                        else:
                            max_column = column
                            j = 0
                    else:
                        j = 0
                maxcolumn = max(max_column, columns)
            else:
                rows = ws.usedrange.rows.count
                columns = ws.usedrange.columns.count
                i = 0
                row_add = 50
                j = row_add
                for row in list(reversed(list(ws.Range(ws.Cells(rows+1,1), ws.Cells(rows+row_add,1)).Value))):
                    for cell_value in row:
                        if cell_value is not None:
                            j = i
                            break
                        else:
                            pass
                        i = i + 1
                maxrow = rows + row_add - j
                i = 0
                col_add = 10
                j = col_add
                for cell_value in list(reversed(list(ws.Range(ws.Cells(1, columns), ws.Cells(1, columns + col_add)).Value[0]))):
                    if cell_value is not None:
                        j = i
                        break
                    else:
                        pass
                    i = i + 1
                maxcolumn = columns + col_add - j
            return maxrow, maxcolumn
        except:
            MyThread_0.pos_er = 1
            print('Error in function getRowsClosNum' + '\n')
            pass

    def value_judge_write_txt(self, result, filetowrite, KEY_TSET_PARAMETER_NAME, valuemin=None, valuemax=None,
                                CHnumber="None"):
        '''
        Function: compare result and value range, and judge what to write
        :param result:
        :param filetowrite:
        :param KEY_TSET_PARAMETER_NAME:
        :param valuemin:
        :param valuemax:
        :param CHnumber:
        :return: None
        '''
        try:
            notelist = ["CH" + CHnumber + " " + str(result),
                        " " + KEY_TSET_PARAMETER_NAME +" TEST ERROR TYPE: Less Than Minimum",
                        " " + KEY_TSET_PARAMETER_NAME + " TEST ERROR TYPE: Greater Than Maximum",
                        " " + KEY_TSET_PARAMETER_NAME + " TEST ERROR TYPE: Result Not Number"]
            try:
                if len(result) > 2:
                    if result[0] == '0' and result[1] == 'x':
                        result_judge = float(int(result, 16))
                    else:
                        result_judge = float(result)
                else:
                    result_judge = float(result)
                if not valuemin is None and not valuemax is None:
                    if result_judge >= valuemin and result_judge < valuemax:
                        filetowrite.write(notelist[0] + '\n')
                    elif result_judge < valuemin:
                        filetowrite.write(notelist[0] + notelist[1] + '\n')
                    else:
                        filetowrite.write(notelist[0] + notelist[2] + '\n')
                elif valuemin is None and not valuemax is None:
                    if result_judge < valuemax:
                        filetowrite.write(notelist[0] + '\n')
                    else:
                        filetowrite.write(notelist[0] + notelist[2] + '\n')
                elif not valuemin is None and valuemax is None:
                    if result_judge >= valuemin:
                        filetowrite.write(notelist[0] + '\n')
                    else:
                        filetowrite.write(notelist[0] + notelist[1] + '\n')
                else:
                    filetowrite.write(notelist[0] + '\n')
            except ValueError:
                filetowrite.write(notelist[0] + notelist[3] + '\n')
                pass
        except:
            MyThread_0.pos_er = 1
            print('Error in function value_judge_write_txt' + '\n')
            pass

    def getrange_para(self, linestr):
        '''
        Function: obtain range of key parameter value
        :param linestr: a row in the traceview file that contain key parameter
        :return: range of value, min and max
        '''
        try:
            pattern = re.compile(r'(?<=Min:)\s*[\d\-\<][0-9NoneM\.E\-\<\>]*')
            valueMin = pattern.findall(linestr)
            pattern = re.compile(r'(?<=Max:)\s*[\d\-\<][0-9NoneM\.E\-\<\>]*')
            valueMax = pattern.findall(linestr)
            try:
                valueMin = float((''.join(valueMin)).strip())
            except ValueError:
                valueMin = None
            try:
                valueMax = float((''.join(valueMax)).strip())
            except ValueError:
                valueMax = None
            return valueMin, valueMax
        except:
            MyThread_0.pos_er = 1
            print('Error in function getrange_para' + '\n')
            pass

    def listaddstr(self, itemlist, strneedadd):
        '''
        Function: add special str for every elements of a list
        :param sheet_ranges: sheet of excel, a column, contain test item name, and all this item form a list
        :param strneedadd: str need to add,
        :param min_row1: start row number
        :param max_col1: column number
        :param max_row1: end row number
        :return: a list which have already add some special str
        '''
        try:
            itemlist = list(map(lambda x: strneedadd + x + r'\s+', itemlist))
            return itemlist
        except:
            MyThread_0.pos_er = 1
            print('Error in function listaddstr' + '\n')
            pass

    def FindActualItemFullPattern(self, testitem_txt, itemlist):
        '''
        Function: use every two nearby element of itemlist to form full pattern that
        :param testitem_txt: traceview file
        :param itemlist: list contains test item name
        :return: a full pattern list
        PS:
        1.Add channel num to test item and as re to match the traceview,if yes，means the traceview have the
        difference of channel, we should divide the data by channel;if No, means there are no channel;
        2.Also we return 3 para,"list_testname" are a list of the test item(from specfile) that we can find from the traceview,
        "list_len_itemname" are a list of the length of the test item name, the last para "itemnamelist" are the re full pattern
        of test item, for macth some part of the traceview
        '''
        try:
            itemchannellist = []
            itemchannellist_start_result = []
            itemnamelist = []
            list_len_itemname = []
            list_testname = []
            itemchannel_start = -1
            itemchannel_start_old = -1
            if testitem_txt[0:6] == "[0][0]" or testitem_txt[0:6] == "[0][1]" or testitem_txt[0:6] == "[0][2]" or testitem_txt[0:6] == "[0][3]":
                channel = 1
            else:
                channel = 0
            for i, item in enumerate(itemlist):
                itemchannel_result = []
                itemchannel_start_result = []
                if channel == 1:
                    item_channel = r'\[0\]\[\d\]\s*' + item
                    info_itemchannel_result = [[m.start(), m.end(), m.group()] for m in re.compile(item_channel).finditer(testitem_txt)]
                    # 之所以加start()识别，是因为有些item包含在另一个item中，这样在寻找时会导致匹配到已经被匹配过的item
                    for j in info_itemchannel_result:
                        itemchannel_result.append(j[2].replace("[", "\[").replace("]", "\]"))
                        itemchannel_start = j[0]
                        itemchannel_start_result.append(j[0])
                    if itemchannel_result:
                        if itemchannel_start > itemchannel_start_old:
                            itemchannellist.extend(itemchannel_result)
                            itemchannellist_start_result.extend(itemchannel_start_result)
                            itemchannel_start_old = itemchannel_start
                        else:
                            pass
                    else:
                        pass
                else:
                    info_itemchannel_result = [[m.start(), m.end(), m.group()] for m in
                                               re.compile(item).finditer(testitem_txt)]
                    for j in info_itemchannel_result:
                        itemchannel_result.append(j[2].replace("[", "\[").replace("]", "\]"))
                        itemchannel_start = j[0]
                        itemchannel_start_result.append(j[0])
                    if itemchannel_result:
                        if itemchannel_start > itemchannel_start_old:
                            itemchannellist.extend(itemchannel_result)
                            itemchannellist_start_result.extend(itemchannel_start_result)
                            itemchannel_start_old = itemchannel_start
                        else:
                            pass
                    else:
                        pass
            for i in range(len(itemchannellist)):
                list_testname.append(itemchannellist[i])
                if i == len(itemchannellist) - 1:
                    if channel == 1:
                        fullitempattern = itemchannellist[i] + r".*" + r"?\n\[0\]\[\d\] Testing "
                        list_len_itemname.append(len("[0][d] Testing "))
                    else:
                        fullitempattern = itemchannellist[i] + r".*" + r"?\nTesting "
                        list_len_itemname.append(len("Testing "))
                else:
                    if channel == 1:
                        fullitempattern = itemchannellist[i] + r".*" + r"?\n\[0\]\[\d\] Testing "
                        list_len_itemname.append(len("[0][d] Testing "))
                    else:
                        fullitempattern = itemchannellist[i] + r".*" + r"?\nTesting "
                        list_len_itemname.append(len("Testing "))
                itemnamelist.append(fullitempattern)
            return itemnamelist, list_len_itemname, list_testname, itemchannellist_start_result

        except:
            MyThread_0.pos_er = 1
            print('Error in function FindActualItemFullPattern' + '\n')
            pass

    def para_re(self,list_para):
        #
        try:
            list_all_para_and_re = []
            for para in list_para:
                list_para_and_re = []
                re_para = r'(?<=' + '\s' + para + r')\s*[\:]*\s+[\=\d\-\<]\s*[0-9XxNoneMABCDEF\.E\-\<\>\s]+[\s\n]+?'
                list_para_and_re.append(re_para)
                list_para_and_re.append(para)
                list_all_para_and_re.append(list_para_and_re)
            return list_all_para_and_re
        except:
            MyThread_0.pos_er = 1
            print('Error in function para_re' + '\n')
            return []

    def excel_process(self):
        timestart = time.time()
        print('The begining of Excel process procedure' + '\n')
        try:
            path_txtsave, path_specfile, path_traceview, path_excelsave, \
            path_para, path_sheet = self.callback_input()
        except:
            MyThread_0.pos_er = 2
            print('please check input information, fail to callback' + '\n')
            return

        if path_para == []:
            temp_low = '0C'
            color_low = 0xFDE9D9
            temp_room = '35C'
            color_room = 0xE4DFEC
            temp_high = '70C'
            color_high = 0xDAEEF3
        elif len(path_para) == 1:
            lowlist = path_para[0].split(';').strip()
            if len(lowlist) == 1:
                temp_low = lowlist[0]
                color_low = 0xFDE9D9
            elif len(lowlist) == 2:
                temp_low = lowlist[0]
                color_low = hex(eval(lowlist[1]))
            else:
                temp_low = '0C'
                color_low = 0xFDE9D9
            temp_room = '35C'
            color_room = 0xE4DFEC
            temp_high = '70C'
            color_high = 0xDAEEF3
        elif len(path_para) == 2:
            lowlist = path_para[0].split(';').strip()
            if len(lowlist) == 1:
                temp_low = lowlist[0]
                color_low = 0xFDE9D9
            elif len(lowlist) == 2:
                temp_low = lowlist[0]
                color_low = hex(eval(lowlist[1]))
            else:
                temp_low = '0C'
                color_low = 0xFDE9D9
            roomlist = path_para[1].split(';').strip()
            if len(roomlist) == 1:
                temp_room = roomlist[0]
                color_room = 0xE4DFEC
            elif len(roomlist) == 2:
                temp_room = roomlist[0]
                color_room = hex(eval(roomlist[1]))
            else:
                temp_room = '35C'
                color_room = 0xE4DFEC
            temp_high = '70C'
            color_high = 0xDAEEF3
        elif len(path_para) == 3:
            lowlist = path_para[0].split(';').strip()
            if len(lowlist) == 1:
                temp_low = lowlist[0]
                color_low = 0xFDE9D9
            elif len(lowlist) == 2:
                temp_low = lowlist[0]
                color_low = hex(eval(lowlist[1]))
            else:
                temp_low = '0C'
                color_low = 0xFDE9D9
            roomlist = path_para[1].split(';').strip()
            if len(roomlist) == 1:
                temp_room = roomlist[0]
                color_room = 0xE4DFEC
            elif len(roomlist) == 2:
                temp_room = roomlist[0]
                color_room = hex(eval(roomlist[1]))
            else:
                temp_room = '35C'
                color_room = 0xE4DFEC
            highlist = path_para[2].split(';').strip()
            if len(highlist) == 1:
                temp_high = highlist[0]
                color_high = 0xDAEEF3
            elif len(highlist) == 2:
                temp_high = highlist[0]
                color_high = hex(eval(highlist[1]))
            else:
                temp_high = '70C'
                color_high = 0xDAEEF3
        else:
            temp_low = '0C'
            color_low = 0xFDE9D9
            temp_room = '35C'
            color_room = 0xE4DFEC
            temp_high = '70C'
            color_high = 0xDAEEF3


        self.xlstoxlsx(path_specfile)

        try:
            for info in os.listdir(path_specfile):
                # obtain full path name of every files
                pre_path = os.path.abspath(path_specfile)
                info1 = os.path.join(pre_path, info)
                try:
                    if info1.endswith('.xlsx'):
                        print('Start excel process procedure of ' + info + '\n')
                        timestart1 = time.time()
                        try:
                            pythoncom.CoInitialize()
                            excel = DispatchEx('excel.application')
                            excel.Visible = 0
                            excel.DisplayAlerts = False
                            # excel.DisplayAlerts = 0  # 关闭系统警告
                            excel.ScreenUpdating = 0  # 关闭屏幕刷新
                            wb = excel.workbooks.Open(info1)
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Fail to load excel file: ' + info1 + '\n')
                            return
                        # 使用for循环来处理所有sheet
                        sheetnames = []
                        try:
                            sheetname_input = list(path_sheet.split(";"))
                            for sheetname in sheetname_input:
                                if not sheetname.strip():
                                    pass
                                else:
                                    try:
                                        sheetname = int(sheetname)
                                        sheetnames.append(sheetname)
                                    except:
                                        sheetnames.append(sheetname)
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Error: please input the right sheetnames, please check parameter '
                                                     'sheetnames in procedure' + '\n')
                            return
                        print(
                            'Start extract the related position of setup and measure parameter' + '\n')

                        allnullrow_sheet = []
                        for (k, sheet) in enumerate(sheetnames):
                            sheetname_print = wb.Worksheets(sheet).Name
                            try:
                                ws = wb.Worksheets(sheet)
                            except:
                                MyThread_0.pos_er = 2
                                excel.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('please check parameter sheetname:' + sheetname_print + '\n')
                                return
                            # 获取表格的最大行和最大列
                            try:
                                mrows, mcolumns = self.getRowsClosNum(ws, index=1)
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns + 1)).Borders.LineStyle = None
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1,
                                                            mcolumns + 1)).Interior.ColorIndex = -4142
                            except:
                                MyThread_0.pos_er = 2
                                excel.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('Fail to get maxrow and maxcol from sheet: ' + sheetname_print + '\n')
                                return

                            pos_setup_start = 0
                            pos_setup_end = 0
                            pos_measure_start = 0
                            pos_measure_end = 0
                            index_para = 0
                            for col, value_col in enumerate(
                                    (ws.Range(ws.Cells(3, 1), ws.Cells(3, mcolumns)).Value)[0]):
                                if not value_col:
                                    pass
                                else:
                                    if 'Setup Parameter' in value_col:
                                        pos_setup_start = col + 1
                                    elif 'Description' in value_col:
                                        if index_para == 0:
                                            pos_setup_end = col + 1
                                            index_para = 1
                                        else:
                                            pos_measure_end = col + 1
                                    elif 'Measurement Parameter' in value_col:
                                        pos_measure_start = col + 1
                                    else:
                                        pass

                            poslist_testname = []
                            for row, value_testname in enumerate(
                                    ws.Range(ws.Cells(4, 1), ws.Cells(mrows + 1, 1)).Value):
                                if not value_testname[0]:
                                    pass
                                else:
                                    poslist_testname.append(row + 4)

                            try:
                                allnullrow = []
                                for i in range(len(poslist_testname) - 1):
                                    setup_nullrowlist = []
                                    measure_nullrowlist = []
                                    allnotnullrow_set = 0
                                    allnotnullrow_mea = 0
                                    if poslist_testname[i + 1] - 2 - poslist_testname[i] == 0:
                                        if not ws.Cells(poslist_testname[i] + 1, pos_setup_start).Value:
                                            setup_nullrow = poslist_testname[i] + 1
                                            setup_nullrowlist.append(setup_nullrow)
                                            ws.Range(ws.Cells(setup_nullrow, pos_setup_start),
                                                          ws.Cells(setup_nullrow, pos_setup_end)).ClearContents
                                            ws.Range(ws.Cells(setup_nullrow, pos_setup_start),
                                                          ws.Cells(setup_nullrow, pos_setup_end)).Clear
                                        else:
                                            allnotnullrow_set = 1
                                        if not ws.Cells(poslist_testname[i] + 1, pos_measure_start).Value:
                                            measure_nullrow = poslist_testname[i] + 1
                                            measure_nullrowlist.append(measure_nullrow)
                                            ws.Range(ws.Cells(measure_nullrow, pos_measure_start),
                                                          ws.Cells(measure_nullrow, pos_measure_end)).ClearContents
                                            ws.Range(ws.Cells(measure_nullrow, pos_measure_start),
                                                          ws.Cells(measure_nullrow, pos_measure_end)).Clear
                                        else:
                                            allnotnullrow_mea = 1
                                    elif poslist_testname[i + 1] - 2 - poslist_testname[i] > 0:
                                        for row, value_row in enumerate(
                                                (ws.Range(ws.Cells(poslist_testname[i] + 1, pos_setup_start),
                                                               ws.Cells(poslist_testname[i + 1] - 1,
                                                                             pos_setup_start)).Value)):
                                            if not value_row[0]:
                                                setup_nullrow = row + poslist_testname[i] + 1
                                                setup_nullrowlist.append(setup_nullrow)
                                                ws.Range(ws.Cells(setup_nullrow, pos_setup_start),
                                                              ws.Cells(setup_nullrow, pos_setup_end)).ClearContents
                                                ws.Range(ws.Cells(setup_nullrow, pos_setup_start),
                                                              ws.Cells(setup_nullrow, pos_setup_end)).Clear
                                            else:
                                                allnotnullrow_set = allnotnullrow_set + 1
                                        for row, value_row in enumerate((ws.Range(
                                                ws.Cells(poslist_testname[i] + 1, pos_measure_start),
                                                ws.Cells(poslist_testname[i + 1] - 1, pos_measure_start)).Value)):
                                            if not value_row[0]:
                                                measure_nullrow = row + poslist_testname[i] + 1
                                                measure_nullrowlist.append(measure_nullrow)
                                                ws.Range(ws.Cells(measure_nullrow, pos_measure_start),
                                                              ws.Cells(measure_nullrow,
                                                                            pos_measure_end)).ClearContents
                                                ws.Range(ws.Cells(measure_nullrow, pos_measure_start),
                                                              ws.Cells(measure_nullrow, pos_measure_end)).Clear
                                            else:
                                                allnotnullrow_mea = allnotnullrow_mea + 1
                                    else:
                                        pass
                                    allnullrow.extend(list(
                                        range((poslist_testname[i] + 1 + max(allnotnullrow_set, allnotnullrow_mea)),
                                              poslist_testname[i + 1])))

                                    rowstart = 5
                                    if not setup_nullrowlist:
                                        pass
                                    else:
                                        setup_cutlist = list(set(
                                            range(min(setup_nullrowlist), poslist_testname[i + 1]))
                                                             - set(setup_nullrowlist))
                                        if not setup_cutlist:
                                            pass
                                        else:
                                            for row in setup_cutlist:
                                                ws.Range(ws.Cells(row, pos_setup_start),
                                                              ws.Cells(row, pos_setup_end)).Cut()

                                                ws.Paste(Destination=ws.Cells(rowstart, 30))
                                                rowstart = rowstart + 1
                                            ws.Range(ws.Cells(5, 30),
                                                          ws.Cells(rowstart - 1, 30 + pos_setup_end -
                                                                        pos_setup_start)).Cut()
                                            ws.Paste(
                                                Destination=ws.Cells(min(setup_nullrowlist), pos_setup_start))

                                    rowstart = 5
                                    if not measure_nullrowlist:
                                        pass
                                    else:
                                        measure_cutlist = list(set(
                                            range(min(measure_nullrowlist), poslist_testname[i + 1]))
                                                               - set(measure_nullrowlist))
                                        if not measure_cutlist:
                                            pass
                                        else:
                                            for row in measure_cutlist:
                                                ws.Range(ws.Cells(row, pos_measure_start),
                                                              ws.Cells(row, pos_measure_end)).Cut()
                                                ws.Paste(
                                                    Destination=ws.Cells(
                                                        rowstart, 30))
                                                rowstart = rowstart + 1
                                            ws.Range(ws.Cells(5, 30),
                                                          ws.Cells(rowstart - 1, 30 + pos_measure_end -
                                                                        pos_measure_start)).Cut()
                                            ws.Paste(
                                                Destination=ws.Cells(min(measure_nullrowlist), pos_measure_start))
                                allnullrow_sheet.append(allnullrow)
                            except:
                                MyThread_0.pos_er = 2
                                excel.Application.Quit()
                                pythoncom.CoUninitialize()
                                print('Fail to get nullrow of setup and measure parameter: ' + sheetname_print + '\n')
                                return

                        try:
                            wb.Save()
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Fail to save excel file: ' + info1 + '\n')
                            return
                        print(
                            'Start extract the related position of null row in whole file' + '\n')
                        try:
                            for (k, sheet) in enumerate(sheetnames):
                                timestart2 = time.time()
                                sheetname_print = wb.Worksheets(sheet).Name
                                print("Begin to process data of " + sheetname_print +
                                                         ' in function delandaddNullrow' + '\n')
                                ws = wb.Worksheets(sheet)
                                # 获取表格的最大行和最大列
                                mrows, mcolumns = self.getRowsClosNum(ws, index=1)
                                nrows = ws.Rows.Count
                                ncols = ws.Columns.Count
                                ws.Range(
                                    ws.Cells(
                                        mrows + 1,
                                        1),
                                    ws.Cells(
                                        nrows,
                                        ncols)).Clear()
                                ws.Range(
                                    ws.Cells(
                                        1,
                                        mcolumns + 1),
                                    ws.Cells(
                                        nrows,
                                        ncols)).Clear()
                                ws.Range(
                                    ws.Cells(
                                        mrows + 1,
                                        1),
                                    ws.Cells(
                                        nrows,
                                        ncols)).Delete()
                                ws.Range(
                                    ws.Cells(
                                        1,
                                        mcolumns + 1),
                                    ws.Cells(
                                        nrows,
                                        ncols)).Delete()
                                allnullrow_sheet[k].reverse()
                                for row in allnullrow_sheet[k]:
                                    if ws.Application.WorksheetFunction.CountA(ws.Range(
                                            ws.Cells(row, 1), ws.Cells(row, mcolumns))) == 0:
                                        ws.Rows(row).Delete()
                                    else:
                                        pass

                                # step2：在每个test class之间加空行隔断
                                poslist_testname = []
                                for row, value_testname in enumerate(
                                        ws.Range(ws.Cells(5, 1), ws.Cells(mrows + 1, 1)).Value):
                                    if not value_testname[0]:
                                        pass
                                    else:
                                        poslist_testname.append(row + 5)

                                poslist_testname.reverse()
                                for row in poslist_testname:
                                    ws.Rows(row).Insert()
                                    ws.Range(ws.Cells(row, 1), ws.Cells(row, mcolumns)).Borders(
                                        8).LineStyle = None
                                    ws.Range(ws.Cells(row, 1), ws.Cells(row, mcolumns)).Borders(
                                        9).LineStyle = 1

                                timeend2 = time.time()
                                print(
                                    'Time for ' + sheetname_print + ' in function delandaddNullrow' + ' is ' + str(timeend2 - timestart2) + '\n')
                            wb.Save()
                            print('Excel file Save successful ' + '\n')
                            print('The end of function delandaddNullrow' + '\n')
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Fail extract the related position of null row in whole file' + '\n')
                            return
                        print('End of the data extraction process' + '\n')
                        print('Start divide part base on temperature and function' + '\n')
                        print('Start flag: before \'Module Setup\'' + '\n')
                        print('End flag: after \'Retest_Shutdown\'' + '\n')
                        print('Low temp flag: part with word: ' + temp_low + '\n')
                        print('Room temp flag: part with word: ' + temp_room + '\n')
                        print('High temp flag: part with word:' + temp_high + '\n')
                        print('Set special border and fill style in follow process' + '\n')
                        try:
                            for (k, sheet) in enumerate(sheetnames):
                                timepstart = time.time()
                                sheetname_print = wb.Worksheets(sheet).Name
                                endrow = 0
                                ws = wb.Worksheets(sheet)
                                mrows, mcolumns = self.getRowsClosNum(ws=ws, index=1)
                                ws.Cells(1, 1).Font.Size = 28  # 字体大小
                                ws.Cells(1, 1).Font.Color = 0xffffff  # 字体颜色
                                ws.Cells(1, 1).Font.Bold = False  # 是否粗体
                                ws.Cells(1, 1).Name = "Arial"  # 字体类型
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(1, mcolumns)).Interior.Color = 0xFF0000
                                ws.Cells(1, 2).Font.Size = 10  # 字体大小
                                ws.Cells(1, 2).Font.Color = 0xffffff  # 字体颜色
                                ws.Cells(1, 2).Font.Bold = False  # 是否粗体
                                ws.Cells(1, 2).Name = "Arial"  # 字体类型
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(1, mcolumns)).Borders(8).LineStyle = 1
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(1, mcolumns)).Borders(9).LineStyle = 1
                                ws.Range(ws.Cells(2, 1),
                                              ws.Cells(2, mcolumns)).Borders(9).LineStyle = 1
                                ws.Range(ws.Cells(3, 1),
                                              ws.Cells(3, mcolumns)).Borders(9).LineStyle = 1

                                ws.Range(ws.Cells(2, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Font.Size = 10
                                ws.Range(ws.Cells(2, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Name = 'Arial'
                                ws.Range(ws.Cells(2, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Font.Color = 0x000000
                                ws.Range(ws.Cells(2, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Font.Bold = False

                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).HorizontalAlignment = -4131
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).VerticalAlignment = -4108

                                ws.Range(ws.Cells(3, 1),
                                              ws.Cells(3, mcolumns)).HorizontalAlignment = -4108
                                ws.Range(ws.Cells(3, 1),
                                              ws.Cells(3, mcolumns)).VerticalAlignment = -4108
                                ws.Range(ws.Cells(3, 1),
                                              ws.Cells(3, mcolumns)).Interior.Color = 0xC0C0C0
                                ws.Range(ws.Cells(3, 1), ws.Cells(3, mcolumns)).Font.Bold = True

                                ws.Range(ws.Cells(mrows + 1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(8).LineStyle = None
                                ws.Range(ws.Cells(mrows + 1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(9).LineStyle = 1
                                ws.Range(ws.Cells(mrows + 1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(9).Weight = 4

                                ws.Range(ws.Cells(3, 1), ws.Cells(mrows + 1, 1)).Font.Size = 10
                                ws.Range(ws.Cells(3, 1), ws.Cells(mrows + 1, 1)).Name = 'Arial'
                                ws.Range(ws.Cells(3, 1),
                                              ws.Cells(mrows + 1, 1)).Font.Color = 0x000000
                                ws.Range(ws.Cells(3, 1), ws.Cells(mrows + 1, 1)).Font.Bold = True

                                tuple_col1 = ws.Range(ws.Cells(1, 1), ws.Cells(mrows + 1, 1)).Value
                                for row, str_row in enumerate(tuple_col1):
                                    row = row + 1
                                    if not str_row[0]:
                                        pass
                                    else:
                                        str_row = ''.join(list(str_row))
                                        if 'Module Setup' in str_row:
                                            ws.Range(ws.Cells(4, 1), ws.Cells(row - 1,
                                                                                             mcolumns)).Interior.Color = 0xF2F2F2
                                            ws.Range(ws.Cells(row - 1, 1),
                                                          ws.Cells(row - 1, mcolumns)).Borders(9).Weight = 4
                                        elif 'Retest' in str_row and 'Shutdown' in str_row:
                                            if endrow == 0:
                                                endrow = row
                                                ws.Range(ws.Cells(endrow, 1),
                                                              ws.Cells(mrows + 1,
                                                                            mcolumns)).Interior.Color = 0xF2F2F2
                                                ws.Range(ws.Cells(endrow, 1),
                                                              ws.Cells(endrow,
                                                                            mcolumns)).Borders(8).Weight = 4
                                            else:
                                                pass
                                        else:
                                            if endrow == 0:
                                                if temp_low in str_row and temp_high not in str_row \
                                                        and temp_room not in str_row:
                                                    nexttemp = 1
                                                    nextnullrow = row
                                                    while (nexttemp):
                                                        nextnullrow = nextnullrow + 1
                                                        if not tuple_col1[nextnullrow - 1][0]:
                                                            pass
                                                        else:
                                                            nexttemp = 0
                                                    ws.Range(ws.Cells(row, 1), ws.Cells(nextnullrow - 1,
                                                                                                       mcolumns)).Interior.Color = color_low
                                                elif temp_room in ws.Cells(row, 1).value and temp_high not in \
                                                        ws.Cells(row, 1).value:
                                                    nexttemp = 1
                                                    nextnullrow = row
                                                    while (nexttemp):
                                                        nextnullrow = nextnullrow + 1
                                                        if not tuple_col1[nextnullrow - 1][0]:
                                                            pass
                                                        else:
                                                            nexttemp = 0
                                                    ws.Range(ws.Cells(row, 1), ws.Cells(nextnullrow - 1,
                                                                                                       mcolumns)).Interior.Color = color_room
                                                elif temp_high in ws.Cells(row, 1).value:
                                                    nexttemp = 1
                                                    nextnullrow = row
                                                    while (nexttemp):
                                                        nextnullrow = nextnullrow + 1
                                                        if not tuple_col1[nextnullrow - 1][0]:
                                                            pass
                                                        else:
                                                            nexttemp = 0
                                                    ws.Range(ws.Cells(row, 1), ws.Cells(nextnullrow - 1,
                                                                                                       mcolumns)).Interior.Color = color_high
                                                else:
                                                    pass
                                            else:
                                                pass

                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(7).LineStyle = 1
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(11).LineStyle = 1

                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(10).LineStyle = 1
                                ws.Range(ws.Cells(1, 1),
                                              ws.Cells(mrows + 1, mcolumns)).Borders(10).Weight = 4

                                timepend = time.time()
                                print('Time for ' + sheetname_print + ' in colorfunction' + ' is ' + str(
                                        timepend - timepstart) + '\n')
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Fail to divide part base on temperature and set border and fill style' + '\n')
                            return
                        if MyThread_0.pos_er == 0:
                            print('Finish set border and fill style' + '\n')
                        elif MyThread_0.pos_er == 2:
                            print('Fail to set border and fill style' + '\n')
                        try:
                            wb.Save()
                            wb.Close()
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                        except:
                            MyThread_0.pos_er = 2
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
                            print('Fail to save excel file' + '\n')
                            return
                        timeend1 = time.time()
                        print('The end: already finish process all data for ' + info + '\n')
                        print('Total time for ' + info + ':' + str(timeend1 - timestart1) + '\n')
                    else:
                        pass
                except:
                    MyThread_0.pos_er = 2
                    excel.Application.Quit()
                    pythoncom.CoUninitialize()
                    print('Error in function excel_process' + '\n')
                    print('Fail to process specfile: ' + info + '\n')
                    return
        except:
            MyThread_0.pos_er = 2
            excel.Application.Quit()
            pythoncom.CoUninitialize()
            print('Error in function excel_process' + '\n')
            print('Fail to process all specfile: ' + '\n')
            return
        timeend = time.time()
        if MyThread_0.pos_er == 0:
            print('The end: already finish process all excel, Successful' + '\n')
            print('Path to save excel file: ' + path_specfile + '\n')
            print('Total time for data process: ' + str(timeend - timestart) + '\n')
        elif MyThread_0.pos_er == 2:
            print('The end: already finish process all excel, Fail' + '\n')
            print('Total time for data process: ' + str(timeend - timestart) + '\n')
        else:
            pass

    def xlstoxlsx(self, rootdir):
        '''
        Function: change file format,xls to xlsx
        :param rootdir: file path store specfile(xls format)
        :return: save a xlsx file and return xlsx file path
        Note: just apply to the path have only one file there
        '''
        try:
            print('Start specfile format conversion: XLS to xlsx')
            # 三个参数：父目录；所有文件夹名（不含路径）；所有文件名
            path_xlsxfile = []
            for parent, dirnames, filenames in os.walk(rootdir, topdown=True):
                for fn in filenames:
                    filedir = os.path.join(parent, fn)
                    if filedir.endswith(".xlsx"):
                        path_xlsxfile.append(filedir)
                    else:
                        if os.path.exists(filedir.replace('.xls', '.xlsx')) and os.path.exists(
                                filedir.replace('.XLS', '.xlsx')):
                            pass
                        else:
                            pythoncom.CoInitialize()
                            excel = DispatchEx('Excel.Application')
                            excel.Visible = 0
                            excel.DisplayAlerts = False  # 覆盖同名文件时不弹出框
                            wb = excel.Workbooks.Open(filedir)
                            # xlsx: FileFormat=51
                            # xls:  FileFormat=56
                            if filedir.endswith(".XLS"):
                                wb.SaveAs(filedir.replace('.XLS', '.xlsx'), FileFormat=51)
                                xlsx_filedir = filedir.replace('.XLS', '.xlsx')
                                path_xlsxfile.append(xlsx_filedir)
                            else:
                                wb.SaveAs(filedir.replace('.xls', '.xlsx'), FileFormat=51)
                                xlsx_filedir = filedir.replace('.xls', '.xlsx')
                                path_xlsxfile.append(xlsx_filedir)
                            wb.Close()
                            excel.Application.Quit()
                            pythoncom.CoUninitialize()
            print('Finish specfile format conversion')
            return (path_xlsxfile)
        except:
            MyThread_0.pos_er = 1
            print('Error in function xlstoxlsx')
            pass


class TableWin(QWidget):
    pos_updown = -1
    pos_save = []


    def __init__(self):
        super(TableWin, self).__init__()
        self.resize(QApplication.desktop().width(), QApplication.desktop().height()-100)
        self.sort_num = 0
        self.open_mode = 0
        self.data_read = 0
        self.part_creat_init()
        self.table_init()
        self.part_size_init()
        self.part_position_init()
        self.part_qss_init()
        self.part_func_init()

    def fn_timer(function):
        @wraps(function)
        def function_timer(*args, **kwargs):
            t0 = time.time()
            result = function(*args, **kwargs)
            t1 = time.time()
            print("Total time running %s: %s seconds" %
                  (function.func_name, str(t1 - t0))
                  )
            return result
        return function_timer

    def closeEvent(self, Event):
        demo._main.checkBox_tablemode.setChecked(False)

    def part_creat_init(self):
        self.table = QTableView(self)
        self.vmin_label = QLabel('Vmin')
        self.vmax_label = QLabel('Vmax')
        self.vmin_edit = QLineEdit()
        self.vmax_edit = QLineEdit()
        self.xlabel_label = QLabel('Xlabel')
        self.ylabel_label = QLabel('Ylabel')
        self.title_label = QLabel('Title')
        self.xlabel_edit = QLineEdit()
        self.ylabel_edit = QLineEdit()
        self.title_edit = QLineEdit()
        self.legend_label = QLabel('Legend')
        self.legend_edit = QLineEdit()
        self.col_label = QLabel("Column")
        self.col_edit = QLineEdit()
        self.col_button = QPushButton('Sort')
        self.search_label = QLabel("Find What")
        self.search_edit = QLineEdit()
        self.search_button = QPushButton('Search')
        self.para_combox = QComboBox()
        self.para_label = QLabel("Parameter")
        self.ch_combox = QComboBox()
        self.ch_label = QLabel("CH Num")
        self.test_combox = QComboBox()
        self.test_label = QLabel("Test Name")
        self.plot_combox = QComboBox()
        self.plot_label = QLabel("Plot Func")
        self.plot_edit = QLineEdit()
        self.plot_button = QPushButton("Plot")
        self.open_edit = QLineEdit()
        self.open_button = QPushButton("Open")
        self.plot_combox.addItems(["LinePlot", "BoxPlot", "BoxenPlot", "violinplot", "BarPlot", "HistPlot", "Swarmplot",
                                   "Scatterplot", "Pairplot", "Pieplot", "Otherplot", "All Function"])

    def table_init(self):
        tablerow = 35
        tablecol = 10
        self.model = QStandardItemModel(tablerow, tablecol, self)
        self.table.setModel(self.model)
        self.table.resizeColumnsToContents()
        self.table.horizontalHeader().setSectionsMovable(True)
        self.table.horizontalHeader().setDragEnabled(True)
        self.table.horizontalHeader().setDragDropMode(QAbstractItemView.InternalMove)
        self.table.horizontalHeader().setStretchLastSection(True)  # 最后一列决定充满剩下的界面
        self.table.setEditTriggers(QAbstractItemView.DoubleClicked)
        # 将右键菜单绑定到槽函数generateMenu
        self.table.setContextMenuPolicy(Qt.CustomContextMenu)
        self.table.customContextMenuRequested.connect(self.generateMenu)

    def part_size_init(self):
        self.col_button.setFixedWidth(65)
        self.search_button.setFixedWidth(65)
        self.plot_button.setFixedWidth(65)
        self.open_edit.setFixedWidth(150)
        self.open_button.setFixedWidth(65)
        self.plot_label.setFixedWidth(105)
        self.plot_edit.setFixedWidth(270)
        self.para_label.setFixedWidth(110)
        self.para_combox.setFixedWidth(200)
        self.test_label.setFixedWidth(110)
        self.ch_label.setFixedWidth(105)
        self.ch_combox.setFixedWidth(140)
        self.plot_combox.setFixedWidth(160)
        self.search_edit.setFixedWidth(120)

    def part_position_init(self):
        self.h_table_layout = QHBoxLayout()
        self.combox_layout = QHBoxLayout()
        self.combox_layout.addWidget(self.para_label)
        self.combox_layout.addWidget(self.para_combox)
        self.combox_layout.addSpacing(10)
        self.combox_layout.addWidget(self.test_label)
        self.combox_layout.addWidget(self.test_combox)
        self.combox_layout.addSpacing(10)
        self.combox_layout.addWidget(self.ch_label)
        self.combox_layout.addWidget(self.ch_combox)
        self.combox_layout.addSpacing(10)
        self.combox_layout.addWidget(self.plot_label)
        self.combox_layout.addWidget(self.plot_combox)
        self.combox_layout.addWidget(self.plot_edit)
        self.combox_layout.addWidget(self.plot_button)
        self.combox_layout.addSpacing(10)
        self.combox_layout.addWidget(self.open_edit)
        self.combox_layout.addWidget(self.open_button)
        self.combox_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.vmin_label)
        self.h_table_layout.addWidget(self.vmin_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.vmax_label)
        self.h_table_layout.addWidget(self.vmax_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.title_label)
        self.h_table_layout.addWidget(self.title_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.xlabel_label)
        self.h_table_layout.addWidget(self.xlabel_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.ylabel_label)
        self.h_table_layout.addWidget(self.ylabel_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.legend_label)
        self.h_table_layout.addWidget(self.legend_edit)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.col_label)
        self.h_table_layout.addWidget(self.col_edit)
        self.h_table_layout.addWidget(self.col_button)
        self.h_table_layout.addSpacing(10)
        self.h_table_layout.addWidget(self.search_label)
        self.h_table_layout.addWidget(self.search_edit)
        self.h_table_layout.addWidget(self.search_button)
        self.h_table_layout.addSpacing(10)
        self.v_layout = QVBoxLayout()
        self.v_layout.addLayout(self.combox_layout)
        self.v_layout.addLayout(self.h_table_layout)
        self.v_layout.addWidget(self.table)
        self.setLayout(self.v_layout)

    def part_qss_init(self):
        self.setStyleSheet('background-color:#6CA6CD;font:22px;font-family:Times New Roman;color:#000000')
        label_qss = 'font:22px;background-color:#E4EBF8;font-family:Times New Roman;color:#2A3D62;border: 1px solid White;border-radius: 3px'
        edit_line_qss = 'QLineEdit{font:20px;font-family:Times New Roman;color:#000000;border: 1px solid White;;border-radius: 2px}' \
                        'QLineEdit:hover{font:20px;font-family:Times New Roman;color:#000000;border: 1px solid #D990FB;;border-radius: 2px}'
        button_open_qss = 'QPushButton{font:23px;background-color:#4F688F;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-bottom:2px outset #000010;border-right:2px outset #000010}' \
                          'QPushButton:hover{font:23px;background-color:#4F688F;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border:1px outset #FCFCFC}' \
                          'QPushButton:pressed{font:23px;background-color:#4F688F;font-family:Times New Roman;color:#FFFFFF;border-radius: 2px;border-left:2px outset #000010;border-top:2px outset #000010}'

        self.vmin_label.setStyleSheet(label_qss)
        self.vmax_label.setStyleSheet(label_qss)
        self.xlabel_label.setStyleSheet(label_qss)
        self.ylabel_label.setStyleSheet(label_qss)
        self.title_label.setStyleSheet(label_qss)
        self.para_label.setStyleSheet(label_qss)
        self.ch_label.setStyleSheet(label_qss)
        self.test_label.setStyleSheet(label_qss)
        self.vmin_edit.setStyleSheet(edit_line_qss)
        self.vmax_edit.setStyleSheet(edit_line_qss)
        self.xlabel_edit.setStyleSheet(edit_line_qss)
        self.ylabel_edit.setStyleSheet(edit_line_qss)
        self.title_edit.setStyleSheet(edit_line_qss)
        self.legend_label.setStyleSheet(label_qss)
        self.legend_edit.setStyleSheet(edit_line_qss)
        self.col_label.setStyleSheet(label_qss)
        self.col_edit.setStyleSheet(edit_line_qss)
        self.col_button.setStyleSheet(button_open_qss)
        self.search_label.setStyleSheet(label_qss)
        self.search_edit.setStyleSheet(edit_line_qss)
        self.search_button.setStyleSheet(button_open_qss)
        self.plot_label.setStyleSheet(label_qss)
        self.plot_edit.setStyleSheet(edit_line_qss)
        self.plot_button.setStyleSheet(button_open_qss)
        self.open_edit.setStyleSheet(edit_line_qss)
        self.open_button.setStyleSheet(button_open_qss)
        self.table.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

    def part_func_init(self):
        shortcut = QShortcut(QKeySequence('Ctrl+f'), self)
        shortcut.activated.connect(self.handleFind)
        self.tname_for_combox, self.df_all, self.len_CH = self.write_table(MyThread_0.result_useinfo_allfile,
                                                                           MyThread_0.list_cH_para_allfile,
                                                                           MyThread_0.list_testclassname_allfile,
                                                                           MyThread_0.path_para,
                                                                           MyThread_0.list_allfilename)
        self.para_combox.activated.connect(self.fun_para_combox)
        self.col_button.clicked.connect(self.sort_by_col)
        self.search_button.clicked.connect(lambda: self.search_table(self.search_edit.text().strip()))
        self.plot_button.clicked.connect(lambda *args: self.plot_func(self.df_all, self.tname_for_combox))
        self.open_button.clicked.connect(self.open_func)
        self.df_all.to_csv('filename.csv')

    def plot_func(self, df_all, tname_for_combox):
        if self.open_mode == 0:
            df_all = self.data_range_set(df_all)
            para_index = self.para_combox.currentIndex()
            para_num = self.para_combox.count()-1
            testname_index = self.test_combox.currentIndex()
            testname_num = self.test_combox.count()-1
            ch_index = self.ch_combox.currentIndex()
            ch_num = self.ch_combox.count()-1
            plot_index = self.plot_combox.currentIndex()+1
            len_tname_combox = []
            for x in tname_for_combox:
                len_tname_combox.append(len(x))
            data = []
            para_section = []
            if para_index == para_num:
                if ch_index == ch_num:
                    for p_index in range(para_num):
                        for t_index in range(len_tname_combox[p_index]):
                            para_section.append(self.para_combox.itemText(p_index))
                            df_section_para = df_all.iloc[:, ((sum(len_tname_combox[0:p_index]) + t_index) * ch_num + 0):
                                                         ((sum(len_tname_combox[0:p_index]) +
                                                           t_index) * ch_num + ch_index)]
                            data.append(df_section_para)
                else:
                    for p_index in range(para_num):
                        for t_index in range(len_tname_combox[p_index]):
                            para_section.append(self.para_combox.itemText(p_index))
                            df_section_para = df_all.iloc[:, [((sum(len_tname_combox[0:p_index]) + t_index) *
                                                               ch_num + ch_index)]]
                            data.append(df_section_para)
            else:
                if testname_index == testname_num:
                    if ch_index == ch_num:
                        for t_index in range(len_tname_combox[para_index]):
                            para_section.append(self.para_combox.itemText(para_index))
                            df_section_para = df_all.iloc[:, ((sum(len_tname_combox[0:para_index]) + t_index) * ch_num + 0):
                                                         ((sum(len_tname_combox[0:para_index]) +
                                                           t_index) * ch_num + ch_index)]
                            data.append(df_section_para)
                    else:
                        for t_index in range(len_tname_combox[para_index]):
                            para_section.append(self.para_combox.itemText(para_index))
                            df_section_para = df_all.iloc[:, [((sum(len_tname_combox[0:para_index]) + t_index) *
                                                           ch_num + ch_index)]]
                            data.append(df_section_para)
                else:
                    if ch_index == ch_num:
                        df_section_para = df_all.iloc[:, ((sum(len_tname_combox[0:para_index]) + testname_index) * ch_num + 0):
                                                    ((sum(len_tname_combox[0:para_index]) + testname_index) * ch_num + ch_index)]
                    else:
                        df_section_para = df_all.iloc[:, [(sum(len_tname_combox[0:para_index]) + testname_index) * ch_num + ch_index]]
                    data.append(df_section_para)
            if self.plot_edit.text().strip() == '':
                self.plot_choose(data, plot_index, para_section)
            else:
                try:
                    scope = {}
                    exec(self.plot_edit.text()) in scope
                except:
                    print("Please input the right Plot function")
        else:
            a = self.table.selectedIndexes()
            if len(a) > 1:
                data_dict = {}
                for index in a:
                    if index.data():
                        col = index.column()
                        if col in data_dict.keys():
                            data_dict[col].append(index.data())
                        else:
                            data_dict[col] = [index.data()]
                    else:
                        pass
                data_list = list(data_dict.values())
                try:
                    data = [np.array(list(map(float, x))) for x in data_list]
                    data = pd.DataFrame(data)
                    print('dataaa: ',data)
                    data = data.apply(pd.to_numeric, errors='coerce')
                    data = self.data_range_set(data)
                    data = [data.T]
                except:
                    print('please choose number1, not str' + '\n')
                    return
            else:
                data = self.data_read
                data = self.data_range_set(data)
                try:
                    scope = {}
                    exec(self.plot_edit.text()) in scope
                except:
                    print("Please input the right Plot function")

    def open_func(self):
        try:
            if self.open_edit.text().strip() == '':
                sheet_name = 0
                header = 0
                index_col = 0
            else:
                sheet_name, header, index_col = self.open_edit.text().split(";")
                try:
                    sheet_name = int(sheet_name)
                except:
                    pass
                try:
                    index_col = int(index_col)
                except:
                    pass
                try:
                    header = int(header)
                except:
                    pass
            file_name, file_type = QFileDialog.getOpenFileName(self, '选择文件', './', 'files(*.xlsx , *.xls , *.XLS , *.csv , *.CSV)')
            if file_name.endswith('xlsx') or file_name.endswith('xls') or file_name.endswith('XLS'):
                data = pd.read_excel(file_name, sheet_name=sheet_name, header=header, names=None, index_col=index_col, usecols=None,
                                         squeeze=False, dtype=None, engine='openpyxl', converters=None, true_values=None,
                                         false_values=None, skiprows=None, nrows=None, na_values=None,
                                         keep_default_na=True, verbose=False, parse_dates=False, date_parser=None,
                                         thousands=None, comment=None, skipfooter=0, convert_float=True,
                                         mangle_dupe_cols=True)
            elif file_name.endswith('csv') or file_name.endswith('CSV'):
                data = pd.read_csv(file_name, sep=',', delimiter=None, header=header, names=None, index_col=index_col,
                                       usecols=None, squeeze=False, prefix=None, mangle_dupe_cols=True, dtype=None,
                                       engine=None, converters=None, true_values=None, false_values=None,
                                       skipinitialspace=False, skiprows=None, skipfooter=0, nrows=None, na_values=None,
                                       keep_default_na=True, na_filter=True, verbose=False, skip_blank_lines=True,
                                       parse_dates=False, infer_datetime_format=False, keep_date_col=False,
                                       date_parser=None, dayfirst=False, cache_dates=True, iterator=False, chunksize=None,
                                       compression='infer', thousands=None, decimal = '.', lineterminator=None,
                                       quotechar='"', quoting=0, doublequote=True, escapechar=None, comment=None,
                                       encoding=None, dialect=None, error_bad_lines=True, warn_bad_lines=True,
                                       delim_whitespace=False, low_memory=True, memory_map=False, float_precision=None)
            else:
                pass
            model = pandasModel(data)
            self.table.setModel(model)
            self.open_mode = 1
            self.data_read = data
        except:
            self.open_mode = 0
            print("Please choose the file you want to open")

    def sort_by_col(self):
        self.sort_num = self.sort_num + 1
        col = self.col_edit.text()
        try:
            if col.strip() == '':
                pass
            else:
                col = int(col)
                if self.sort_num == 1:
                    self.table.setSortingEnabled(True)
                    self.table.sortByColumn(col-1, Qt.AscendingOrder)
                else:
                    self.table.setSortingEnabled(True)
                    self.table.sortByColumn(col-1, Qt.DescendingOrder)
                    self.sort_num = 0
        except:
            print('please input serial number, not str' + '\n')
            return

    def handleFind(self):
        self.findDialog = QDialog()
        self.findDialog.setWindowTitle("Search")
        self.findLabel = QLabel("Find what:", self.findDialog)
        self.findField = QLineEdit(self.findDialog)
        self.findButton = QPushButton("Find all", self.findDialog)
        self.upButton = QPushButton("Up", self.findDialog)
        self.downButton = QPushButton("Down", self.findDialog)

        grid = QGridLayout()
        grid.addWidget(self.findLabel, 0, 0, 1, 1)
        grid.addWidget(self.findField, 0, 1, 1, 2)
        grid.addWidget(self.findButton, 1, 0, 1, 1)
        grid.addWidget(self.upButton, 1, 1, 1, 1)
        grid.addWidget(self.downButton, 1, 2, 1, 1)
        self.findDialog.setLayout(grid)

        TableWin.pos_save = []
        TableWin.pos_updown = -1

        self.findField.textChanged.connect(self.para_init)
        self.findButton.clicked.connect(
            lambda: self.search_table(self.findField.text().strip()))
        self.upButton.clicked.connect(
            lambda: self.upfind(self.findField.text().strip()))
        self.downButton.clicked.connect(
            lambda: self.downfind(self.findField.text().strip()))
        self.findDialog.setModal(False)
        self.findDialog.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.findDialog.show()

    def para_init(self):
        TableWin.pos_save = []
        TableWin.pos_updown = -1

    def upfind(self, search_content):
        row_num = self.model.rowCount()
        col_num = self.model.columnCount()
        if search_content == "":
            pass
        else:
            for row in range(row_num):
                for col in range(col_num):
                    if self.model.index(row, col).data() is None:
                        pass
                    else:
                        if search_content.lower() in self.model.index(row, col).data().lower():
                            TableWin.pos_save.append([row,col])
                        else:
                            self.model.item(row, col).setBackground(QColor(240, 255, 240))  # F0FFF0

        if TableWin.pos_save:
            for i, [row, col] in enumerate(TableWin.pos_save):
                self.model.item(row, col).setBackground(QColor(240, 255, 240))  # F0FFF0

            if TableWin.pos_updown == -1:
                TableWin.pos_updown = 0
            elif TableWin.pos_updown == 0:
                TableWin.pos_updown = len(TableWin.pos_save) - 1
            else:
                TableWin.pos_updown = TableWin.pos_updown - 1
            row = TableWin.pos_save[TableWin.pos_updown][0]
            col = TableWin.pos_save[TableWin.pos_updown][1]
            self.model.item(row, col).setBackground(QColor(255, 153, 153))
            self.table.verticalScrollBar().setSliderPosition(row)
            self.table.horizontalScrollBar().setSliderPosition(col)
        else:
            pass

    def downfind(self, search_content):
        row_num = self.model.rowCount()
        col_num = self.model.columnCount()
        if search_content == "":
            pass
        else:
            for row in range(row_num):
                for col in range(col_num):
                    if self.model.index(row, col).data() is None:
                        pass
                    else:
                        if search_content.lower() in self.model.index(row, col).data().lower():
                            TableWin.pos_save.append([row, col])
                        else:
                            self.model.item(row, col).setBackground(QColor(240, 255, 240))  # F0FFF0

        if TableWin.pos_save:
            for i, [row, col] in enumerate(TableWin.pos_save):
                self.model.item(row, col).setBackground(QColor(240, 255, 240))  # F0FFF0

            if TableWin.pos_updown == -1:
                TableWin.pos_updown = 0
            elif TableWin.pos_updown == len(TableWin.pos_save) - 1:
                TableWin.pos_updown = 0
            else:
                TableWin.pos_updown = TableWin.pos_updown + 1
            row = TableWin.pos_save[TableWin.pos_updown][0]
            col = TableWin.pos_save[TableWin.pos_updown][1]
            self.model.item(row, col).setBackground(QColor(255, 153, 153))
            self.table.verticalScrollBar().setSliderPosition(row)
            self.table.horizontalScrollBar().setSliderPosition(col)
        else:
            pass

    def search_table(self,search_content):
        row_num = self.model.rowCount()
        col_num = self.model.columnCount()
        if search_content == "":
            pass
        else:
            i = 0
            for row in range(row_num):
                for col in range(col_num):
                    if self.model.index(row,col).data() is None:
                        pass
                    else:
                        if search_content.lower() in self.model.index(row,col).data().lower():
                            i = i + 1
                            self.model.item(row, col).setBackground(QColor(255,153,153)) #FF9999
                            if i == 1:
                                self.table.verticalScrollBar().setSliderPosition(row)
                                self.table.horizontalScrollBar().setSliderPosition(col)
                            else:
                                pass
                        else:
                            self.model.item(row, col).setBackground(QColor(240,255,240)) #F0FFF0

    def write_table(self, data_allfile_allpara, cH_allfile_allpara, testname_allfile_allpara, name_para, list_allfilename):
        print('Show result in table')
        ## 综合所有文件确定testname的总体情况
        testname_para_total = []
        len_testname_total = 0
        len_testname_para_total = [0]
        for para_num in range(len(name_para)):
            testname_total = []
            for file_num, file_data in enumerate(testname_allfile_allpara):
                if file_num < 20:  # 最多只查找20个文件，为了节省时间
                    testname_total = testname_total + file_data[para_num]
                else:
                    break
            sort_testname_total = sorted(set(testname_total), key=testname_total.index)
            dict_testname_total = dict(zip(sort_testname_total, range(len(sort_testname_total))))
            testname_para_total.append(dict_testname_total)
            len_testname_total = len_testname_total + len(sort_testname_total)
            len_testname_para_total.append(len_testname_total)


        ## 综合所有文件确定CH的总体情况
        CH_total = []
        for para_num in range(len(name_para)):
            for file_num, file_data in enumerate(cH_allfile_allpara):
                if file_num < 20:  # 最多只查找20个文件，为了节省时间
                    CH_total.extend(file_data[para_num])
                else:
                    break
        sort_CH_total = sorted(set(CH_total), key=CH_total.index)
        len_CH = len(sort_CH_total)

        if data_allfile_allpara == []:
            df1 = pd.DataFrame([0])
        else:
            df = pd.DataFrame(data_allfile_allpara)
            df1 = pd.concat([df[i].apply(pd.Series) for i in range(df.shape[1])], axis=1)
            column_list = list(itertools.chain.from_iterable(list(itertools.chain.from_iterable(cH_allfile_allpara[0]))))
            if len(column_list) == df1.shape[1]:
                df1.columns = [('CH'+ str(ch_num)) for ch_num in column_list]
            else:
                df1.columns = [('CH'+ str(ch_num)) for ch_num in ([i for i in range(len_CH)] * (df1.shape[1] // len_CH) +
                               [i for i in range(len_CH)][0:(df1.shape[1] % len_CH)])]
            df1 = df1.apply(pd.to_numeric, errors='coerce')

        # 确定combox的选项
        self.ch_combox.addItems(sort_CH_total)
        self.ch_combox.addItem("All CH")
        self.para_combox.addItems(name_para)
        self.para_combox.addItem("All Parameter")
        if len(testname_para_total) > 0:
            self.test_combox.addItems(list(testname_para_total[0].keys()))
            self.test_combox.addItem("All TestName")
        else:
            pass


        ## 根据CH的类型来写参数名称和位置
        if len_CH == 1:
            value_col_paraname_None = 3
            for para_num, para_data in enumerate(name_para):
                self.model.setItem(0, 0, QStandardItem("SN"))
                self.model.setItem(0, 1, QStandardItem("Parameter"))
                self.model.setItem(0, value_col_paraname_None-1, QStandardItem(str(para_data)))
                value_col_paraname_None = value_col_paraname_None + 1 + (len_CH + 1) * (
                    len(testname_para_total[para_num]))
        else:
            value_col_paraname_Num = 3
            value_col_CH_Num = 3
            for para_num, para_data in enumerate(name_para):
                self.model.setItem(0, 0, QStandardItem("SN"))
                self.model.setItem(0, 1, QStandardItem("Parameter"))
                self.model.setItem(1, 1, QStandardItem("Channel"))
                self.model.setItem(0, value_col_paraname_Num-1, QStandardItem(str(para_data)))
                value_col_paraname_Num = value_col_paraname_Num + 1 + (len_CH + 1) * (
                    len(testname_para_total[para_num]))
            for test_num, test_data in enumerate(testname_para_total):
                for col in range(len_CH * len(testname_para_total[test_num])):
                    self.model.setItem(1, value_col_CH_Num-1 + col + col // len_CH, QStandardItem('CH' + str(col % len_CH)))
                value_col_CH_Num = value_col_CH_Num + (len_CH + 1) * len(testname_para_total[test_num]) + 1

        ## 根据CH的类型来确定数据的位置
        value_row_CH_None = 0
        value_row_CH_Num = 0
        if len_CH == 1:  # 当为单通道时
            for file_num, file_data in enumerate(data_allfile_allpara):
                self.model.setItem(2 + value_row_CH_None-1, 0, QStandardItem(str(list_allfilename[file_num])))
                for para_num, para_data in enumerate(file_data):
                    if para_data == []:
                        pass
                    else:
                        for col, data in enumerate(para_data):
                            # 写数据
                            item = QStandardItem(str(data))
                            self.model.setItem(2 + value_row_CH_None-1, 3-1 + (len_CH + 1) * (int(
                                testname_para_total[para_num].get(
                                    testname_allfile_allpara[file_num][para_num][col]))) + (len_CH + 1) *
                                    len_testname_para_total[para_num] + para_num,
                                               item)
                            # 写testclass
                            self.model.setItem(2 + value_row_CH_None-1, 2-1 +(len_CH + 1) * (int(
                                testname_para_total[para_num].get(
                                    testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH + 1) * len_testname_para_total[para_num] + para_num,
                                               QStandardItem(str(testname_allfile_allpara[file_num][para_num][col])))
                value_row_CH_None = value_row_CH_None + 1
        else:  # 当为多通道时
            for file_num, file_data in enumerate(data_allfile_allpara):
                self.model.setItem(3 + value_row_CH_Num-1, 0, QStandardItem(str(list_allfilename[file_num])))
                for para_num, para_data in enumerate(file_data):
                    if para_data == []:
                        pass
                    else:
                        for col, data in enumerate(para_data):
                            # 写数据
                            self.model.setItem(3 + value_row_CH_Num-1, 3-1 +(len_CH + 1) * (int(
                                testname_para_total[para_num].get(
                                    testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH + 1) * len_testname_para_total[para_num] + int(
                                cH_allfile_allpara[file_num][para_num][col]) + para_num,
                                               QStandardItem(str(data)))

                            # 写testclass
                            self.model.setItem(3 + value_row_CH_Num-1, 2-1 +(len_CH + 1) * (int(
                                testname_para_total[para_num].get(
                                    testname_allfile_allpara[file_num][para_num][col]))) +
                                    (len_CH + 1) * len_testname_para_total[para_num] + para_num,
                                               QStandardItem(str(testname_allfile_allpara[file_num][para_num][col])))
                value_row_CH_Num = value_row_CH_Num + 1
        return testname_para_total, df1, len_CH

    def fun_para_combox(self, index):
        self.test_combox.clear()
        if index == self.para_combox.count()-1:
            pass
        else:
            self.test_combox.addItems(list(self.tname_for_combox[index].keys()))
        self.test_combox.addItem("All TestName")

    def generateMenu(self, pos):
        menu = QMenu()
        act_item1 = menu.addAction(u'折线图')
        act_item2 = menu.addAction(u'箱图')
        act_item3 = menu.addAction(u'增强型箱图')
        act_item4 = menu.addAction(u'小提琴图')
        menu_item5 = menu.addMenu(u'柱状图')
        act_item5_1 = menu_item5.addAction(u'所有值')
        act_item5_2 = menu_item5.addAction(u'平均值')
        act_item5_3 = menu_item5.addAction(u'中值')
        act_item6 = menu.addAction(u'直方图')
        act_item7 = menu.addAction(u'蜂群散点图')
        act_item8 = menu.addAction(u'散点图')
        act_item9 = menu.addAction(u'对图')
        act_item10 = menu.addAction(u'扇形图')
        act_item11 = menu.addAction(u'其它图')
        act_item12 = menu.addAction(u'所有图')

        action = menu.exec_(self.table.mapToGlobal(pos))
        # 显示选中行的数据文本
        if action == act_item1:
            self.show_info(1)
        if action == act_item2:
            self.show_info(2)
        if action == act_item3:
            self.show_info(3)
        if action == act_item4:
            self.show_info(4)
        if action == act_item5_1:
            self.show_info(55)
        if action == act_item5_2:
            self.show_info(5)
        if action == act_item5_3:
            self.show_info(555)
        if action == act_item6:
            self.show_info(6)
        if action == act_item7:
            self.show_info(7)
        if action == act_item8:
            self.show_info(8)
        if action == act_item9:
            self.show_info(9)
        if action == act_item10:
            self.show_info(10)
        if action == act_item11:
            self.show_info(11)
        if action == act_item12:
            self.show_info(12)

    def data_range_set(self, data):
        try:
            vmin = self.vmin_edit.text()
            vmax = self.vmax_edit.text()
            if vmin.strip() == '':
                vmin = None
            else:
                vmin = float(vmin)
            if vmax.strip() == '':
                vmax = None
            else:
                vmax = float(vmax)
            if vmin == None and vmax == None:
                pass
            elif vmin == None:
                data = data[data < vmax]
            elif vmax == None:
                data = data[data > vmin]
            else:
                data = data[(data > vmin) & (data < vmax)]
            return data
        except:
            print("failed to set data range")
            return None

    def show_info(self, fun_num=1):  # 7
        a = self.table.selectedIndexes()
        data_dict = {}
        for index in a:
            if index.data():
                col = index.column()
                if col in data_dict.keys():
                    data_dict[col].append(index.data())
                else:
                    data_dict[col] = [index.data()]
            else:
                pass
        data_list = list(data_dict.values())
        try:
            data = [np.array(list(map(float, x))) for x in data_list]
            data = pd.DataFrame(data)
            data = data.apply(pd.to_numeric, errors='coerce')
            data = self.data_range_set(data)
            data = [data.T]
            self.plot_choose(data, fun_num)
        except:
            print('please choose number, not str' + '\n')
            return

    def plot_choose(self, data, fun_num, para_section = None):
        try:
            title_name = self.title_edit.text().strip()
            xlabel_name = self.xlabel_edit.text().strip()
            ylabel_name = self.ylabel_edit.text().strip()
            label_legend = self.legend_edit.text().strip()
            if title_name == '':
                title_name = None
            else:
                title_name = list(title_name.split(";"))
            if xlabel_name == '':
                xlabel_name = None
            else:
                xlabel_name = list(xlabel_name.split(";"))
            if ylabel_name == '':
                ylabel_name = None
            else:
                ylabel_name = list(ylabel_name.split(";"))
            if label_legend == '':
                label_legend = None
            else:
                label_legend = list(label_legend.split(";"))
            if fun_num == 1:
                self.lineplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 2:
                self.boxplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 3:
                self.boxenplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 4:
                self.violinplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 5 or fun_num == 55 or fun_num == 555:
                self.barplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name, fun_num)
            elif fun_num == 6:
                self.histplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 7:
                self.swarmplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 8:
                self.scatterplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 9:
                self.pairplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 10:
                self.pieplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 11:
                self.otherplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name)
            elif fun_num == 12:
                self.allplot(data, label_legend, para_section, title_name, xlabel_name, ylabel_name, fun_num)
            else:
                pass
        except:
            print('Can not plot figure' + '\n')
            return

    def lineplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            plt.figure(dpi=120)
            sns.set(style="whitegrid")
            sns.lineplot(x=None, y=None, hue=None, size=None, style=None, data=data, palette="tab10", hue_order=None,
                             hue_norm=None, sizes=None, size_order=None, size_norm=None, dashes=True, markers=None,
                             style_order=None, units=None, estimator='mean', ci=95, n_boot=1000, sort=True,
                             err_style='band', err_kws=None, legend='full', linewidth=2.5, ax=None)
            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules", fontdict={'family' : 'Times New Roman', 'size' : 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Module Num', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\lineplot_" + str(i_name) + r".png")
        plt.show()

    def boxplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            plt.figure(dpi=120)
            sns.set(style="whitegrid")
            sns.boxplot(x=None, y=None, hue=None, data=data, order=None, hue_order=None, orient=None, color=None,
                            palette='tab10', saturation=0.75, width=0.8, dodge=True, fliersize=5, linewidth=None, whis=1.5,
                            notch=False, ax = None)

            # sns.factorplot(x=None, y=None, hue=None, data=data, row=None, col=None, col_wrap=None,
            #                ci = 95, n_boot = 1000, units = None, order = None, estimator = mean,
            #                hue_order = None, row_order = None,col_order = None, kind = 'box', size = 4, aspect = 1,
            #                orient = None, color = None, palette = 'tab10', legend = True, legend_out = True, sharex = True,
            #                sharey = True, margin_titles = False, facet_kws = None)

            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules",
                              fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Channel', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            # ax.grid()
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\boxplot_" + str(i_name) + r".png")
        plt.show()

    def boxenplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            plt.figure(dpi=120)
            sns.set(style="whitegrid")
            sns.boxenplot(x=None, y=None, hue=None, data=data, order=None, hue_order=None, orient=None, color=None,
                              palette=None, saturation=0.75, width=0.8, dodge=True, k_depth='proportion',
                              linewidth=None, scale='exponential', outlier_prop=None, ax=None)
            # sns.factorplot(x=None, y=None, hue=None, data=data, row=None, col=None, col_wrap=None,
            #                ci = 95, n_boot = 1000, units = None, order = None, estimator = mean,
            #                hue_order = None, row_order = None,col_order = None, kind = 'box', size = 4, aspect = 1,
            #                orient = None, color = None, palette = 'tab10', legend = True, legend_out = True, sharex = True,
            #                sharey = True, margin_titles = False, facet_kws = None)

            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules",
                              fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Channel', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            # ax.grid()
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\boxenplot_" + str(i_name) + r".png")
        plt.show()

    def violinplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            plt.figure(dpi=120)
            sns.set(style="whitegrid")
            sns.violinplot(x=None, y=None, hue=None, data=data, order=None, hue_order=None, bw='scott', cut=2,
                               scale='area', scale_hue=True, gridsize=100, width=0.8, inner='box', split=False,
                               dodge=True, orient=None, linewidth=None, color=None, palette='tab10', saturation=0.75,
                               ax=None)

            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules",
                              fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Channel', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            # ax.grid()
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\violinplot_" + str(i_name) + r".png")
        plt.show()

    def barplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None, fun_num = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            if fun_num == 55:
                data.plot(kind='bar', ax=None, colormap='cool', grid = True)
            elif fun_num == 5:
                data.mean(0).plot(kind='bar', ax=None, colormap='cool', grid = True)
            elif fun_num == 555:
                data.mean(1).plot(kind='bar', ax=None, colormap='cool', grid = True)
            else:
                pass
            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules",
                              fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Channel', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\barplot_" + str(i_name) + r".png")
        plt.show()

    def histplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            for i, col in enumerate(data.columns):
                plt.figure(dpi=120)
                sns.distplot(np.array(data.iloc[:,[i]]), bins=20, hist=True, kde=True, rug=False, fit=None, hist_kws=None, kde_kws=None,
                                 rug_kws=None, fit_kws=None, color=None, vertical=False, norm_hist=False, axlabel=None,
                                 label=data.columns[i], ax=None)

                if not title_name:
                    if para_section:
                        plt.title(para_section[para_index] + " of Modules",
                                  fontdict={'family': 'Times New Roman', 'size': 18})
                    else:
                        plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

                if not ylabel_name:
                    if para_section:
                        plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                    else:
                        plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                if not xlabel_name:
                    plt.xlabel('Module Num', fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                plt.yticks(fontproperties='Times New Roman', size=14)
                plt.xticks(fontproperties='Times New Roman', size=14)
                plt.legend(prop={'family': 'Times New Roman', 'size': 14})
                if not label:
                    pass
                else:
                    plt.legend([label_num for label_num in label])
                i_name = i_name + 1
                plt.savefig(MyThread_0.path_txtsave_image + r"\histplot_" + str(i_name) + r".png")
        plt.show()

    def swarmplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            plt.figure(dpi=120)
            sns.set(style="whitegrid")
            sns.swarmplot(x=None, y=None, hue=None, data=data, order=None, hue_order=None, dodge=False, orient=None,
                              color=None, palette='tab10', size=5, edgecolor='gray', linewidth=0, ax=None)

            # sns.factorplot(x=None, y=None, hue=None, data=data, row=None, col=None, col_wrap=None,
            #                ci = 95, n_boot = 1000, units = None, order = None, estimator = mean,
            #                hue_order = None, row_order = None,col_order = None, kind = 'box', size = 4, aspect = 1,
            #                orient = None, color = None, palette = 'tab10', legend = True, legend_out = True, sharex = True,
            #                sharey = True, margin_titles = False, facet_kws = None)


            '''
            Parameters：
                x,y,hue 数据集变量 变量名
                date 数据集 数据集名
                row,col 更多分类变量进行平铺显示 变量名
                col_wrap 每行的最高平铺数 整数
                estimator 在每个分类中进行矢量到标量的映射 矢量
                ci 置信区间 浮点数或None
                n_boot 计算置信区间时使用的引导迭代次数 整数
                units 采样单元的标识符，用于执行多级引导和重复测量设计 数据变量或向量数据
                order, hue_order 对应排序列表 字符串列表
                row_order, col_order 对应排序列表 字符串列表
                kind : 可选：point 默认, bar 柱形图, count 频次, box 箱体, violin 提琴, strip 散点，
                swarm 分散点（具体图形参考文章前部的分类介绍）
                size 每个面的高度（英寸） 标量
                aspect 纵横比 标量
                orient 方向 "v"/"h"
                color 颜色 matplotlib颜色
                palette 调色板 seaborn颜色色板或字典
                legend hue的信息面板 True/False
                legend_out 是否扩展图形，并将信息框绘制在中心右边 True/False
                share{x,y} 共享轴线 True/False
                facet_kws FacetGrid的其他参数 字典
            '''

            if not title_name:
                if para_section:
                    plt.title(para_section[para_index] + " of Modules",
                              fontdict={'family': 'Times New Roman', 'size': 18})
                else:
                    plt.title("Title", fontdict={'family': 'Times New Roman', 'size': 18})
            else:
                plt.title(title_name[para_index], fontdict={'family': 'Times New Roman', 'size': 18})

            if not ylabel_name:
                if para_section:
                    plt.ylabel(para_section[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
                else:
                    plt.ylabel("Value", fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.ylabel(ylabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            if not xlabel_name:
                plt.xlabel('Channel', fontdict={'family': 'Times New Roman', 'size': 16})
            else:
                plt.xlabel(xlabel_name[para_index], fontdict={'family': 'Times New Roman', 'size': 16})
            plt.yticks(fontproperties='Times New Roman', size=14)
            plt.xticks(fontproperties='Times New Roman', size=14)
            plt.legend(prop={'family': 'Times New Roman', 'size': 14})
            if not label:
                pass
            else:
                plt.legend([label_num for label_num in label])
            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\swarmplot_" + str(i_name) + r".png")
        plt.show()

    def scatterplot(self, data_list, label=None, para_section=None, title_name=None,
                  xlabel_name=None, ylabel_name=None):
        for para_index, data in enumerate(data_list):
            # plt.figure()
            # sns.scatterplot(x=None, y=None, hue=None, style=None, size=None, data=None, palette=None, hue_order=None,
            #                     hue_norm=None, sizes=None, size_order=None, size_norm=None, markers=True, style_order=None,
            #                     x_bins=None, y_bins=None, units=None, estimator=None, ci=95, n_boot=1000, alpha='auto',
            #                     x_jitter=None, y_jitter=None, legend='brief', ax=None)
            pass

    def pairplot(self, data_list, label=None, para_section=None, title_name=None,
                  xlabel_name=None, ylabel_name=None):
        i_name = 0
        for para_index, data in enumerate(data_list):
            # plt.figure()
            sns.set(style="whitegrid")
            # kind：{‘scatter’, ‘reg’}, 可选。
            # diag_kind：{‘auto’, ‘hist’, ‘kde’}, 可选
            sns.pairplot(data, hue=None, hue_order=None, palette="tab10", vars=None, x_vars=None, y_vars=None,
                             kind='reg', diag_kind='kde', markers=None, height=2.5, aspect=1, dropna=True,
                             plot_kws=None, diag_kws=None, grid_kws=None, size=None)

            i_name = i_name + 1
            plt.savefig(MyThread_0.path_txtsave_image + r"\pairplot_" + str(i_name) + r".png")
        plt.show()

    def pieplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        for para_index, data in enumerate(data_list):
            # plt.figure()
            # plt.pie(data, explode=None, labels=None, autopct='%1.1f%%',
            #     shadow=True, startangle=90)
            pass

    def otherplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None):
        pass

    def allplot(self, data_list, label = None, para_section = None, title_name = None,
                 xlabel_name = None, ylabel_name = None, fun_num = None):
        self.lineplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.boxplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.boxenplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.violinplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.barplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name, fun_num)
        self.histplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.swarmplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.scatterplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.pairplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.pieplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)
        self.otherplot(data_list, label, para_section, title_name, xlabel_name, ylabel_name)


class pandasModel(QAbstractTableModel):

    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.index.size

    def columnCount(self, parent=None):
        return self._data.columns.size

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, rowcol, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[rowcol]
        if orientation == Qt.Vertical and role == Qt.DisplayRole:
            return self._data.index[rowcol]
        return None

    def flags(self, index):
        flags = super(self.__class__, self).flags(index)
        flags |= Qt.ItemIsEditable
        flags |= Qt.ItemIsSelectable
        flags |= Qt.ItemIsEnabled
        flags |= Qt.ItemIsDragEnabled
        flags |= Qt.ItemIsDropEnabled
        return flags

    def sort(self, Ncol, order):
        """Sort table by given column number.
        """
        try:
            self.layoutAboutToBeChanged.emit()
            self._data = self._data.sort_values(self._data.columns[Ncol], ascending=not order)
            self.layoutChanged.emit()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.addLibraryPath('./plugins')
    app.processEvents()
    demo = Traceview()
    demo.show()
    time9 = time.time()
    print('time9', time9 - time1)
    sys.exit(app.exec_())






