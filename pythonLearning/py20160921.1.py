# coding=utf-8 #使用中文必须加这一句
import numpy as np
# a = 'hi,python!'+'!'
# b = 'hello'
# # c = >>a
# str1='1%c1%c%d'%('+','=',2)
# str2='%d'%0xA
# str3=int('12')
# str4='abcd'
# str5=str4.capitalize()
# print ('%d' %(0xa+0x7))
# print('中文')
# print (len(b))
# print (str3)
# print(str5)
# #原始字符串，用于正则表达式中的路径
# # import os
# # path=r'd:\software'
# # print (os.listdir(path))
# #
# # 元组与列表
# list2=['a','b','c']
# list2.append('d')
# print(list2)
# string1="abced"
# string1=string1[4]
# print(string1)
# a=[1,2]+[1,2,3]
# print(a)
#
# tuple=('a','b','c','d')
# print(tuple[1])
#
# dic={'a':1,'b':2}
# print(dic['b'])
# dic['c']=5
# print(dic)
# dic=dic.items()
# print(dic)
#
# file=open('d:\python.txt','w')
# file.write('a\nb\nc\nd\ne')
# file=open('d:\python.txt','r')
# s=file.readline()
# d=file.readline()
# str1=file.readline()
# # s=file.readlines()
# print(s)
# print(d)
# print(str1)

# #python语句if
# list1=[3,'a'] #a和b使用的是ASCII码
# list2=[3,'b']
# if list1>list2: #两个list比较大小，首先比较第一个，第一个比较完了，如果相等则比较第二个
#     print(1)
# elif list1>=list2:
#     print(2)
# else:
#     print(3)
# list =range(1,7,2)
# print(list)

# #for循环
# people={'xufang':'xufang','sunshujuan':'sunshujuan','zahngxuguang':'zhangxuguang','zhouxin':'zhouxin'}
# for i in people:
#     if i=='sunshujuan':
#         print (people[i])
#         continue
#         print('zhouxin')
#     elif i=='xufang1': #这里使用if和elif都行
#         print(people[i])
#         break
# else:
#     print('xufang is a good student')

# list=[['a','b'],['c','d'],['e','f']]
# tuple=(('a','b'),('c','d'),('e','f'))
# for [x,y] in tuple:
#     print x,y
# for (x,y) in list:
#     print (x,y)

# #for循环的嵌套，求50到1000间的所有素数
# import math
# list=[]
# for i in range(50,100,1):
#     for j in range(2,int(math.sqrt(i))+1,1):
#         if i%j==0:
#             break
#     else:
#         print(i)
#         list.append(i)
#     print(list)

#函数
#函数的声明
# def hi():
#     print('xufang is a good student')
# hi()
# #求和函数，求1一直加到A的和
# def sum(A):
#     s=0
#     for i in range(1,A+1,1):
#         s=s+i
#     return s
# print(sum(100))

# #函数的参数混合传递方式
# def cub(x=1,y=2,z=3):
#     return x+y-z
# print(cub(x=2,y=3,2))

# b=[2]
# b[0]=3
# print(b)
#
# #lambda表达式
# fun = lambda  x : x+2
# print(fun(3))

# #建立一个模块moduleexample,并调用
# import moduleexample
# moduleexample.show()
# print(moduleexample.name)
# moduleexample.name='your module'
# name='abc'
# print (moduleexample.name)

#模块的_name_属性
#建立模块moduleexample2
# import moduleexample2
# moduleexample2.show()
# import moduleexample
# print(dir(moduleexample))

#正则表达式
# s='life cccaan can (sewwre)35555) cn an one be good good goodd'
import re
# print (re.search('can',s))
# print (re.match('l',s))
# print (re.findall('e c',s))
# print (re.findall('c.+an',s))
# print (re.subn('good|be','bad',s,1))
# r=re.subn('good|be','bad',s,3)
# print(r[0])
# print(r[1]) #显示替换次数
# print (re.findall('\\bc.*?\\b',s))
# print (re.findall('\\so.+?',s))
# print (re.findall('[a-z]{3}',s))
# print (re.sub('good','bad',s,2))
# print (re.findall('\\Bo.+?\\b',s))
# print (re.findall('c*an',s))
# print (re.findall('\(\\w+\)',s))
# print('\\\\na\b\nac')
# s='''life can be good;
#   ...life can be bad'''
# r=re.compile(r'be(?=\sgood|bad)')
# m=r.search(s)
# print(m.groups())
# print (m.span())
# #组的用法
# s='''life can be dreams
#  life can be great thoughts life can mean a person;
# ...life can mean a person'''
# r=re.compile(r'\b(?P<first>\w.+)a(?P<second>\w.+)\b')
# m=r.search(s,0)
# print(m)
# print(m.groups())
# print(m.group(1))
# print(m.group(2))
# print(m.groupdict())

import re
# import sys
# if len(sys.argv)==1:
#     sour = raw_input('请输入要处理的文件路径：')
# else:
#     sour=sys.argv[1]
# file = open(sour)
# s=file.readlines()
# file.close()
# print '***************************************'
# print sour,'中的函数有：'
# print '***************************************'
# i=0
# #循环处理每一行，匹配其中的函数，并输出函数所在的行号以及函数原型
# for line in s:
#     i=i+1
#     var = DealwithVar(line)
#     if len(var) == 1:
#         print 'Line: ' ,i,'\t',var[0]


# file = open(r'd:\GetFunction.txt','w')

# # 类的使用
# class A:
#     __name=''
#     price=0
#     name='1'
# a=A()
# a.price=20
# a.name='xufang'
# print(a.name)
# A.__nam3 ='sunshujuan'
# print(A.__nam3)
# A.price=30
# print a.price
# b=A()
# print(b.__nam3)
# #类的方法
# class book:
#     price = 20  #定义一个公有属性
#     __name = '1'
#     __author = '2'
#     def show(self):
#         print self.price
#         print self.__name
#         print self.__author
#     def set(self,name,author):
#         self.__name = name
#         self.__author = author
# # book.set('xufang', 'sunshujuan')  #这句话报错
# a = book()
# print a.show()
# a.set('xufang','sunshujuan')
# print a.show()
# b=book()
# print b.show()
#类的专有方法
# class book:
#     price = 20  #定义一个公有属性
#     __class = '1'
#     __author = '2'
#     def show(self):
#         print self.__class
#         print self.__author
# #     def __init__(self,author,class):
# #         self.__author = author
# #         self.__name = class
# # a = book('xufang','sunshujuan')
# # a.show()
# # b = book( '', '' )
# b=book()
# b.show()
#类的多重继承
# class A:
#     a = 1
#     b = 2
#     c = 3
#     def show(self,a,b,c):
#         print a
#         print b
#         print c
# class B:
#     def show(self):
#         print 'sunshujuan'
# class C(A,B):
#     def show(self,a,b,c,d,e):
#         # print a
#         # print b
#         # print c
#         print d
#         print e
# c=C()
# print c.show(4,5,6,7,8)

#捕获异常
# l=[1,2,3]
# try:
#     l[2]/0
# except IndexError,erro:
#     print('indexerror')
#     print erro
# except ZeroDivisionError,errr:
#     print('ZeroDivisionError')
#     print(errr)
# except:
#     print 'error'
# else:
#     print 'No Error'
# l='abcde'
# print len(l)
import pdb
# pdb.set_trace()
# for i in range(0,1):
#     i=i*5
#     print i
# for i in range(0, 6):
#     i = i * 5
#     print i
# print('''
# for i in range(0,3):
# i=i*2
# print i
# ''')
# l=[1,2,3]
# pdb.run('''
# for i in range(0,3):
#     i=i*2
#     print i
# ''')
# reload(sys)
# def sum1(a=1):
#     a+=1
#     return a
# b=sum1()
# print(b)
# c=sum1()
# print(c)
# d=sum1()
# print(d)
# tuple1=(1,2)
# tuple2=(2,3)
# tuple3=tuple2+tuple1
# print(tuple3)
# a=np.arange(1,10,1)