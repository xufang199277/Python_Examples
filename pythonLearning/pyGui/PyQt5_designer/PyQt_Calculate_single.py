# -*- coding: utf-8 -*-
"""
    【简介】
     单个程序实现科学计算器，按钮批量创建及调用函数
"""
from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton , QWidget, QApplication, QTextEdit
import sys
from functools import partial
import numpy as np
import math
class WinForm(QWidget):
	Calculate_Char_SHOW = ""
	Calculate_Char_SHOW_SAVE = ""
	Calculate_Char_Operation = ""
	Calculate_Char_Operation_SAVE = ""
	Calculate_Char_SHOW_HandInput = ""
	Calculate_Char_SHOW_List = []
	Calculate_Char_SHOW_List_SAVE = []
	Calculate_Char_Operation_List = []
	Calculate_Char_Operation_List_SAVE = []
	PI = math.pi
	E = math.e
	List_Save = 0
	def __init__(self, parent=None):
		super(WinForm, self).__init__(parent)
		self.setWindowTitle("科学计算器_许放")
		self.resize(416, 645)
		self.setMaximumSize(419, 645)
		self.Displaytext = QTextEdit(self)
		self.Displaytext.setGeometry(0, 0, 418, 321)
		font = QFont()
		font.setPointSize(24)
		font.setBold(True)
		font.setWeight(75)
		self.Displaytext.setFont(font)
		font.setPointSize(12)
		# font.setBold(True)
		font.setWeight(75)
		self.pBtn_Dic = {}
		Geometry_X = -83
		Geometry_Y = 275
		pBtn_row = 1
		self.pBtn_i = 0
		self.pBtn_TextList_SHOW_TextEdit = ["2nd", "deg", "sin", "cos", "tan", "pow", "log", ",", "(", ")", "√", "C",
													"del", "%", "/", "X!", "7", "8", "9", "*", "1/", "4", "5", "6", "-", "pi",
													"1", "2", "3", "+", "change", "e", "0", ".", "="]
		self.pBtn_TextList_SHOW_pBtn = ["2nd", "deg", "sin", "cos", "tan", "Xy", "log", ",", "(", ")", "√x", "C",
										"del", "%", "/", "X!", "7", "8", "9", "*", "1/X", "4", "5", "6", "-", "pi",
										"1", "2", "3", "+", "change", "e", "0", ".", "="]
		self.pBtn_TextList_Operation = ["2nd", "math.degrees", "math.sin", "math.cos", "math.tan", "math.pow", "math.log",
										",", "(", ")", "math.sqrt", "C", "del", "%", "/", "X!", "7", "8", "9", "*", "1/", "4",
										"5", "6", "-", "PI", "1", "2", "3", "+", "change", "E", "0", ".", "="]
		for self.pBtn_i in range(35):
			if self.pBtn_i - int(self.pBtn_i / 5) <= 4 * pBtn_row:
				Geometry_X = Geometry_X + 83
				if self.pBtn_i - 5 * int(self.pBtn_i / 5) == 0:
					Geometry_X = 0
					Geometry_Y = Geometry_Y + 46
					pBtn_row = pBtn_row + 1
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)] = QPushButton(self)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setGeometry(Geometry_X, Geometry_Y, 85, 48)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setText(self.pBtn_TextList_SHOW_pBtn[self.pBtn_i])
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setFont(font)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].clicked.connect(partial(self.pBtn_Click_Function ,
																			  self.pBtn_i))
	def pBtn_Click_Function(self,pBtn_Object_Num):
		WinForm.Calculate_Char_SHOW = self.Displaytext.toPlainText()
		if self.Displaytext.toPlainText() == WinForm.Calculate_Char_SHOW_SAVE:
			self.Calculate_PARA_KEY(pBtn_Object_Num)
		else:
			self.Calculate_PARA_HandInput(pBtn_Object_Num)
		WinForm.Calculate_Char_SHOW = ''.join(WinForm.Calculate_Char_SHOW_List)
		WinForm.Calculate_Char_Operation = ''.join(WinForm.Calculate_Char_Operation_List)
		cursor = self.Displaytext.textCursor()
		cursor.movePosition(QtGui.QTextCursor.End)
		if self.Displaytext.toPlainText() == WinForm.Calculate_Char_SHOW_SAVE:
			self.Displaytext.setPlainText(WinForm.Calculate_Char_SHOW)
		else: self.Displaytext.setPlainText(WinForm.Calculate_Char_SHOW_HandInput)
		self.Displaytext.setTextCursor(cursor)
		self.Displaytext.ensureCursorVisible()
		WinForm.Calculate_Char_SHOW_List_SAVE = WinForm.Calculate_Char_SHOW_List
		WinForm.Calculate_Char_SHOW_SAVE = WinForm.Calculate_Char_SHOW
		WinForm.Calculate_Char_Operation_List_SAVE = WinForm.Calculate_Char_Operation_List
		WinForm.Calculate_Char_Operation_SAVE = WinForm.Calculate_Char_Operation

	def Calculate_PARA_HandInput(self,pBtn_Object_Num):
		if self.Displaytext.toPlainText() == "":
			WinForm.Calculate_Char_Operation_List = []
			WinForm.Calculate_Char_SHOW_List = []
		else:
			WinForm.List_Save = len(WinForm.Calculate_Char_SHOW_SAVE) - len(WinForm.Calculate_Char_SHOW)
			if WinForm.List_Save == 0:
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE
			elif WinForm.List_Save > 0:
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE[
														:(-1 * WinForm.List_Save)]
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE[:(-1 * WinForm.List_Save)]
			else:
				WinForm.Calculate_Char_Operation_List_SAVE.append(WinForm.Calculate_Char_SHOW[WinForm.List_Save:])
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE
				WinForm.Calculate_Char_SHOW_List_SAVE.append(WinForm.Calculate_Char_SHOW[WinForm.List_Save:])
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE
		if self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "=":
			WinForm.Calculate_Char_SHOW_HandInput = WinForm.Calculate_Char_SHOW + "\n" + str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List))
			WinForm.Calculate_Char_Operation_List.append(str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List)))
			WinForm.Calculate_Char_SHOW_List.append("\n" + str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List)))
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "C":
			WinForm.Calculate_Char_SHOW_HandInput = "0"
			WinForm.Calculate_Char_SHOW_List = ["0"]
			WinForm.Calculate_Char_Operation_List = ["0"]
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "change":
			pass
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "del":
			if WinForm.Calculate_Char_SHOW == "":
				pass
			else:
				WinForm.Calculate_Char_SHOW_HandInput = ''.join(WinForm.Calculate_Char_SHOW_List[:-1])
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE[:-1]
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE[:-1]
		else:
			if WinForm.Calculate_Char_SHOW == "0":
				WinForm.Calculate_Char_SHOW_HandInput = self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num]
				WinForm.Calculate_Char_SHOW_List[0] = self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num]
				WinForm.Calculate_Char_Operation_List[0] = self.pBtn_TextList_Operation[pBtn_Object_Num]
			else:
				WinForm.Calculate_Char_SHOW_List.append(self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num])
				WinForm.Calculate_Char_Operation_List.append(self.pBtn_TextList_Operation[pBtn_Object_Num])
				WinForm.Calculate_Char_SHOW_HandInput = ''.join(WinForm.Calculate_Char_SHOW_List)

	def Calculate_PARA_KEY(self,pBtn_Object_Num):
		if self.Displaytext.toPlainText() == "":
			WinForm.Calculate_Char_Operation_List = []
			WinForm.Calculate_Char_SHOW_List = []
		else:
			WinForm.List_Save = len(WinForm.Calculate_Char_SHOW_SAVE) - len(WinForm.Calculate_Char_SHOW)
			if WinForm.List_Save == 0:
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE
			else:
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE[
														:(-1 * WinForm.List_Save)]
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE[:(-1 * WinForm.List_Save)]
		if self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "=":
			WinForm.Calculate_Char_SHOW_List.append("\n" + str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List)))
			WinForm.Calculate_Char_Operation_List.append("\n" + str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List)))
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "C":
			WinForm.Calculate_Char_SHOW_List = ["0"]
			WinForm.Calculate_Char_Operation_List = ["0"]
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "change":
			pass
		elif self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num] == "del":
			if WinForm.Calculate_Char_SHOW == "":
				pass
			else:
				WinForm.Calculate_Char_SHOW_List = WinForm.Calculate_Char_SHOW_List_SAVE[:-1]
				WinForm.Calculate_Char_Operation_List = WinForm.Calculate_Char_Operation_List_SAVE[:-1]
		else:
			if WinForm.Calculate_Char_SHOW == "0":
				WinForm.Calculate_Char_SHOW_List[0] = self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num]
				WinForm.Calculate_Char_Operation_List[0] = self.pBtn_TextList_Operation[pBtn_Object_Num]
			else:
				WinForm.Calculate_Char_SHOW_List.append(self.pBtn_TextList_SHOW_TextEdit[pBtn_Object_Num])
				WinForm.Calculate_Char_Operation_List.append(self.pBtn_TextList_Operation[pBtn_Object_Num])

	def Calculate_Function(self,Operation_Expression):
		WinForm.Calculate_Char_Expression = ''.join(Operation_Expression).strip().split("\n").pop()
		WinForm.Calculate_Char_Expression_Value = eval(WinForm.Calculate_Char_Expression)
		return WinForm.Calculate_Char_Expression_Value

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()
	sys.exit(app.exec_())


	# def is_number(self,NumOrNot):
	# 	if NumOrNot == "." or NumOrNot == "(" or NumOrNot == ")":
	# 		return True
	# 	try:  # 如果能运行float(s)语句，返回True（字符串s是浮点数）
	# 		float(NumOrNot)
	# 		return True
	# 	except ValueError:  # ValueError为Python的一种标准异常，表示"传入无效的参数"
	# 		pass  # 如果引发了ValueError这种异常，不做任何事情（pass：不做任何事情，一般用做占位语句）
	# 	# try:
	# 	# 	import unicodedata  # 处理ASCii码的包
	# 	# 	unicodedata.numeric(s)  # 把一个表示数字的字符串转换为浮点数返回的函数
	# 	# 	return True
	# 	# except (TypeError, ValueError):
	# 	# 	pass
	# 	# return False
