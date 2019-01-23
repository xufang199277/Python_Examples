# !/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import win32api,win32gui
import sys
import time
import win32con
from PIL import ImageGrab
import numpy as np
from scipy.special import comb
import random
class SaoLei():
    #扫雷游戏窗口
    class_name = "TMain"
    title_name = "Minesweeper Arbiter "
    #窗口坐标
    left, top, right, bottom = 0, 0, 0, 0
    #每个小格子的尺寸
    block_width, block_height = 16, 16
    blocks_x,blocks_y = 0, 0
    #程序结束标志
    gameover = 0
    # 数字1-3： 周围雷数；0： 未被打开；ed： 被打开空白；hongqi： 红旗；boom 普通雷；boom_red： 踩中的雷
    rgba_ed = [(225, (192, 192, 192)), (31, (128, 128, 128))]
    rgba_hongqi = [(54, (255, 255, 255)), (17, (255, 0, 0)), (109, (192, 192, 192)), (54, (128, 128, 128)),
                   (22, (0, 0, 0))]
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
    img = []
    position_skip = []
    def __init__(self):
        self.hwnd = win32gui.FindWindow(SaoLei.class_name, SaoLei.title_name)
        if self.hwnd:
            print("找到窗口")
            SaoLei.left, SaoLei.top, SaoLei.right, SaoLei.bottom = win32gui.GetWindowRect(self.hwnd)
            #win32gui.SetForegroundWindow(hwnd)
            print("窗口坐标：")
            print(str(SaoLei.left)+' '+str(SaoLei.top)+' '+str(SaoLei.right)+' '+str(SaoLei.bottom))
        else:
            print("未找到窗口")
        #锁定雷区坐标
        #去除周围功能按钮以及多余的界面
        #具体的像素值是通过QQ的截图来判断的
        SaoLei.left += 15
        SaoLei.top += 112
        SaoLei.right -= 27
        SaoLei.bottom = SaoLei.top + 128
        #抓取雷区图像
        self.rect = (SaoLei.left, SaoLei.top, SaoLei.right, SaoLei.bottom)
        #横向有blocks_x个方块
        SaoLei.blocks_x = round((SaoLei.right - SaoLei.left) / SaoLei.block_width)
        print(SaoLei.blocks_x)
        #纵向有blocks_y个方块
        SaoLei.blocks_y = round((SaoLei.bottom - SaoLei.top) / SaoLei.block_height)
        print(SaoLei.blocks_y)
        self.map = np.zeros(shape=(SaoLei.blocks_x,SaoLei.blocks_y))
        self.rgba_0_Statedict = {}
        self.hongqi_Statedict = {}
        self.problist = np.zeros(shape=(SaoLei.blocks_x * SaoLei.blocks_y))
        self.StartGame(self.problist)

    def StartGame(self,prob_list):
        self.Sure_Boom(prob_list)


    def Sure_Boom(self,prob_para):
        self.round_detect1 = 1
        mark1 = 0
        mark2 = 0
        mark3 = 0
        self.showmap()
        while(self.round_detect1):
            self.round_detect1_Num = 0
            self.round_detect_Boom = 0
            self.hongqi_Statedict_save = {}
            self.rgba_0_Statedict_save = {}
            self.round_detect2 = 1
            self.probstate = []
            self.all_position_probmax = []
            self.position_probmax = 0
            mark1 = mark1 +1
            print("mark1")
            while(self.round_detect2):
                self.Not_Click_list = []
                print("mark4")
                self.round_detect2 = 0
                self.NotBoomNum = 0
                self.hongqiNum = 0
                self.sure_boom_position = []
                self.mark = 0
                self.rgba_0_Statedict = {}
                self.hongqi_Statedict = {}
                print("eight")
                # SaoLei.img.show()
                for x_position in range(SaoLei.blocks_x):
                    for y_position in range(SaoLei.blocks_y):
                        # print("mark5")
                        if [x_position,y_position] not in SaoLei.position_skip:
                            if self.map[x_position][y_position] == 1 or self.map[x_position][y_position] == 2 or self.map[x_position][y_position] == 3 \
                                    or self.map[x_position][y_position] == 4 or self.map[x_position][y_position] == 5 or self.map[x_position][y_position] == 6 \
                                    or self.map[x_position][y_position] == 8:
                                for i in range(x_position-1,x_position+2):
                                    for j in range(y_position-1,y_position+2):

                                        if i >= 0 and j >= 0 and (i,j) != (x_position, y_position) and i < 8 and j < 8:
                                            print("five")
                                            print([i,j,x_position,y_position])
                                            if self.map[i][j] == 0:
                                                self.NotBoomNum = self.NotBoomNum + 1
                                                self.rgba_0_Statedict.setdefault(y_position+8*x_position, {})[j+8*i] = 0
                                                self.sure_boom_position.append([i,j])
                                                print("self.sure_boom_position1")
                                                print(self.sure_boom_position)
                                            elif self.map[i][j] == -5:
                                                self.NotBoomNum = self.NotBoomNum + 1
                                                self.hongqiNum = self.hongqiNum + 1
                                            else: pass
                                        else: pass
                            else:
                                self.NotBoomNum = 50
                                self.hongqiNum = 50
                        else:
                            self.NotBoomNum = 50 #任意选一个数，保证下面的if在self.map[x_position][y_position]=0时不执行
                            self.hongqiNum = 50
                        if self.map[x_position][y_position] == self.NotBoomNum:
                            # 标记为雷
                            SaoLei.position_skip.append([x_position,y_position])
                            print("map")
                            print(self.map)
                            print("x_position")
                            print(x_position)
                            print("y_position")
                            print(y_position)
                            print("self.NotBoomNum")
                            print(self.NotBoomNum)
                            print("self.sure_boom_position")
                            print(self.sure_boom_position)
                            for i in range(len(self.sure_boom_position)):
                                if self.map[self.sure_boom_position[i][0]][self.sure_boom_position[i][1]] != -5:
                                    win32api.SetCursorPos([SaoLei.left+self.sure_boom_position[i][1]*SaoLei.block_width,
                                                   SaoLei.top+self.sure_boom_position[i][0]*SaoLei.block_height])
                                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)
                                    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0, 0, 0)
                                    self.hongqiNum = self.hongqiNum + 1
                                    # self.map[self.sure_boom_position[i][0],self.sure_boom_position[i][1]] = -5
                                # time.sleep(0.1)
                            self.round_detect2 = 1
                            mark2 = mark2 + 1
                            print('mark2')
                        else: pass
                        if self.map[x_position][y_position] == self.hongqiNum:
                            SaoLei.position_skip.append([x_position, y_position])
                            for i in range(len(self.sure_boom_position)):
                                win32api.SetCursorPos([SaoLei.left + self.sure_boom_position[i][1] * SaoLei.block_width,
                                        SaoLei.top + self.sure_boom_position[i][0] * SaoLei.block_height])
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
                                self.hongqiNum = self.hongqiNum + 1
                                    # self.map[self.sure_boom_position[i][0],self.sure_boom_position[i][1]] = -5
                            # time.sleep(0.1)
                            self.round_detect2 = 1
                            mark2 = mark2 + 1
                            print('mark2')
                        else: pass
                        # time.sleep(2)
                        self.sure_boom_position = []
                        self.showmap()
                        self.hongqi_Statedict.setdefault(y_position + 8 * x_position, self.hongqiNum)
                        self.NotBoomNum = 0
                        self.hongqiNum = 0
                        if self.map[x_position][y_position] == -5 or self.map[x_position][y_position] == 1 or self.map[x_position][y_position] == 2 or self.map[x_position][y_position] == 3 \
                                    or self.map[x_position][y_position] == 4 or self.map[x_position][y_position] == 5 or self.map[x_position][y_position] == 6 \
                                    or self.map[x_position][y_position] == 8 or self.map[x_position][y_position] == -4:
                            self.Not_Click_list.append([x_position,y_position])
                        else: pass
                if self.hongqi_Statedict != {}:
                    self.hongqi_Statedict_save = self.hongqi_Statedict
                else: pass
                if self.rgba_0_Statedict != {}:
                    self.rgba_0_Statedict_save = self.rgba_0_Statedict
                else: pass
                print(self.round_detect2)
            print("self.Not_Click_list")
            print(self.Not_Click_list)
            self.probstate = self.Odds_Boom(self.rgba_0_Statedict_save,prob_para,self.hongqi_Statedict_save, self.Not_Click_list)
            print("self.probstate")
            print(self.probstate)
            self.all_position_probmax = self.Position_Allmin(self.probstate)
            print("self.all_position_probmax")
            print(self.all_position_probmax)
            self.random_positon = random.randint(0, len(self.all_position_probmax)-1)
            self.position_probmax = self.all_position_probmax[self.random_positon]
            print("self.position_probmax")
            print(self.position_probmax)
            self.position_x = round((self.position_probmax - (self.position_probmax % 8)) / 8)
            self.position_y = round(self.position_probmax % 8)
            mark3 = mark3 + 1
            print("mark3")
            win32api.SetCursorPos([SaoLei.left+self.position_y*SaoLei.block_width, SaoLei.top+self.position_x*SaoLei.block_height])
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
            # self.map[self.position_x][self.position_y] = -5
            # time.sleep(0.1)
            self.showmap()
            # SaoLei.img.show()
            # SaoLei.img.crop((0, 0, 16,16)).show()
            print("tanse")
            print(SaoLei.img.crop((0, 0, 16, 16)).getcolors())
            self.problist = np.zeros(shape=(SaoLei.blocks_x * SaoLei.blocks_y))
            # print(self.map)
            for k in range(SaoLei.blocks_x):
                for h in range(SaoLei.blocks_y):
                    print("mark6")
                    if self.map[k][h] != 0:
                        self.round_detect1_Num = self.round_detect1_Num + 1
                    else: pass
                    if self.map[k][h] == -6:
                        self.round_detect_Boom = 1
                    else: pass
            if self.round_detect1_Num == SaoLei.blocks_x * SaoLei.blocks_y or self.round_detect_Boom == 1:
                self.round_detect1 = 0
            else: pass
            # print(self.round_detect_Boom)
            # time.sleep(0.1)
            # self.showmap()
            # print(self.round_detect1)




    def Odds_Boom(self,rgba_0_State_para, prob_parameter,hongqi_State_para,NotClick_State_para):
        self.DictLen = 0
        for j in rgba_0_State_para.keys():
            position_x_round = round((j - (j % 8))/8)
            position_y_round = round(j % 8)
            self.DictLen = len(rgba_0_State_para[j])
            for i in rgba_0_State_para[j].keys():
                # position_x_i = round((i - (i % 8)) / 8)
                # position_y_i = round(i % 8)
                # if i !=
                print(i)
                if j in hongqi_State_para.keys():
                    if self.map[position_x_round][position_y_round] > 1:
                        print("i")
                        print(i)
                        prob_parameter[i] = prob_parameter[i] + comb(self.DictLen-1,self.map[position_x_round][position_y_round]-1-hongqi_State_para[j])\
                                                        /comb(self.DictLen,self.map[position_x_round][position_y_round]-hongqi_State_para[j])
                    elif self.map[position_x_round][position_y_round] == 1:
                        print(i)
                        prob_parameter[i] = prob_parameter[i] + 1/self.DictLen
                    else: pass
                else:
                    if self.map[position_x_round][position_y_round] > 1:
                        print(i)
                        prob_parameter[i] = prob_parameter[i] + comb(self.DictLen-1,self.map[position_x_round][position_y_round]-1)\
                                                        /comb(self.DictLen,self.map[position_x_round][position_y_round])
                    elif self.map[position_x_round][position_y_round] == 1:
                        print(i)
                        prob_parameter[i] = prob_parameter[i] + 1 / self.DictLen
                    else: pass
        for not_j in NotClick_State_para:
            print("max(prob_parameter)")
            print(max(prob_parameter))
            prob_parameter[not_j[1]+8*not_j[0]] = max(prob_parameter)
            print("not_j[1]+8*not_j[0]")
            print(not_j[1]+8*not_j[0])
        return prob_parameter

# 扫描雷区图像
    def showmap(self):
        SaoLei.gameover = 0
        SaoLei.img = ImageGrab.grab().crop(self.rect)
        # SaoLei.img.show()
        for y in range(SaoLei.blocks_y):
            for x in range(SaoLei.blocks_x):
                self.this_image = SaoLei.img.crop((y * SaoLei.block_width, x * SaoLei.block_height, (y + 1) * SaoLei.block_width,
                                       (x + 1) * SaoLei.block_height))
                if self.this_image.getcolors() == SaoLei.rgba_0:
                    self.map[x][y] = 0
                elif self.this_image.getcolors() == SaoLei.rgba_1:
                    self.map[x][y] = 1
                elif self.this_image.getcolors() == SaoLei.rgba_2:
                    self.map[x][y] = 2
                elif self.this_image.getcolors() == SaoLei.rgba_3:
                    self.map[x][y] = 3
                elif self.this_image.getcolors() == SaoLei.rgba_4:
                    self.map[x][y] = 4
                elif self.this_image.getcolors() == SaoLei.rgba_5:
                    self.map[x][y] = 5
                elif self.this_image.getcolors() == SaoLei.rgba_6:
                    self.map[x][y] = 6
                elif self.this_image.getcolors() == SaoLei.rgba_8:
                    self.map[x][y] = 8
                elif self.this_image.getcolors() == SaoLei.rgba_ed:
                    self.map[x][y] = -4
                elif self.this_image.getcolors() == SaoLei.rgba_hongqi:
                    self.map[x][y] = -5
                elif self.this_image.getcolors() == SaoLei.rgba_boom or self.this_image.getcolors() == SaoLei.rgba_boom_red:
                    SaoLei.gameover = 1
                    self.map[x][y] = -6
                    print("mark7")
                    sys.exit(0)
                else:
                    print("无法识别图像")
                    # print(self.map)
                    print(x,y)
                    sys.exit(0)
        return SaoLei.gameover

    def Position_Allmin(self,list):
        j = 0
        position_list = []
        for i in list:
            if i == min(list):
                position_list.append(j)
            j = j + 1
        return position_list

if __name__ == "__main__":
    saolei_game = SaoLei()