#- * - coding: gbk -*-

#!/usr/bin/envpython
background_image_filename='sushiplate.jpg'
mouse_image_filename='fugu.png'
#ָ��ͼ���ļ�����
import pygame
#����pygame��
from pygame.locals import *
#����һЩ���õĺ����ͳ���
from sys import exit
#��sysģ���һ��exit���������˳�����
pygame.init()
#��ʼ��pygame,Ϊʹ��Ӳ����׼��
screen=pygame.display.set_mode((640,480),0,32)
#������һ������
pygame.display.set_caption("Hello,World!")
#���ô��ڱ���
background=pygame.image.load(background_image_filename).convert()
mouse_cursor=pygame.image.load(mouse_image_filename).convert_alpha()
#���ز�ת��ͼ��
while Ture:
#��Ϸ��ѭ��
    for event in pygame.event.get():
        if event.type==QUIT:
#���յ��˳��¼����˳�����
            exit()
screen.blit(background,(0,0))
#������ͼ����ȥ
x,y=pygame.mouse.get_pos()
#������λ��
x-=mouse_cursor.get_width()/2
y-=mouse_cursor.get_height()/2
#����������Ͻ�λ��
screen.blit(mouse_cursor,(x,y))
#�ѹ�껭��ȥ
pygame.display.update()
#ˢ��һ�»���3
