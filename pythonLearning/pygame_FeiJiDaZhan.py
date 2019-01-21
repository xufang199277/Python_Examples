#!/usr/bin/env python
# -*- coding:utf-8 -*-
import wx
import wx.lib.buttons
import cPickle
import os
class PaintWindow(wx.Window):
    def __init__(self, parent, id):
        wx.Window.__init__(self, parent, id)
        self.SetBackgroundColour("Green") #设置画板的背景色
        self.color = "Green"  #画笔的初始颜色
        self.thickness = 8 #设置画笔的初始粗细
class PaintFrame(wx.Frame):
    def __init__(self, parent):
        self.title = "Paint Frame"
        wx.Frame.__init__(self, parent, -1, self.title, size=(800, 600))
        self.paint = PaintWindow(self, -1)
        # self.paint = ControlPanel(self,None,-1,)
        self.CreatePanel()

    def CreatePanel(self):
        controlPanel = ControlPanel(self, -1, self.paint)
        box = wx.BoxSizer(wx.HORIZONTAL)  # 放置水平的box sizer
        box.Add(controlPanel, 0, wx.EXPAND)  # 水平方向伸展时不改变尺寸
        box.Add(self.paint, -1, wx.EXPAND)
        self.SetSizer(box)
class ControlPanel(wx.Panel):
    BMP_SIZE = 16
    BMP_BORDER = 3
    NUM_COLS = 4
    NUM_ROWS = 10
    SPACING = 4

    colorList = ('Black', 'Yellow', 'Red', 'Green', 'Blue', 'Purple',
                 'Brown', 'Aquamarine', 'Forest Green', 'Light Blue',
                 'Goldenrod', 'Cyan', 'Orange', 'Navy', 'Dark Grey',
                 'Light Grey')
    maxThickness = 20

    def __init__(self, parent, ID, paint):
        wx.Panel.__init__(self, parent, ID, style=wx.RAISED_BORDER)
        self.paint = paint
        buttonSize = (self.BMP_SIZE + 4 * self.BMP_BORDER,
                      self.BMP_SIZE + 4 * self.BMP_BORDER)
        colorGrid = self.createColorGrid(parent, buttonSize)  # 创建颜色grid sizer
        thicknessGrid = self.createThicknessGrid(parent,buttonSize)  # 创建线条grid sizer
        self.layout(colorGrid, thicknessGrid)

    def createColorGrid(self, parent, buttonSize):
        self.colorMap = {}
        self.colorButtons = {}
        colorGrid = wx.GridSizer(rows=self.NUM_ROWS,cols=self.NUM_COLS, hgap=2, vgap=2)
        for eachColor in self.colorList:
            bmp = self.MakeBitmap(eachColor)
            b = wx.lib.buttons.GenBitmapToggleButton(self, -1, bmp, size=buttonSize)
            b.SetBezelWidth(1000000)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetColour, b)
            colorGrid.Add(b, 0)
            self.colorMap[b.GetId()] = eachColor
            self.colorButtons[eachColor] = b
        self.colorButtons[self.colorList[0]].SetToggle(True)
        return colorGrid

    def createThicknessGrid(self, parent, buttonSize):
        self.thicknessIdMap = {}
        self.thicknessButtons = {}
        thicknessGrid = wx.GridSizer(cols=self.NUM_COLS, hgap=2, vgap=2)
        for x in range(1, self.maxThickness + 1):
            b = wx.lib.buttons.GenToggleButton(self, -1, str(x), size=buttonSize)
            b.SetBezelWidth(1)
            b.SetUseFocusIndicator(False)
            self.Bind(wx.EVT_BUTTON, self.OnSetThickness, b)
            thicknessGrid.Add(b, 0)
            self.thicknessIdMap[b.GetId()] = x
            self.thicknessButtons[x] = b
        self.thicknessButtons[1].SetToggle(True)
        return thicknessGrid

    def layout(self, colorGrid, thicknessGrid):
        box = wx.BoxSizer(wx.VERTICAL)  # 使用垂直的box szier放置grid sizer
        box.Add(colorGrid, 0, wx.ALL, self.SPACING)  # 参数0表示在垂直方向伸展时不改变尺寸
        box.Add(thicknessGrid, 0, wx.ALL, self.SPACING)
        self.SetSizer(box)
        box.Fit(self)

    def OnSetColour(self, event):
        color = self.colorMap[event.GetId()]
        if color != self.paint.color:
            self.colorButtons[self.paint.color].SetToggle(False)
        self.paint.SetColor(color)

    def OnSetThickness(self, event):
        thickness = self.thicknessIdMap[event.GetId()]
        if thickness != self.paint.thickness:
            self.thicknessButtons[self.paint.thickness].SetToggle(False)
        self.paint.SetThickness(thickness)

    def MakeBitmap(self, color):
        bmp = wx.EmptyBitmap(16, 15)
        dc = wx.MemoryDC(bmp)
        dc.SetBackground(wx.Brush(color))
        dc.Clear()
        dc.SelectObject(wx.NullBitmap)
        return bmp


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = PaintFrame(None)
    frame.Show(True)
    app.MainLoop()