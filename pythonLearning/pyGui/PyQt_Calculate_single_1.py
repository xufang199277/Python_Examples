# -*- coding: utf-8 -*-
"""
    【简介】
     单个程序实现科学计算器，按钮批量创建及调用函数
"""
from PyQt5.QtGui import QFont,QTextCursor
from PyQt5.QtWidgets import QPushButton , QWidget, QApplication, QTextEdit
import sys
from functools import partial
import math
class WinForm(QWidget):
	Calculate_Char_SHOW = ""
	Calculate_Char_SHOW_List = []
	Calculate_Char_Operation_List = []
	PI = math.pi
	E = math.e
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
		font.setWeight(75)
		self.pBtn_Dic = {}
		Geometry_X = -83
		Geometry_Y = 275
		pBtn_row = 1
		self.pBtn_i = 0
		self.TextEdit_SHOW_List = ["trig", "degree", "sin", "cos", "tan", "pow", "log", ",", "(", ")", "√", "C","del",
								   "%", "/", "X!", "7", "8", "9", "*", "1/", "4", "5", "6", "-", "pi","1", "2","3", "+",
								   "change", "e", "0", ".", "=","\n","INPUT ERROR", "rad","arcsin", "arccos", "arctan"]
		self.pBtn_SHOW_List = ["trig", "deg", "sin", "cos", "tan", "Xy", "log", ",", "(", ")", "√x", "C",
								"del", "%", "/", "X!", "7", "8", "9", "*", "1/X", "4", "5", "6", "-", "pi",
								"1", "2", "3", "+", "change", "e", "0", ".", "="]
		self.pBtn__Operation_TextEdit_Dict = {"degree":"math.degrees", "sin":"math.sin", "cos":"math.cos", "tan":"math.tan",
										"pow":"math.pow", "log":"math.log",",":",", "(":"(", ")":")", "√":"math.sqrt",
										"%":"%", "/":"/", "X!":"math.factorial", "7":"7", "8":"8", "9":"9", "*":"*", "1/":"1/",
										"4":"4","5":"5", "6":"6", "-":"-", "pi":"PI", "1":"1", "2":"2", "3":"3", "+":"+",
										"e":"E", "0":"0", ".":".", "\n":"\n","":"", "arcsin":"math.asin",
										"arccos":"math.acos", "arctan":"math.atan", "rad":"math.radians"}
		for self.pBtn_i in range(35):
			if self.pBtn_i - int(self.pBtn_i / 5) <= 4 * pBtn_row:
				Geometry_X = Geometry_X + 83
				if self.pBtn_i - 5 * int(self.pBtn_i / 5) == 0:
					Geometry_X = 0
					Geometry_Y = Geometry_Y + 46
					pBtn_row = pBtn_row + 1
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)] = QPushButton(self)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setGeometry(Geometry_X, Geometry_Y, 85, 48)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setText(self.pBtn_SHOW_List[self.pBtn_i])
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].setFont(font)
			self.pBtn_Dic['pBtn_' + str(self.pBtn_i)].clicked.connect(partial(self.pBtn_Click_Function ,self.pBtn_i))

	def pBtn_Click_Function(self,pBtn_Object_Num):
		self.Calculate_PARA_HandInput(pBtn_Object_Num)
		WinForm.Calculate_Char_SHOW = ''.join(WinForm.Calculate_Char_SHOW_List)
		cursor = self.Displaytext.textCursor()
		cursor.movePosition(QTextCursor.End)
		self.Displaytext.setPlainText(WinForm.Calculate_Char_SHOW)
		self.Displaytext.setTextCursor(cursor)
		self.Displaytext.ensureCursorVisible()
		WinForm.Calculate_Char_SHOW_List = []
		WinForm.Calculate_Char_Operation_List = []

	def Calculate_PARA_HandInput(self,pBtn_Object_Num):
		WinForm.Calculate_Char_SHOW = self.Displaytext.toPlainText()
		WinForm.Calculate_Char_SHOW_List = self.Cut_EditText_Part(WinForm.Calculate_Char_SHOW)
		WinForm.Calculate_Char_Operation_List = self.ShowToOperation(WinForm.Calculate_Char_SHOW_List)
		PARA_HAND_INPUT = self.TextEdit_SHOW_List[pBtn_Object_Num]
		if PARA_HAND_INPUT == "=":
			WinForm.Calculate_Char_SHOW_List.append("\n" + str(self.Calculate_Function(WinForm.Calculate_Char_Operation_List)))
		elif PARA_HAND_INPUT == "C":
			WinForm.Calculate_Char_SHOW_List = ["0"]
		elif PARA_HAND_INPUT == "change":
			pass
		elif PARA_HAND_INPUT == "degree":
			self.TextEdit_SHOW_List[1] = "rad"
			self.TextEdit_SHOW_List[-4] = "degree"
			self.pBtn_SHOW_List[1] = "rad"
			self.pBtn_Dic['pBtn_' + str(1)].setText(self.pBtn_SHOW_List[1])
			WinForm.Calculate_Char_SHOW_List.append(PARA_HAND_INPUT)
		elif PARA_HAND_INPUT == "rad":
			self.TextEdit_SHOW_List[1] = "degree"
			self.TextEdit_SHOW_List[-4] = "rad"
			self.pBtn_SHOW_List[1] = "deg"
			self.pBtn_Dic['pBtn_' + str(1)].setText(self.pBtn_SHOW_List[1])
			WinForm.Calculate_Char_SHOW_List.append(PARA_HAND_INPUT)
		elif PARA_HAND_INPUT == "trig":
			self.TextEdit_SHOW_List[0] = "atrig"
			self.TextEdit_SHOW_List[2] = "arcsin"
			self.TextEdit_SHOW_List[3] = "arccos"
			self.TextEdit_SHOW_List[4] = "arctan"
			self.TextEdit_SHOW_List[-1] = "sin"
			self.TextEdit_SHOW_List[-2] = "cos"
			self.TextEdit_SHOW_List[-3] = "tan"
			self.pBtn_SHOW_List[0] = "atrig"
			self.pBtn_SHOW_List[2] = "arcsin"
			self.pBtn_SHOW_List[3] = "arccos"
			self.pBtn_SHOW_List[4] = "arctan"
			self.pBtn_Dic['pBtn_' + str(0)].setText(self.pBtn_SHOW_List[0])
			self.pBtn_Dic['pBtn_' + str(2)].setText(self.pBtn_SHOW_List[2])
			self.pBtn_Dic['pBtn_' + str(3)].setText(self.pBtn_SHOW_List[3])
			self.pBtn_Dic['pBtn_' + str(4)].setText(self.pBtn_SHOW_List[4])
		elif PARA_HAND_INPUT == "atrig":
			self.TextEdit_SHOW_List[0] = "trig"
			self.TextEdit_SHOW_List[2] = "sin"
			self.TextEdit_SHOW_List[3] = "cos"
			self.TextEdit_SHOW_List[4] = "tan"
			self.TextEdit_SHOW_List[-1] = "arcsin"
			self.TextEdit_SHOW_List[-2] = "arccos"
			self.TextEdit_SHOW_List[-3] = "arctan"
			self.pBtn_SHOW_List[0] = "trig"
			self.pBtn_SHOW_List[2] = "sin"
			self.pBtn_SHOW_List[3] = "cos"
			self.pBtn_SHOW_List[4] = "tan"
			self.pBtn_Dic['pBtn_' + str(0)].setText(self.pBtn_SHOW_List[0])
			self.pBtn_Dic['pBtn_' + str(2)].setText(self.pBtn_SHOW_List[2])
			self.pBtn_Dic['pBtn_' + str(3)].setText(self.pBtn_SHOW_List[3])
			self.pBtn_Dic['pBtn_' + str(4)].setText(self.pBtn_SHOW_List[4])
		elif PARA_HAND_INPUT == "del":
			if WinForm.Calculate_Char_SHOW == "":
				pass
			else:
				WinForm.Calculate_Char_SHOW_List.pop()
		else:
			if WinForm.Calculate_Char_SHOW == "0":
				WinForm.Calculate_Char_SHOW_List[0] = PARA_HAND_INPUT
			else:
				WinForm.Calculate_Char_SHOW_List.append(PARA_HAND_INPUT)

	def Calculate_Function(self,Operation_Expression):
		WinForm.Calculate_Char_Expression = ''.join(Operation_Expression).strip().split("\n").pop()
		try:
			WinForm.Calculate_Char_Expression_Value = eval(WinForm.Calculate_Char_Expression)
		except Exception: WinForm.Calculate_Char_Expression_Value = "INPUT ERROR"
		return WinForm.Calculate_Char_Expression_Value

	def Cut_EditText_Part(self,str_EditText_show):
		n1 = len(str_EditText_show)
		i = 0
		Char_EditText = []
		while (i < n1):
			for Text_Part in self.TextEdit_SHOW_List:
				if str_EditText_show[i:i + len(Text_Part)] == Text_Part:
					if Text_Part == "INPUT ERROR":
						Char_EditText.append("")
					else: Char_EditText.append(Text_Part)
					i = i + len(Text_Part)
				else:
					pass
		return Char_EditText

	def ShowToOperation(self,show_key_list):
		ShowToOperation_List = []
		for key in show_key_list:
			ShowToOperation_List.append(self.pBtn__Operation_TextEdit_Dict[key])
		return ShowToOperation_List

if __name__ == "__main__":
	app = QApplication(sys.argv)
	form = WinForm()
	form.show()
	sys.exit(app.exec_())