# coding:utf8
import wx

app = wx.App()  # 创建对象
win = wx.Frame(None, title="ahuang1900", size=(410,340 ))  # 创建窗口对象

wx.Button(win, label="open", pos=(245, 5), size=(80, 25))  # 创建按钮1
wx.Button(win, label="save", pos=(325, 5), size=(80, 25))  # 创建按钮2
wx.TextCtrl(win, pos=(5, 5), size=(240, 25))  # 创建文本框1

# 创建文本框2
wx.TextCtrl(win, pos=(5, 35), size=(300, 300), style=wx.TE_MULTILINE | wx.HSCROLL)

win.Show()  # 显示
app.MainLoop()  # 主事件循环