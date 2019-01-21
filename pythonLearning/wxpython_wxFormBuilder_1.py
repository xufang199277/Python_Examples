# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Jun 17 2015)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import cPickle
import os


###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title='Paint By WuYan', pos=wx.DefaultPosition,
                          size=wx.Size(1200, 900), style=wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHintsSz(wx.DefaultSize, wx.DefaultSize)

        gbSizer1 = wx.GridBagSizer(0, 0)
        gbSizer1.SetFlexibleDirection(wx.BOTH)
        gbSizer1.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel1 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(410, 900), wx.TAB_TRAVERSAL)
        gbSizer2 = wx.GridBagSizer(0, 0)
        gbSizer2.SetFlexibleDirection(wx.BOTH)
        gbSizer2.SetNonFlexibleGrowMode(wx.FLEX_GROWMODE_SPECIFIED)

        self.m_panel3 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 400), wx.TAB_TRAVERSAL)
        gSizer1 = wx.GridSizer(4, 4, 0, 0)

        self.m_button6 = wx.Button(self.m_panel3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button6, 0, wx.ALL, 5)

        self.m_button7 = wx.Button(self.m_panel3, wx.ID_ANY, u"2", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button7, 0, wx.ALL, 5)

        self.m_button8 = wx.Button(self.m_panel3, wx.ID_ANY, u"3", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button8, 0, wx.ALL, 5)

        self.m_button9 = wx.Button(self.m_panel3, wx.ID_ANY, u"4", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button9, 0, wx.ALL, 5)

        self.m_button10 = wx.Button(self.m_panel3, wx.ID_ANY, u"5", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button10, 0, wx.ALL, 5)

        self.m_button11 = wx.Button(self.m_panel3, wx.ID_ANY, u"6", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button11, 0, wx.ALL, 5)

        self.m_button12 = wx.Button(self.m_panel3, wx.ID_ANY, u"7", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button12, 0, wx.ALL, 5)

        self.m_button13 = wx.Button(self.m_panel3, wx.ID_ANY, u"8", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button13, 0, wx.ALL, 5)

        self.m_button14 = wx.Button(self.m_panel3, wx.ID_ANY, u"9", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button14, 0, wx.ALL, 5)

        self.m_button15 = wx.Button(self.m_panel3, wx.ID_ANY, u"10", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button15, 0, wx.ALL, 5)

        self.m_button16 = wx.Button(self.m_panel3, wx.ID_ANY, u"11", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button16, 0, wx.ALL, 5)

        self.m_button17 = wx.Button(self.m_panel3, wx.ID_ANY, u"12", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button17, 0, wx.ALL, 5)

        self.m_button18 = wx.Button(self.m_panel3, wx.ID_ANY, u"13", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button18, 0, wx.ALL, 5)

        self.m_button19 = wx.Button(self.m_panel3, wx.ID_ANY, u"14", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button19, 0, wx.ALL, 5)

        self.m_button20 = wx.Button(self.m_panel3, wx.ID_ANY, u"15", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button20, 0, wx.ALL, 5)

        self.m_button21 = wx.Button(self.m_panel3, wx.ID_ANY, u"16", wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer1.Add(self.m_button21, 0, wx.ALL, 5)

        self.m_panel3.SetSizer(gSizer1)
        self.m_panel3.Layout()
        gbSizer2.Add(self.m_panel3, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        self.m_panel4 = wx.Panel(self.m_panel1, wx.ID_ANY, wx.DefaultPosition, wx.Size(400, 400), wx.TAB_TRAVERSAL)
        gSizer2 = wx.GridSizer(4, 4, 0, 0)

        self.m_button22 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button22, 0, wx.ALL, 5)

        self.m_button23 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button23, 0, wx.ALL, 5)

        self.m_button24 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button24, 0, wx.ALL, 5)

        self.m_button25 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button25, 0, wx.ALL, 5)

        self.m_button26 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button26, 0, wx.ALL, 5)

        self.m_button27 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button27, 0, wx.ALL, 5)

        self.m_button28 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button28, 0, wx.ALL, 5)

        self.m_button29 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button29, 0, wx.ALL, 5)

        self.m_button30 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button30, 0, wx.ALL, 5)

        self.m_button31 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button31, 0, wx.ALL, 5)

        self.m_button32 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button32, 0, wx.ALL, 5)

        self.m_button33 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button33, 0, wx.ALL, 5)

        self.m_button34 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button34, 0, wx.ALL, 5)

        self.m_button35 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button35, 0, wx.ALL, 5)

        self.m_button36 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button36, 0, wx.ALL, 5)

        self.m_button37 = wx.Button(self.m_panel4, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size(100, 100), 0)
        gSizer2.Add(self.m_button37, 0, wx.ALL, 5)

        self.m_panel4.SetSizer(gSizer2)
        self.m_panel4.Layout()
        gbSizer2.Add(self.m_panel4, wx.GBPosition(1, 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        self.m_panel1.SetSizer(gbSizer2)
        self.m_panel1.Layout()
        gbSizer1.Add(self.m_panel1, wx.GBPosition(0, 0), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        self.m_panel2 = wx.Panel(self, wx.ID_ANY, wx.DefaultPosition, wx.Size(800, 800), wx.TAB_TRAVERSAL)
        gbSizer1.Add(self.m_panel2, wx.GBPosition(0, 1), wx.GBSpan(1, 1), wx.EXPAND | wx.ALL, 5)

        self.SetSizer(gbSizer1)
        self.Layout()
        self.m_menubar2 = wx.MenuBar(0)
        self.m_menu2 = wx.Menu()
        self.m_menubar2.Append(self.m_menu2, u"菜单")

        self.SetMenuBar(self.m_menubar2)

        self.Centre(wx.BOTH)


        # Connect Events
        self.m_button6.Bind(wx.EVT_LEFT_DCLICK, self.m_button6OnLeftDClick)
        self.m_button7.Bind(wx.EVT_LEFT_DCLICK, self.m_button7OnLeftDClick)
        self.m_button8.Bind(wx.EVT_LEFT_DCLICK, self.m_button8OnLeftDClick)
        self.m_button9.Bind(wx.EVT_LEFT_DCLICK, self.m_button9OnLeftDClick)
        self.m_button10.Bind(wx.EVT_LEFT_DCLICK, self.m_button10OnLeftDClick)
        self.m_button11.Bind(wx.EVT_LEFT_DCLICK, self.m_button11OnLeftDClick)
        self.m_button12.Bind(wx.EVT_LEFT_DCLICK, self.m_button12OnLeftDClick)
        self.m_button13.Bind(wx.EVT_LEFT_DCLICK, self.m_button13OnLeftDClick)
        self.m_button14.Bind(wx.EVT_LEFT_DCLICK, self.m_button14OnLeftDClick)
        self.m_button15.Bind(wx.EVT_LEFT_DCLICK, self.m_button15OnLeftDClick)
        self.m_button16.Bind(wx.EVT_LEFT_DCLICK, self.m_button16OnLeftDClick)
        self.m_button17.Bind(wx.EVT_LEFT_DCLICK, self.m_button17OnLeftDClick)
        self.m_button18.Bind(wx.EVT_LEFT_DCLICK, self.m_button18OnLeftDClick)
        self.m_button19.Bind(wx.EVT_LEFT_DCLICK, self.m_button19OnLeftDClick)
        self.m_button20.Bind(wx.EVT_LEFT_DCLICK, self.m_button20OnLeftDClick)
        self.m_button21.Bind(wx.EVT_LEFT_DCLICK, self.m_button21OnLeftDClick)
        self.colorButtonMap()
        self.colorPanelMap()
        self.PenColor = "Green"  # 画笔的初始颜色
        self.PenThickness = 10  # 设置画笔的初始粗细

        # 创建一个画笔
        self.pen = wx.Pen(self.PenColor, self.PenThickness, wx.SOLID)  # wx.Pen方法用于创建画笔
        # self.lines = []
        # self.curLine = []
        # self.pos = (0, 0)
        self.InitBuffer()

    def __del__(self):
        pass
    def InitBuffer(self):
        # 创建缓存的设备上下文
        self.buffer = wx.EmptyBitmap(800, 800)  # 创建一个与客户区域大小相同的空位图
        dc = wx.BufferedDC(None, self.buffer)  # 在位图上使用缓存的设备上下文

        # 使用设备上下文
        # dc.SetBackground(wx.Brush(self.GetBackgroundColour(self.m_panel2 )))  # 设置设备上下文（即客户区域）的背景色
        dc.Clear()
        self.DrawLines(dc)
        self.reInitBuffer = False
    def DrawLines(self, dc):
        # for colour, thickness, curLine in self.lines:
            pen = wx.Pen(self.PenColor, self.PenThickness, wx.SOLID)
            dc.SetPen(pen)
            # for coords in curLine:
            #     dc.DrawLine(*coords)
    def SetThickness(self,PenThickness):
        self.pen = wx.Pen(PenThickness, wx.SOLID)

    # Virtual event handlers, overide them in your derived class
    def m_button6OnLeftDClick(self, event):
        self.PenThickness = 1
        # self.SetThickness(1)
        event.Skip()

    def m_button7OnLeftDClick(self, event):
        PenThickness = 2
        event.Skip()

    def m_button8OnLeftDClick(self, event):
        PenThickness = 3
        event.Skip()

    def m_button9OnLeftDClick(self, event):
        PenThickness = 4
        event.Skip()

    def m_button10OnLeftDClick(self, event):
        PenThickness = 5
        event.Skip()

    def m_button11OnLeftDClick(self, event):
        PenThickness = 6
        event.Skip()

    def m_button12OnLeftDClick(self, event):
        PenThickness = 7
        event.Skip()

    def m_button13OnLeftDClick(self, event):
        PenThickness = 8
        event.Skip()

    def m_button14OnLeftDClick(self, event):
        PenThickness = 9
        event.Skip()

    def m_button15OnLeftDClick(self, event):
        PenThickness = 10
        event.Skip()

    def m_button16OnLeftDClick(self, event):
        PenThickness = 11
        event.Skip()

    def m_button17OnLeftDClick(self, event):
        PenThickness = 12
        event.Skip()

    def m_button18OnLeftDClick(self, event):
        PenThickness = 13
        event.Skip()

    def m_button19OnLeftDClick(self, event):
        PenThickness = 14
        event.Skip()

    def m_button20OnLeftDClick(self, event):
        PenThickness = 15
        event.Skip()

    def m_button21OnLeftDClick(self, event):
        PenThickness = 16
        event.Skip()

    # self.colorMap()
    def colorPanelMap(self):
        # self.m_panel1.SetBackgroundColour("Black")
        self.m_panel2.SetBackgroundColour("Black")
        # self.m_panel3.SetBackgroundColour("Black")
        # self.m_panel4.SetBackgroundColour("Black")


    def colorButtonMap(self):
        colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
                     'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',
                     'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',
                     'Light Grey')
        self.m_button22.SetBackgroundColour("Black")
        self.m_button23.SetBackgroundColour("Yellow")
        self.m_button24.SetBackgroundColour("Green")
        self.m_button25.SetBackgroundColour("Blue")
        self.m_button26.SetBackgroundColour("Blue")
        self.m_button27.SetBackgroundColour("Purple")
        self.m_button28.SetBackgroundColour("Brown")
        self.m_button29.SetBackgroundColour("Aquamarine")
        self.m_button30.SetBackgroundColour("Forest Green")
        self.m_button31.SetBackgroundColour("Light Blue")
        self.m_button32.SetBackgroundColour("Goldenrod")
        self.m_button33.SetBackgroundColour("Cyan")
        self.m_button34.SetBackgroundColour("Orange")
        self.m_button35.SetBackgroundColour("Navy")
        self.m_button36.SetBackgroundColour("Dark Grey")
        self.m_button37.SetBackgroundColour("Light Grey")


    # 定义MakeBitmap函数，功能是使用一种颜色来创造一个位图
    # def MakeBitmap(self, color):
    #     bmp = wx.EmptyBitmap(50, 50)
    #     dc = wx.MemoryDC(bmp)
    #     dc.SetBackground(wx.Brush(color))
    #     dc.Clear()
    #     dc.SelectObject(wx.NullBitmap)
    #     return bmp

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()
