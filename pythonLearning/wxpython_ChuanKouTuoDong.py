#- * - coding: gbk -*-
import wx
from PIL import Image

class ShapedFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"ShapedWindow",
        style=wx.FRAME_SHAPED|wx.SIMPLE_BORDER)
        self.hasShape=False
        self.delta=wx.Point(0,0)
        self.bmp=Image.getVippiBitmap()
        self.SetClientSize((self.bmp.GetWidth(),self.bmp.GetHeight()))
        dc=wx.ClientDC(self)
        dc.DrawBitmap(self.bmp,0,0,True)
        self.SetWindowShape()
        self.Bind(wx.EVT_LEFT_DCLICK,self.OnDoubleClick)

#1新事件
        self.Bind(wx.EVT_LEFT_DOWN,self.OnLeftDown)
        self.Bind(wx.EVT_LEFT_UP,self.OnLeftUp)
        self.Bind(wx.EVT_MOTION,self.OnMouseMove)

        self.Bind(wx.EVT_RIGHT_UP,self.OnExit)
        self.Bind(wx.EVT_PAINT,self.OnPaint)
        self.Bind(wx.EVT_WINDOW_Create,self.SetWindowShape)

    def SetWindowShape(self,evt=None):
        r=wx.RegionFromBitmap(self.bmp)
        self.hasShape=self.SetShape(r)

    def OnDoubleClick(self,evt):
        if self.hasShape:
            self.SetShape(wx.Region())
            self.hasShape=False
        else:
            self.SetWindowShape()

    def OnPaint(self,evt):
        dc=wx.PaintDC(self)
        dc.DrawBitmap(self.bmp,0,0,True)

    def OnExit(self,evt):
        self.Close()

    def OnLeftDown(self,evt):#2鼠标按下
        self.CaptureMouse()
        pos=self.ClientToScreen(evt.GetPosition())
        origin=self.Ge
        evt.GetPosition()
        self.delta=wx.Point(pos.x-origin.x,pos.y-origin.y)

    def OnMouseMove(self,evt):#3鼠标移动
        if  evt.Dragging()and   evt.LeftIsDown():
            pos=self.ClientToScreen(evt.GetPosition())
            newPos=(pos.x-self.delta.x,pos.y-self.delta.y)
            self.Move(newPos)

    def     OnLeftUp(self,evt):#4鼠标释放
        if  self.HasCapture():
            self.ReleaseMouse()



if  __name__=='__main__':
    app=wx.PySimpleApp()
    ShapedFrame().Show()
    app.MainLoop()

# #1我们为三个事件增加了相应的处理器http://www.shwlxx.com/sort/4，以作相应的工作。这三个事件是鼠标左键按下，鼠标左键释放和鼠标移动。
#
# #2拖动事件从鼠标左键按下开始。这个事件处理器做两件事。首先它捕获这个鼠标，直到鼠标被释放，以防止鼠标事件被改善到其它窗口部件。第二，它计算事件发生http://www.boomss.com的位置和窗口左上角之间的偏移量，这个偏移量将被用来计算窗口的新位置。
#
# #3这个处理器当鼠标移动时被调用，它首先检查看该事件是否是一个鼠标左键按下，如果是，它使用这个新的位置和前面计算的偏移量来确定窗口的新位置，并移动窗口。
#
# #4当鼠标左键被释放时，ReleaseMouse()被调用，这使得鼠标事件又可以被发送到其它的窗口部件。
#
# 这个拖动技术可以被完善以适合其它的需要。例如，仅在一个定义的区域内鼠标敲击才开始一个拖动，你可以对鼠标按下事件的位置做一个测试，使敲击发生在右边的位置时，才能拖动