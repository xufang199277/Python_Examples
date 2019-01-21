# -*- coding: utf-8 -*-
# '''
# wx.Window 是一个基类，许多构件从它继承。包括 wx.Frame 构件。技术上这意味着，我们可以在所有的
# 子类中使用 wx.Window 的方法。我们这里介绍它的几种方法：
#
# * SetTitle( string title ) —— 设置窗口标题。只可用于框架和对话框。
# * SetToolTip( wx.ToolTip tip ) —— 为窗口添加提示。
# * SetSize( wx.Size size ) —— 设置窗口的尺寸。
# * SetPosition( wx.Point pos ) —— 设置窗口出现的位置。
# * Show( show = True ) —— 显示或隐藏窗口。其中的参数可以为 True 或False。
# * Move( wx.Point pos ) —— 将窗口移动到指定位置。
# * SetCursor( wx.StockCursor id ) —— 设置窗口的鼠标指针样式。
#
#
# Python代码  收藏代码
# import wx
# app = wx.PySimpleApp()
# frame = wx.Frame( None, -1, '' )
# frame.SetToolTip( wx.ToolTip( 'This is a frame' ) )
# frame.SetCursor( wx.StockCursor( wx.CURSOR_MAGNIFIER ) )
# frame.SetPosition( wx.Point( 0, 0 ) )
# frame.SetSize( wx.Size( 300, 250 ) )
# frame.SetTitle( 'simple2.py' )
# frame.Show()
# app.MainLoop()
#
# 我们创建了一个"This is a frame"提示。鼠标指针被设置为放大镜样式。可用的鼠标指针样式有：
#
# wx.CURSOR_ARROW
# wx.CURSOR_RIGHT_ARROW
# wx.CURSOR_BLANK
# wx.CURSOR_BULLSEYE
# wx.CURSOR_CHAR
# wx.CURSOR_CROSS
# wx.CURSOR_HAND
# wx.CURSOR_IBEAM
# wx.CURSOR_LEFT_BUTTON
# wx.CURSOR_MAGNIFIER
# wx.CURSOR_MIDDLE_BUTTON
# wx.CURSOR_NO_ENTRY
# wx.CURSOR_PAINT_BRUSH
# wx.CURSOR_PENCIL
# wx.CURSOR_POINT_LEFT
# wx.CURSOR_POINT_RIGHT
# wx.CURSOR_QUESTION_ARROW
# wx.CURSOR_RIGHT_BUTTON
# wx.CURSOR_SIZENESW
# wx.CURSOR_SIZENS
# wx.CURSOR_SIZENWSE
# wx.CURSOR_SIZEWE
# wx.CURSOR_SIZING
# wx.CURSOR_SPRAYCAN
# wx.CURSOR_WAIT
# wx.CURSOR_WATCH
# wx.CURSOR_ARROWWAIT
#
#
# 我们把窗口放在了左上角，大小是 300x250 像素，标题被设置为"simple2.py"。
#
#
#
# ======================================================================
#
#
#
# wx.Frame 是一个容器构件。这意味着它可以容纳其它构件。它有如下的构造器：
#
# wx.Frame( wx.Window parent, id, string title, wx.Point pos=wx.DefaultPosition, wx.Size size=wx.DefaultSize, style = wx.DEFAULT_FRAME_STYEL, string name='frame' )
#
# 构造器是一种特殊的函数。它在对象创建时被调用。对于我们来说重要的是，我们打算创建一个新的构件时，只要简单的调用它的构造器就行了。Python允许 参数有默认值。所以在wx.Frame中必须的参数就只剩下了parent、id和title了。如果你按顺序指定参数的值，那么你可以不必带上参数的名 称。比如你想创建一个wx.Frame构件，它没有parent，标识符是100，标题是"Title"，位置在(100,50)大小是 (100,100)：
#
# frame=wx.Frame(None,100,'Title',wx.Point(100,50),wx.Size(100,100))
# 下面我们省略了 pos 参数。所以必须明确的提供 size 参数：
#
# frame=wx.Frame(None,100,'Title',size=wx.Size(100,100))
#
# 下面的例子，我们将使用其它有用的特性：
#
#
# Python代码  收藏代码
# import wx
# def main():
#     app=wx.PySimpleApp()
#     frame=wx.Frame(None,-1,'Icon',wx.DefaultPosition,wx.Size(350,300))
#     frame.SetIcon(wx.Icon('Tipi.ico',wx.BITMAP_TYPE_ICO))
#     frame.Center()
#     frame.Show()
#     app.MainLoop()
# if __name__ == '__main__':
#     main()
#
# Icon文件名为Iipi.ico。位于当前目录下。Icon构造器的第一个参数是Icon文件名，第二个参数是 Icon 文件类型。
# 就像你注意到的，程序的结构发生了改变。这样才符合Python编程的标准。
#
# 在Python中，__name__ 是一个特殊的变量。更复杂的程序通常由几个文件组成，但仅有一个文件用于开启程序。对于这个文件，当你直接执行它时，Python设置__name__变 量的值为'__main__'。所以，如果你双击icon.py或从命令行直接执行它，__name__ 变量的值就会等于__main__。main()函数也就会被调用。
#
#
#
# ======================================================================
#
#
# 创建一个菜单栏在wxPython中相当简单。我们将讨论给菜单栏添加菜单、为已经存在的菜单添加子菜单。所有菜单都有菜单项组成。菜单项可以是常规项、复选项以及单选项。
#
# 先来创建一个菜单栏：
# menubar = wx.MenuBar()
#
# 接着创建我们的菜单：
# file = wx.Menu()
# edit = wx.Menu()
# help = wx.Menu()
#
# 然后为菜单添加菜单项。做这件事有两种方式：
# file.Append( 101, '&Open', 'Open a new document' )
# file.Append( 102, '&Save', 'Save the document' )
#
# 我们可以使用横线来分隔逻辑区域：
# file.AppendSeparator()
#
# 如果你想在菜单中使用 Icon，你需要手工创建 MenuItem 对象：
# quit=wx.MenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application')
# quit.SetBitmap(wx.Image('stock_exit-16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
# file.AppendItem(quit)
#
# wxPython工具包只能把bitmap图片用于菜单，所以我们需要把我们的PNG图片转换为bitmap格式。
#
# 然后把菜单加入到菜单栏：
# menubar.Append( file, '&File' )
# menubar.Append( edit, '&Edit' )
# menubar.Append( help, '&Help' )
#
# 最后在我们的程序类中创建菜单栏：
# self.SetMenuBar( menubar )
#
# 我们把上述这些组成个小脚本：
#
# Python代码  收藏代码
# #!/usr/bin/env python
# # FileName: menu1.py
# import wx
# class MyMenu( wx.Frame ):
# def __init__(self,parent,ID,title):
# wx.Frame.__init__(self,parent,-1,title,wx.DefaultPosition,wx.Size(200, 150))
# menubar=wx.MenuBar()
# file=wx.Menu()
# edit=wx.Menu()
# help=wx.Menu()
# file.Append(101,'&Open','Open a new document')
# file.Append(102,'&Save','Save the document')
# file.AppendSeparator()
# quit=wx.MenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application')
# quit.SetBitmap(wx.Image('stock_exit-16.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
# file.AppendItem(quit)
# menubar.Append(file,'&File')
# menubar.Append(edit,'&Edit')
# menubar.Append(help,'&Help')
# self.SetMenuBar( menubar )
#
# class MyApp(wx.App):
# def OnInit(self):
# frame=MyMenu(None,-1,'menu1.py')
# frame.Show(True)
# return True
#
# app=MyApp(0)
# app.MainLoop()
#
# 到目前为止我们已经知道了如何定义默认的普通菜单项。接下来让我们看看如何明确的定义复选菜单项和单选菜单项：
# edit.Append( 201, 'check item1', '', wx.ITEM_CHECK )
# edit.Append( 202, 'check item2', '', kind=wx.ITEM_CHECK )
# 或者
# quit=wxMenuItem(file,105,'&Quit\tCtrl+Q','Quit the Application', wx.ITEM_NORMAL)
#
# 其中那个参数被称为种类。
# 可选的种类有：
# * wx.ITEM_NORMAL —— 默认
# * wx.ITEM_CHECK —— 复选
# * wx.ITEM_RADIO —— 单选
#
# 如果你想创建子菜单，要先创建一个菜单：
# submenu = wx.Menu()
#
# 然后为此子菜单添加一些菜单项：
# submenu.Append( 301, 'radio item1', kind= wx.ITEM_RADIO )
# submenu.Append( 302, 'radio item2', kind=wx.ITEM_RADIO )
# submenu.Append( 303, 'radio item3', kind=wx.ITEM_RADIO )
#
# 把子菜单添加到某个菜单对象就成了：
# edit.AppendMenu( 203, 'submenu', submenu )
#
# 最后，我们来看一下如何响应用户的动作。我们只是简单的感受一下。后面会有更详细的解释。
# 当用户选择了某个菜单项时，就产生了一个事件。我们必须提供一个事件处理器，用它反应相应的事件。在 wxPython 中处理事件是到目前为止我已知最优雅最简单的了。如果翻参考手册，你会发现 wx.EVT_MENU 处理在事件处理那章。
#
# 假如我们想为 quit 菜单项添加一个事件处理器：
# wx.EVT_MENU( self, 105, self.OnQuit )
#
# 我们需要提供三个信息。我们要把事件处理器绑定到的那个对象。这里是 self, 程序的主对象。与之相匹配的菜单项的 id。以及处理事件的方法的名称。
#
# 对用户的动作做出反应的方法需要两个参数。第一个是方法定义于其中的那个对象。第二个是产生的事件。本例中，我们什么也不做，只是简单的关闭我们的程序：
# def OnQuit( self, event ):
# self.Close()
#
#
# 下面的脚本会展示上面说的各种菜单项、子菜单以及一个简单的事件处理。我讨厌程序窗口出现在角落里，所以加上了：
# self.Centre()
#
# 这样窗口就会出现在屏幕的当中。
#
# Python代码  收藏代码
# #!/usr/bin/python
# # FileName: menu2.py
# import wx
#
# class MyMenu(wx.Frame):
# def __init__(self, parent, ID, title):
# wx.Frame.__init__(self, parent, -1, title,
# wx.DefaultPosition, wx.Size(380, 250))
# menubar = wx.MenuBar()
# file = wx.Menu()
# edit = wx.Menu()
# help = wx.Menu()
# file.Append(101, '&Open', 'Open a new document')
# file.Append(102, '&Save', 'Save the document')
# file.AppendSeparator()
# quit = wx.MenuItem(file, 105, '&Quit\tCtrl+Q', 'Quit the Application')
# quit.SetBitmap(wx.Image ('gtk-quit.png',
# wx.BITMAP_TYPE_PNG).ConvertToBitmap())
# file.AppendItem(quit)
# edit.Append(201, 'check item1', '', wx.ITEM_CHECK)
# edit.Append(202, 'check item2', kind= wx.ITEM_CHECK)
# submenu = wx.Menu()
# submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)
# submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)
# submenu.Append(303, 'radio item3', kind= wx.ITEM_RADIO)
# edit.AppendMenu(203, 'submenu', submenu)
# menubar.Append(file, '&File')
# menubar.Append(edit, '&Edit')
# menubar.Append(help, '&Help')
# self.SetMenuBar(menubar)
# self.Centre()
#
# wx.EVT_MENU(self, 105, self.OnQuit)
# def OnQuit(self, event):
# self.Close()
# class MyApp(wx.App):
# def OnInit(self):
# frame = MyMenu(None, -1, 'menu2.py')
# frame.Show(True)
# return True
# app = MyApp(0)
# app.MainLoop()
#
#
# ======================================================================
#
#
# 工具栏是一个集合了大多数常用命令和动作的构件。典型的象保存、打开、剪切、复制、粘贴、撤销、重复等。目的是为了节省时间。从工具栏执行动作只需点击一下，而从菜单需要点击两下。
#
# Python代码  收藏代码
# #!/usr/bin/env python
# # FileName: toolbar.py
# import wx
# class MyToolBar( wx.Frame ):
#
# def __init__( self, parent, ID, title ):
# wx.Frame.__init__( self, parent, ID, title, wx.DefaultPosition, wx.Size( 350, 250 ) )
#
# vbox = wx.BoxSizer( wx.VERTICAL )
# toolbar = wx.ToolBar( self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER )
# toolbar.AddSimpleTool( 1, wx.Image( 'stock_new.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'New', '' )
# toolbar.AddSimpleTool( 2, wx.Image( 'stock_open.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Opne', '' )
# toolbar.AddSimpleTool( 3, wx.Image( 'stock_save.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Save', '' )
# toolbar.AddSeparator()
# toolbar.AddSimpleTool( 4, wx.Image( 'stock_exit.png', wx.BITMAP_TYPE_PNG ).ConvertToBitmap(), 'Exit', '' )
# toolbar.Realize()
#
# vbox.Add( toolbar, 0, border=5 )
# self.SetSizer( vbox )
# self.statusbar = self.CreateStatusBar()
#
# self.Centre()
#
# wx.EVT_TOOL( self, 1, self.OnNew )
# wx.EVT_TOOL( self, 2, self.OnOpen )
# wx.EVT_TOOL( self, 3, self.OnSave )
# wx.EVT_TOOL( self, 4, self.OnExit )
#
# def OnNew( self, event ):
# self.statusbar.SetStatusText( 'New Command' )
#
# def OnOpen( self, event ):
# self.statusbar.SetStatusText( 'Open Command' )
#
# def OnSave( self, event ):
# self.statusbar.SetStatusText( 'Save Command' )
#
# def OnExit( self, event ):
# self.Close()
#
# class MyApp( wx.App ):
# def OnInit( self ):
# frame = MyToolBar( None, -1, ' toolbar.py' )
# frame.Show( True )
# return True
#
# app = MyApp( 0 )
# app.MainLoop()
#
# wx.BoxSizer 在后面的布局章节会解释到。工具栏构件通过三步创建。
#
# 首先，我们创建一个工具栏对象。
# tollbar = wx.ToolBar( self, -1, style= wx.TB_HORIZONTAL | wx.NO_BORDER )
#
# 然后我们使用 AddSimpleTool() 方法为工具栏添加了几个工具。你在参考手册中找不到这个方法。它是一个 wxPython 扩展。这既是个诅语也是个祝福。它合 Python 编程变得容易。但另一方面，这些扩展没有被写入文档。你不得不通过浏览源代码、demo 或者在邮件列表中提问来了解它们。
# toolbar.AddSimpleTool(1,wx.Image('stock_new.png',wx.BITMAP_TYPE_PNG).ConvertToBitmap(),'New','')
#
# 最后，我们调用 Realize() 方法。这个方法显示工具栏构件。
# toolbar.Realize()
#
# 工具栏有好几个事件处理顺。当你点击工具栏上的图标时，就会产生一个wx.EVT_COMMAND_TOOL_CLICKED事件。我们把此事件绑定的某个具体的wx.EVT_TOOL处理器方法上。
#
# 为了显示相关的输出，我们创建了一个状态栏。
# self.statusbar = self.CreateStatusBar()
#
# 这仍然是另外一个 wxPython 扩展。这样一旦我们点击工具栏按纽，状态栏就会显示相关信息。这是通过使用 SetStatusText() 方法达成的。
#
#
# ======================================================================
#
#
# 有两种基本的方法可以用来布置我们的构件。第一种是手工布置。我们通过在构造器中指定位置来摆放我们的构件。
#
# Python代码  收藏代码
# #!/usr/bin/evn python
# import wx
# class MyFrame(wx.Frame):
# def __init__(self,parent,ID,title):
# wx.Frame.__init__(self,parent,ID,title,wx.DefaultPosition,wx.Size(250,50))
# panel=wx.Panel(self,-1)
#
# wx.Button(panel,-1,'Button1',(0,0))
# wx.Button(panel,-1,'Button2',(80,0))
# wx.Button(panel,-1,'Button3',(160,0))
#
# class MyApp(wx.App):
# def OnInit(self):
# frame=MyFrame(None,-1,'layout.py')
# frame.Show(True)
# frame.Centre()
#
# app = MyApp(0)
# app.MainLoop()
#
# 当窗口大小改变时，按纽的大小和位置并不改变。这是手工设置构件位置的一个主要特征。第二种方法是使用布局管理器。这是现实程序中比较流行的方法。基本上你要使用 sizer。我们将讨论：
#
# * wx.BoxSizer
# * wx.StaticBoxSizer
# * wx.GridSizer
# * wx.GridBagSizer
#
#
# ======================================================================
#
#
# 我们来写一个程序，它的窗口顶部的一行被三个按纽占据。这些按纽会随窗口的改变而改变。
#
#
# Python代码  收藏代码
# #!/usr/bin/env python
# # FileName: wxboxsizer.py
# import wx
# class MyFrame(wx.Frame):
# def __init__(self,parent,ID,title):
# wx.Frame.__init__(self,parent,ID,title,(-1,-1),wx.Size(250,50))
# panel=wx.Panel(self,-1)
# box=wx.BoxSizer(wx.HORIZONTAL)
# box.Add( wx.Button( panel, -1, 'Button1' ), 1 )
# box.Add( wx.Button( panel, -1, 'Button2' ), 1 )
# box.Add( wx.Button( panel, -1, 'Button3' ), 1 )
#
# panel.SetSizer(box)
# self.Centre()
#
# class MyApp(wx.App):
# def OnInit(self):
# frame = MyFrame( None, -1, 'wxboxsizer.py' )
# frame.Show(True)
# return True
#
# app = MyApp(0)
# app.MainLoop()
#
#
# 我既可水平的摆放构件，也可竖直的摆放。
# box = wx.BoxSizer( integer orient )
#
# 其中的方向（orient）可以是 wx.VERTICAL 或 wx.HORIZONTAL。将构件加入 wx.BoxSizer 要使用 Add() 方法。为了理解，我们来看一下它的参数。
# Add(wx.Window window,integer proportion=0,integer flag=0,integer border=0)
#
# 其中的 proportion 参数定义了在定义的方向上构件改变的比例。假设我们有三个按纽，它们的 proportion 属性分别为0、1和2。它们被加入一个水平的 wx.BoxSizer。proportion 参数为 0 的按纽根本不发生变化。而这个参数值为 2 的按纽在水平方向改变的程序将是参数值为 1 的那个按纽的两倍。
#
# flag 参数可以更深入的设置构件的属性。我们可以控制构件之间的边框。我们可以在构件之间增加一些空白象素。在要使用边框的地方我们需要定义边界。我们可以使用 | 符号来连接它们。比如 wx.LEFT | wx.BOTTOM 。flag参数的值可以是：
# * wx.LEFT
# * wx.RIGHT
# * wx.BOTTOM
# * wx.TOP
# * wx.ALL
#
# 如果我们使用 wx.EXPAND 标识，我们的构件将占据所有分配给它的空间。最后，我们还可以定义构件的对齐方式。有以下几种：
# * wx.ALIGN_LEFT
# * wx.ALIGN_RIGHT
# * wx.ALIGN_TOP
# * wx.ALIGN_BOTTOM
# * wx.ALIGN_CENTER_VERTICAL
# * wx.ALIGN_CENTER_HORIZONTAL
# * wx.ALIGN_CENTER
#
# 看一个例子：
#
# Python代码  收藏代码
# #!/usr/bin/python
# # FileName: layout3.py
# import wx
# class MyFrame( wx.Frame ):
# def __init__( self, parent, ID, title ):
# wx.Frame.__init__(self,parent,ID,title,(-1,-1),wx.Size(450,300))
#
# panel = wx.Panel(self,-1)
# box = wx.BoxSizer( wx.HORIZONTAL )
#
# box.Add( wx.Button( panel, -1, 'Button1' ), 1, wx.ALL, 5 )
# box.Add( wx.Button( panel, -1, 'Button2' ), 0, wx.EXPAND )
# box.Add( wx.Button( panel, -1, 'Button3' ), 0, wx.ALIGN_CENTER )
#
# panel.SetSizer( box )
# self.Center()
#
# class MyApp( wx.App ):
# def OnInit( self ):
# frame = MyFrame( None, -1, 'layout3.py' )
# frame.Show( True )
# return True
#
# app = My App( 0 )
# app.MainLoop()
#
# 这个例子中，我们仍旧是创建了三个按纽。第一个的周围有一些边界。它是唯一一个可以在水平方向改变大小的，当主窗口的大小改变时。第二个按纽占据了分配给它的所有空间。第三个在竖起方向据中对齐。
# 我们可以任意组合 wx.BoxSizer 。例如，我们可以将几个水平的 wx.BoxSizer 放在一个竖起的 wx.BoxSizer 中或者相反。这样我们就能产生复杂的布局。
#
#
# Python代码  收藏代码
# #!/usr/bin/env python
# # FileName: borders.py
# import wx
# class MyFrame( wx.Frame ):
# def __init__( self, parent, id, title ):
# wx.Frame.__init__( self, parent, id, title )
#
# vbox = wx.BoxSizer( wx.VERTICAL )
# hbox1 = wx.BoxSizer( wx.HORIZONTAL )
# hbox2 = wx.BoxSizer( wx.HORIZONTAL )
#
# pnl1 = wx.Panel( self, -1, style=wx.SIMPLE_BORDER )
# pnl2 = wx.Panel( self, -1, style=wx.RAISED_BORDER )
# pnl3 = wx.Panel( self, -1, style=wx.SUNKEN_BORDER )
# pnl4 = wx.Panel( self, -1, style=wx.DOUBLE_BORDER )
# pnl5 = wx.Panel( self, -1, style=wx.STATIC_BORDER )
# pnl6 = wx.Panel( self, -1, style=wx.NO_BORDER )
#
# hbox1.Add( pnl1, 1, wx.EXPAND | wx.ALL, 3 )
# hbox1.Add( pnl2, 1, wx.EXPAND | wx.ALL, 3 )
# hbox1.Add( pnl3, 1, wx.EXPAND | wx.ALL, 3 )
#
# hbox2.Add( pnl4, 1, wx.EXPAND | wx.ALL, 3 )
# hbox2.Add( pnl5, 1, wx.EXPAND | wx.ALL, 3 )
# hbox2.Add( pnl6, 1, wx.EXPAND | wx.ALL, 3 )
#
# vbox.Add( hbox1, 1, wx.EXPAND )
# vbox.Add( hbox2, 1, wx.EXPAND )
#
# self.SetSizer( vbox )
# self.Centre()
#
# class MyApp( wx.App ):
# def OnInit( self ):
# frame = MyFrame( None, -1, 'borders.py' )
# frame.Show( True )
# return True
#
# app = MyApp( 0 )
# app.MainLoop()
#
'''
在这个例子中，我们创建了一个两行三列的表格。我们创建了一个竖直的 wx.BoxSizer 和两个水平的 wx.BoxSizer。我们只是简单的把两个水平的放进了那个竖直的中了。我们展示了六种可用的边框样式。边框是简单的窗口装饰品。注意其中两个边框样 式只能在 windows 上使用。
边框：
'''

#
# * wx.SIMPLE_BORDER
# * wx.RAISED_BORDER
# * wx.SUNKEN_BORDER
# * wx.DOUBLE_BORDER
# * wx.STATIC_BORDER
# * wx.NO_BORDER
#
#
# ======================================================================
#
# wx.GridSizer 使用两维的表格来布局它里面的东西。每个表格的宽度等于它里面最大那个构件的宽度，高度等于它里面高度最大的那个构件的高度。
# wx.GridSizer( integer rows, integer cols, integer vgap, integer hgap )
#
# 在构造器中，我们设定行和列的数目以及构件的水平和竖直间距。我们使用 AddMany() 方法将我们的构件插入到表中。按照从左到右、从上到下的顺序。
#
#
# Python代码  收藏代码
# #!/usr/bin/env python
# # FileName: calculator.py
# import wx
# class MyFrame( wx.Frame ):
# def __init__( self, parent, id, title ):
# wx.Frame.__init__(self,parent,id,title,wx.DefaultPosition,wx.Size(300, 250))
#
# self.formula = False
#
# menubar = wx.MenuBar()
# file = wx.Menu()
# file.Append( 22, '&Quit', 'Exit Calculator' )
# menubar.Append( file, '&File' )
# self.SetMenuBar( menubar )
#
# wx.EVT_MENU( self, 22, self.OnClose )
# sizer = wx.BoxSizer( wx.VERTICAL )
#
# self.display = wx.TextCtrl(self, -1, '', style=wx.TE_RIGHT)
# sizer.Add(self.display, 0, wx.EXPAND|wx.TOP|wx.BOTTOM, 4)
# gs = wx.GridSizer(4, 4, 3, 3)
# gs.AddMany([(wx.Button(self, 20, 'Cls'), 0, wx.EXPAND),
# (wx.Button(self, 21, 'Bck'), 0, wx.EXPAND),
# (wx.StaticText(self, -1, ''), 0, wx.EXPAND),
# (wx.Button(self, 22, 'Close'), 0, wx.EXPAND),
# (wx.Button(self, 1, '7'), 0, wx.EXPAND),
# (wx.Button(self, 2, '8'), 0, wx.EXPAND),
# (wx.Button(self, 3, '9'), 0, wx.EXPAND),
# (wx.Button(self, 4, '/'), 0, wx.EXPAND),
# (wx.Button(self, 5, '4'), 0, wx.EXPAND),
# (wx.Button(self, 6, '5'), 0, wx.EXPAND),
# (wx.Button(self, 7, '6'), 0, wx.EXPAND),
# (wx.Button(self, 8, '*'), 0, wx.EXPAND),
# (wx.Button(self, 9, '1'), 0, wx.EXPAND),
# (wx.Button(self, 10, '2'), 0, wx.EXPAND),
# (wx.Button(self, 11, '3'), 0, wx.EXPAND),
# (wx.Button(self, 12, '-'), 0, wx.EXPAND),
# (wx.Button(self, 13, '0'), 0, wx.EXPAND),
# (wx.Button(self, 14, '.'), 0, wx.EXPAND),
# (wx.Button(self, 15, '='), 0, wx.EXPAND),
# (wx.Button(self, 16, '+'), 0, wx.EXPAND)])
# sizer.Add(gs, 1, wx.EXPAND)
# self.SetSizer(sizer)
# self.Centre()
# wx.EVT_BUTTON(self, 20, self.OnClear)
# wx.EVT_BUTTON(self, 21, self.OnBackspace)
# wx.EVT_BUTTON(self, 22, self.OnClose)
# wx.EVT_BUTTON(self, 1, self.OnSeven)
# wx.EVT_BUTTON(self, 2, self.OnEight)
# wx.EVT_BUTTON(self, 3, self.OnNine)
# wx.EVT_BUTTON(self, 4, self.OnDivide)
# wx.EVT_BUTTON(self, 5, self.OnFour)
# wx.EVT_BUTTON(self, 6, self.OnFive)
# wx.EVT_BUTTON(self, 7, self.OnSix)
# wx.EVT_BUTTON(self, 8, self.OnMultiply)
# wx.EVT_BUTTON(self, 9, self.OnOne)
# wx.EVT_BUTTON(self, 10, self.OnTwo)
# wx.EVT_BUTTON(self, 11, self.OnThree)
# wx.EVT_BUTTON(self, 12, self.OnMinus)
# wx.EVT_BUTTON(self, 13, self.OnZero)
# wx.EVT_BUTTON(self, 14, self.OnDot)
# wx.EVT_BUTTON(self, 15, self.OnEqual)
# wx.EVT_BUTTON(self, 16, self.OnPlus)
#
# def OnClear(self, event):
# self.display.Clear()
# def OnBackspace(self, event):
# formula = self.display.GetValue()
# self.display.Clear()
# self.display.SetValue(formula[:-1])
# def OnClose(self, event):
# self.Close()
# def OnDivide(self, event):
# if self.formula:
# return
# self.display.AppendText('/')
# def OnMultiply(self, event):
# if self.formula:
# return
# self.display.AppendText('*')
# def OnMinus(self, event):
# if self.formula:
# return
# self.display.AppendText('-')
# def OnPlus(self, event):
# if self.formula:
# return
# self.display.AppendText('+')
# def OnDot(self, event):
# if self.formula:
# return
# self.display.AppendText('.')
# def OnEqual(self, event):
# if self.formula:
# return
# formula = self.display.GetValue()
# self.formula = True
# try:
# self.display.Clear()
# output = eval(formula)
# self.display.AppendText(str(output))
# except StandardError:
# self.display.AppendText("Error")
# def OnZero(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('0')
# def OnOne(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('1')
# def OnTwo(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('2')
# def OnThree(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('3')
# def OnFour(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('4')
# def OnFive(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('5')
# def OnSix(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('6')
# def OnSeven(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('7')
# def OnEight(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('8')
# def OnNine(self, event):
# if self.formula:
# self.display.Clear()
# self.formula = False
# self.display.AppendText('9')
#
# class MyApp(wx.App):
# def OnInit(self):
# frame = MyFrame(None, -1, "calculator.py")
# frame.Show(True)
# self.SetTopWindow(frame)
# return True
# app = MyApp(0)
# app.MainLoop()
#
# 我们输入的公式使用 python 的内置函数 eval 来处理。
# output = eval( formula )
#
# 如果公式有错，就会显示一条错误信息。请注意我们是如何在 Bck 和 Close 按纽之间插入空白的。我们只是简单的在那放了一个空的 wx.StaticText。这是一个很常用的技巧。
#
# '''


#实例程序
#!/usr/bin/env python2.4

# I like to put the python version on the #! line,
# so that I can have multiple versions installed.

"""

This is a small wxPython app developed to demonstrate how to write
Pythonic wxPython code.

"""

import wx

class DemoPanel(wx.Panel):
    """This Panel hold two simple buttons, but doesn't really do anything."""
    def __init__(self, parent, *args, **kwargs):
        """Create the DemoPanel."""
        wx.Panel.__init__(self, parent, *args, **kwargs)

        self.parent = parent  # Sometimes one can use inline Comments

        NothingBtn = wx.Button(self, label="Do Nothing with a long label")
        NothingBtn.Bind(wx.EVT_BUTTON, self.DoNothing )

        MsgBtn = wx.Button(self, label="Send Message")
        MsgBtn.Bind(wx.EVT_BUTTON, self.OnMsgBtn )

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(NothingBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5)
        Sizer.Add(MsgBtn, 0, wx.ALIGN_CENTER|wx.ALL, 5)

        self.SetSizerAndFit(Sizer)

    def DoNothing(self, event=None):
        """Do nothing."""
        pass

    def OnMsgBtn(self, event=None):
        """Bring up a wx.MessageDialog with a useless message."""
        dlg = wx.MessageDialog(self,
                               message='A completely useless message',
                               caption='A Message Box',
                               style=wx.OK|wx.ICON_INFORMATION
                               )
        dlg.ShowModal()
        dlg.Destroy()

class DemoFrame(wx.Frame):
    """Main Frame holding the Panel."""
    def __init__(self, *args, **kwargs):
        """Create the DemoFrame."""
        wx.Frame.__init__(self, *args, **kwargs)

        # Build the menu bar
        MenuBar = wx.MenuBar()

        FileMenu = wx.Menu()

        item = FileMenu.Append(wx.ID_EXIT, text="&Quit")
        self.Bind(wx.EVT_MENU, self.OnQuit, item)

        MenuBar.Append(FileMenu, "&File")
        self.SetMenuBar(MenuBar)

        # Add the Widget Panel
        self.Panel = DemoPanel(self)

        self.Fit()

    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()

if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Micro App")
    frame.Show()
    app.MainLoop()