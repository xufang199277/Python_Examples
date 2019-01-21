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

#1���¼�
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

    def OnLeftDown(self,evt):#2��갴��
        self.CaptureMouse()
        pos=self.ClientToScreen(evt.GetPosition())
        origin=self.Ge
        evt.GetPosition()
        self.delta=wx.Point(pos.x-origin.x,pos.y-origin.y)

    def OnMouseMove(self,evt):#3����ƶ�
        if  evt.Dragging()and   evt.LeftIsDown():
            pos=self.ClientToScreen(evt.GetPosition())
            newPos=(pos.x-self.delta.x,pos.y-self.delta.y)
            self.Move(newPos)

    def     OnLeftUp(self,evt):#4����ͷ�
        if  self.HasCapture():
            self.ReleaseMouse()



if  __name__=='__main__':
    app=wx.PySimpleApp()
    ShapedFrame().Show()
    app.MainLoop()

# #1����Ϊ�����¼���������Ӧ�Ĵ�����http://www.shwlxx.com/sort/4��������Ӧ�Ĺ������������¼������������£��������ͷź�����ƶ���
#
# #2�϶��¼������������¿�ʼ������¼��������������¡����������������ֱ꣬����걻�ͷţ��Է�ֹ����¼������Ƶ��������ڲ������ڶ����������¼�����http://www.boomss.com��λ�úʹ������Ͻ�֮���ƫ���������ƫ���������������㴰�ڵ���λ�á�
#
# #3���������������ƶ�ʱ�����ã������ȼ�鿴���¼��Ƿ���һ�����������£�����ǣ���ʹ������µ�λ�ú�ǰ������ƫ������ȷ�����ڵ���λ�ã����ƶ����ڡ�
#
# #4�����������ͷ�ʱ��ReleaseMouse()�����ã���ʹ������¼��ֿ��Ա����͵������Ĵ��ڲ�����
#
# ����϶��������Ա��������ʺ���������Ҫ�����磬����һ�����������������û��ſ�ʼһ���϶�������Զ���갴���¼���λ����һ�����ԣ�ʹ�û��������ұߵ�λ��ʱ�������϶�