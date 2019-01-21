import random
import win32api,win32gui
import sys
import time
import win32con
from PIL import ImageGrab
import numpy as np
import time
#扫雷游戏窗口
class_name = "TMain"
title_name = "Minesweeper Arbiter "
hwnd = win32gui.FindWindow(class_name, title_name)

#窗口坐标
left = 0
top = 0
right = 0
bottom = 0

if hwnd:
    print("找到窗口")
    left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    #win32gui.SetForegroundWindow(hwnd)
    print("窗口坐标：")
    print(str(left)+' '+str(top)+' '+str(right)+' '+str(bottom))
else:
    print("未找到窗口")
#锁定雷区坐标
#去除周围功能按钮以及多余的界面
#具体的像素值是通过QQ的截图来判断的
left += 15
top += 112
right -= 27
bottom = top + 128
#抓取雷区图像
#526542652 281409
rect = (left, top, right, bottom)
img = ImageGrab.grab().crop(rect)
block_width, block_height = 16, 16
print(rect)
#横向有blocks_x个方块
blocks_x = round((right - left) / block_width)
print(blocks_x)
#纵向有blocks_y个方块
blocks_y = round((bottom - top) / block_height)
print(blocks_y)
# imgd = img.crop((7*block_width, 5*block_height, 8*block_width, 6*block_height))
# imgd.show()
# print(imgd.getcolors())
# imgd.show()
#数字1-8 周围雷数
#0 未被打开
#ed 被打开 空白
#hongqi 红旗
#boom 普通雷
#boom_red 踩中的雷
rgba_ed = [(225, (192, 192, 192)), (31, (128, 128, 128))]
rgba_hongqi = [(54, (255, 255, 255)), (17, (255, 0, 0)), (109, (192, 192, 192)), (54, (128, 128, 128)), (22, (0, 0, 0))]
rgba_0 = [(54, (255, 255, 255)), (148, (192, 192, 192)), (54, (128, 128, 128))]
rgba_1 = [(185, (192, 192, 192)), (31, (128, 128, 128)), (40, (0, 0, 255))]
rgba_2 = [(160, (192, 192, 192)), (31, (128, 128, 128)), (65, (0, 128, 0))]
rgba_3 = [(62, (255, 0, 0)), (163, (192, 192, 192)), (31, (128, 128, 128))]
rgba_4 = [(169, (192, 192, 192)), (31, (128, 128, 128)), (56, (0, 0, 128))]
rgba_5 = [(70, (128, 0, 0)), (155, (192, 192, 192)), (31, (128, 128, 128))]
rgba_6 = [(153, (192, 192, 192)), (31, (128, 128, 128)), (72, (0, 128, 128))]
rgba_8 = [(149, (192, 192, 192)), (107, (128, 128, 128))]
rgba_boom = [(4, (255, 255, 255)), (144, (192, 192, 192)), (31, (128, 128, 128)), (77, (0, 0, 0))]
rgba_boom_red = [(4, (255, 255, 255)), (144, (255, 0, 0)), (31, (128, 128, 128)), (77, (0, 0, 0))]
map = np.zeros(shape=(blocks_x,blocks_y))

#扫描雷区图像
def showmap():
    # img = ImageGrab.grab().crop(rect)
    # print(rect)
    gameover = 1
    for y in range(blocks_x):
        for x in range(blocks_y):
            this_image = img.crop((x * block_width, y * block_height, (x + 1) * block_width, (y + 1) * block_height))
            # this_image.show()
            print((x,y))
            print(this_image.getcolors())
            if this_image.getcolors() == rgba_0:
                # this_image.show()
                map[y][x] = 0
                # this_image.show()
            elif this_image.getcolors() == rgba_1:
                map[y][x] = 1
                # print(map[2][2])
            elif this_image.getcolors() == rgba_2:
                # this_image.show()
                map[y][x] = 2
            elif this_image.getcolors() == rgba_3:
                map[y][x] = 3
            elif this_image.getcolors() == rgba_4:
                map[y][x] = 4
            elif this_image.getcolors() == rgba_5:
                map[y][x] = 5
            elif this_image.getcolors() == rgba_6:
                map[y][x] = 6
            elif this_image.getcolors() == rgba_8:
                map[y][x] = 8
            elif this_image.getcolors() == rgba_ed:
                map[y][x] = -1
            elif this_image.getcolors() == rgba_hongqi:
                map[y][x] = -4
            elif this_image.getcolors() == rgba_boom or this_image.getcolors() == rgba_boom_red:
                gameover = 1
                print(gameover)
                # break
                # sys.exit(0)
            else:
                # pass
                print("无法识别图像")
                # gameover = 0
                # print("坐标")
                # print((y,x))
                # print("颜色")
                # print(this_image.getcolors())
                # print(map)
                sys.exit(0)
    print(gameover)
    return gameover


showmap()

# #插旗
# def banner():
#     # showmap()
#     for y in range(blocks_y):
#         for x in range(blocks_x):
#             if 1 <= map[y][x] and map[y][x] <= 5:
#                 print((x,y))
#                 boom_number = map[y][x]
#                 print(boom_number)
#                 block_white = 0
#                 block_qi = 0
#                 for yy in range(y-1,y+2):
#                     for xx in range(x-1,x+2):
#                         if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
#                             if not (yy == y and xx == x):
#                                 if map[yy][xx] == 0:
#                                     block_white += 1
#                                 elif map[yy][xx] == -4:
#                                     block_qi += 1
#                 print(block_white)
#                 print(block_qi)
#                 if boom_number == block_white + block_qi:
#                     for yy in range(y - 1, y + 2):
#                         for xx in range(x - 1, x + 2):
#                             if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
#                                 if not (yy == y and xx == x):
#                                     if map[yy][xx] == 0:
#                                         win32api.SetCursorPos([left+xx*block_width, top+yy*block_height])
#                                         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
#                                         win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
#                                         # showmap()
#
# # banner()
#
# # 点击白块
# def dig():
#     # showmap()
#     iscluck = 0
#     for y in range(blocks_y):
#         for x in range(blocks_x):
#             if 1 <= map[y][x] and map[y][x] <= 5:
#                 boom_number = map[y][x]
#                 block_white = 0
#                 block_qi = 0
#                 for yy in range(y - 1, y + 2):
#                     for xx in range(x - 1, x + 2):
#                         if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
#                             if not (yy == y and xx == x):
#                                 if map[yy][xx] == 0:
#                                     block_white += 1
#                                 elif map[yy][xx] == -4:
#                                     block_qi += 1
#                 if boom_number == block_qi and block_white > 0:
#                     for yy in range(y - 1, y + 2):
#                         for xx in range(x - 1, x + 2):
#                             if 0 <= yy and 0 <= xx and yy < blocks_y and xx < blocks_x:
#                                 if not(yy == y and xx == x):
#                                     if map[yy][xx] == 0:
#                                         win32api.SetCursorPos([left + xx * block_width, top + yy * block_height])
#                                         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#                                         win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#                                         iscluck = 1
#     if iscluck == 0:
#         luck()
# #
# #随机点击
# def luck():
#     fl = 1
#     while(fl):
#         random_x = random.randint(0, blocks_x - 1)
#         random_y = random.randint(0, blocks_y - 1)
#         if(map[random_y][random_x] == 0):
#             win32api.SetCursorPos([left + random_x * block_width, top + random_y * block_height])
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#             win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#             fl = 0
#
# #
# def gogo():
#     win32api.SetCursorPos([left, top])
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#     win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#     i = 1
#     while(i):
#         time.sleep(5)
#         gameover = showmap()
#         print(gameover)
#         if(gameover == 0):
#             banner()
#             # banner()
#             dig()
#         else:
#             i = 0
#             # pass
#             # gameover = 0
#             # win32api.keybd_event(113, 0, 0, 0)
#             # win32api.SetCursorPos([left, top])
#             # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
#             # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
#             # showmap()
# if __name__ == '__main__':
#     gogo()
#
#
