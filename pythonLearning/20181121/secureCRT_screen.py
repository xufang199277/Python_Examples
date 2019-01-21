# $language = "Python"
# $interface = "1.0"
# 使用python语言实现SecureCRT中的Screen功能
# CurrentColumn返回当前光标的列坐标。
curCol = crt.Screen.CurrentColumn
crt.Dialog.MessageBox(str(curCol))

# CurrentRow返回当前光标的行坐标。
curRow = crt.Screen.CurrentRow
crt.Dialog.MessageBox(str(curRow))

# Columns 返回当前屏幕的最大列宽
cols = crt.Screen.Columns
crt.Dialog.MessageBox(str(cols))

# Rows 返回当前屏幕的最大行宽
rows = crt.Screen.Rows
crt.Dialog.MessageBox(str(rows))

# IgnoreEscape 定义当使用WaitForString、WaitForStrings和ReadString这三个方法时是否获取Escape字符（特殊字符如回车）默认是会获取的
crt.Screen.IgnoreEscape = False
crt.Dialog.MessageBox(crt.Screen.ReadString(["\03"], 5))  # 获取ctrl+c

crt.Screen.IgnoreEscape = True
crt.Dialog.MessageBox(crt.Screen.ReadString(["\03"], 2))  # 不获取ctrl+c

# MatchIndex 定义当使用WaitForStrings和ReadString这三个方法时会根据参数的位置 获取返回值，从1开始计算，如果没有一个匹配则返回0.
outPut = crt.Screen.ReadString(["error", "warning", "#"], 10)
index = crt.Screen.MatchIndex
if (index == 0):
    crt.Dialog.MessageBox("Timed out!")
elif (index == 1):
    crt.Dialog.MessageBox("Found 'error'")
elif (index == 2):
    crt.Dialog.MessageBox("Found 'warning'")
elif (index == 3):
    crt.Dialog.MessageBox("Found '#'")

# Synchronous 设置屏幕的同步属性。若设置为false，则在脚本中使用WaitForString、WaitForStrings、ReadString函数时可能存在丢失一部分数据的现象，设置为true后可能会存在屏幕卡顿的情况，默认为false
crt.Screen.Synchronous = True
crt.Screen.Send("\r\n")
crt.Screen.ReadString("#")
crt.Screen.Send("\r\n")
crt.Screen.WaitForString("#")
crt.Screen.Send("\r\n")
crt.Screen.WaitForStrings(["#", ">"])
crt.Screen.Send("conf t\r\n")

# 方法
# Clear()清屏功能
# crt.Screen.Clear()

# get()按照坐标取出一个矩形框内的屏幕上的字符(即从某行某列开始到其它行其它列)，不包含字符串中的回车换行符，所以这个多用于获取无格式的光标处字符串或某小段特定区域字符串。
out = crt.Screen.Get(row1, col1, row2, col2)
crt.Dialog.MessageBox(out)

# get2()解释按照坐标取出一个矩形框内的屏幕上的字符(即从某行某列开始到其它行其它列)，包含字符串中的回车换行符，所以这个多用于获取大段带格式的字符串。
crt.Screen.Get2(row1, col1, row2, col2)

# IgnoreCase 使用全局参数设置控制在使用WaitForString、WaitForStrings和ReadString这三个函数时是否对大小写敏感，默认为false大小写字符串都会检查，设置为true时则不会检测大小写。
crt.Screen.IgnoreCase = True
crt.Screen.Send("show memory\r\n")
crt.Screen.WaitForString("more")
crt.Screen.Send("\r\n")
crt.Screen.WaitForStrings("more", "#")
crt.Screen.Send("\r\n")
crt.Screen.ReadString("more", "#")

# Send() 向远端设备或者屏幕发送字符串，当向屏幕发送字符串时需要指定第二个参数为Ture
crt.Screen.Send("show version\r\n")
crt.Screen.Send("\r\nhello,world!\r\n", True)
crt.Screen.IgnoreCase = True
while (crt.Screen.WaitForString("more", 10)):
    crt.Screen.Send("\r\n")

# SendKeys()向当前窗口发送按键，包含组合按键，比如可以发送类似"CTRL+ALT+C"等这样的组合键，这样写即可：crt.screen.sendkeys("^%c");这个功能需要语言本身支持，目前只有VBS和JS脚本可以使用。

# SendSpecial()可以发送特殊控制码，这个控制码是Crt内置的功能，具体可以包含的有Menu、Telnet、VT functions功能列表中提供的所有功能，
crt.Screen.SendSpecial("vT_HOLD_SCREEN")

# WaitForCursor()等待光标移动，当移动时返回值为true，当有超时时间参数且超时时返回false，否则会一直等待光标移动。利用这个功能可以用来判断一个命令的输出是否结束，
crt.Screen.WaitForCursor(5)
crt.Screen.Send("\r\nhello,world!\r\n", True)
if (crt.Screen.WaitForCursor(5)):
    crt.Screen.Send("show version\r\n")

# WaitForKey()检测有键盘按键时返回true，当有超时时间参数且超时时返回false，否则会一直等待按键
if (crt.Screen.WaitForKey(5)):
    crt.Screen.Send("show version\r\n")

# WaitForString()一般用于发送命令后等待某字符串
# crt.Screen.WaitForString(string,[timeout],[bCaseInsensitive])
crt.Screen.WaitForString("#", 10)

# WaitForStrings()与WaitForString是同样的功能，可以等待多个字符串
outPut = crt.Screen.WaitForStrings(["error", "warning", "#"], 10)
index = crt.Screen.MatchIndex
if (index == 0):
    crt.Dialog.MessageBox("Timed out!")
elif (index == 1):
    crt.Dialog.MessageBox("Found 'error'")
elif (index == 2):
    crt.Dialog.MessageBox("Found 'warning'")
elif (index == 3):
    crt.Dialog.MessageBox("Found '#'")

# ReadString()与WaitForStrings功能类似，都是等待某几个字符出现，不同的是它还会读取字符串之前出现的所有字符。
crt.Screen.ReadString([string1, string2], [timeout], [bCaseInsensitive])
# 1、string，必选参数，等待的字符串，最少有一个，可以是特殊字符比如:\r\n；
# 2、timeout，可选参数，超时时间，当检测不到对应字符串时会返回false，没有此参数时会一直等待；
# 3、bCaseInsensitive，可选参数，大小写不敏感，默认值是false，表示将检测字符串的大小写，当为true时不检测大小写。