# coding=utf-8 #使用中文必须加这一句
# file: GetFunction.py
#
import re
import sys
def DealwithFunc(s):
    r=re.compile(r'''
        (?<=def\s)
        \w+
        \(.*?\)
        (?=:)
        ''',re.X)
    return  r.findall(s)
def DealwithVar(s):
    vars=[]
    r=re.compile(r'''
        \b
        \w+
        (?=\s=)
        ''',re.X)
    vars.extend(r.findall(s))
    r = re.compile(r'''
        (?<=for\s)
        \w+
        \s
        (?=in)
        ''', re.X)
    vars.extend(r.findall(s))
    return vars
if len(sys.argv) == 1:
    sour = raw_input('请输入要处理的文件路径：')
else:
    sour = sys.argv[1]
file = open(sour)
s=file.readlines()
file.close()
# print '***************************************'
# print (sour , '中的函数有：')
# print '***************************************'
i=0
#循环处理每一行，匹配其中的函数，并输出函数所在的行号以及函数原型
for line in s:
    i = i + 1
    function = DealwithFunc(line)
    if len(function) == 1:
        print 'Line: ' ,i,'\t',function[0]

for line in s:
    i = i + 1
    var = DealwithVar(line)
    if len(var) == 1:
        print 'Line: ' ,i,'\t',var[0]
print(sour)

