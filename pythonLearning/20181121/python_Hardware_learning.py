# -*- coding: utf-8 -*-
# Function: 变量的作用域空间
# name = "whole global name"
# class Person:
#     name = "class global name"
#     def __init__(self,newPersonName):
#         self.name = newPersonName
#
#     def showName(self):
#         name = "wuyan"
#         print("My name is %s" %(name))
#         print("Your name is %s" % (self.name))
#         print("His name is %s" % (Person.name))
#
# def Pobject():
#     personObject = Person("xufang")
#     personObject.showName()
#     print("Her name is %s" % (name))
#
# if __name__ == "__main__":
#     Pobject()


# Function：画函数图像
import sys
from tkinter import *
from math import *

class wave :
    def __init__(self, points=400, formula = None, period = 1):
        self.data = [0.0]*points
        self.points = points
        self.formula = formula
        self.period = period
        if formula :
            for p in range(points):
                x = p*pi*2* period /points
                self.data[p] = eval(formula)

    def __add__(self, other):
        target = wave(points = self.points)
        for i in range(self.points):
            target.data[i] = self.data[i] + other.data[i]
            return target

    def __mul__(self, other):
        target = wave(points = self.points)
        if type(other) == type(5) or type(other) == type(5.0):
            for i in range(self.points):
                target.data[i] = self.data[i] * other
        else :
            for i in range(self.points):
                target.data[i] = self.data[i] * other.data[i]
                return target

    def __sub__(self, other):
        target = wave(points = self.points)
        for i in range(self.points):
            target.data[i] = self.data[i] - other.data[i]
            return target

    def integral(self):
        ans = 0.0
        for pt in self.data :
            ans  = ans + pt
        return ans * 2 * pi / self.points

    def plot(self,title = "??", pixHeight = None, pixWidth = None, maxY = None,others = []):
        # pixHeight = self.points*2/3 # pleasant ratio
        # pixWidth = self.points
        # find max and min data to scale
        maxY = max(max(self.data),-min(self.data))
        offset = pixHeight/2
        scale = offset/maxY
        # create windows by Tk
        win = Tk()
        win.title(title)
        canvas1 = Canvas(win,width = pixWidth, height = pixHeight)
        #create zero line
        canvas1.create_line(0, offset,pixWidth,offset)
        canvas1.pack()
        self.plotOne(canvas1, pixWidth,scale,offset)
        for i in range(len(others)):
            others[i].plotOne(canvas1, pixWidth, scale, offset)
        if sys.platform == "win32":
            win.mainloop()

    def plotOne(self, canvas2, pixWidth, scale, offset):
        isinstance1 = wave(points = pixWidth, formula= self.formula, period = self.period)
        for x in range(pixWidth):
            y = offset - isinstance1.data[x] * scale
            # if x:
            canvas2.create_line(x-1, y, x, y)
                # yprev = y
        print(isinstance1.data)


    def fft(self):
            work = self *1 # Harmonics will be stripped from this
            for harm in range(1,10):
                formula = "-sin(%d * x)" % harm
                area = (wave(formula = formula) * work).integral()
                amplitude = area/-pi
                if amplitude > .000001:
                    print("Harmonic=",harm, "Amplitude=%.04f" %amplitude)
                takeAway = wave(formula = "sin(%d * x) * %f" %(harm, amplitude))
                work = work-takeAway

# def test():
#     p1 = wave(formula = "sin(x)/1")
#     p3 = wave(formula = "sin(3*x)/3")
#     p5 = wave(formula = "sin(5*x)/5")
#     mys = p1+p3+p5
#     mys.fft()
#
# if __name__ == "__main__" :
#     test()


# # test code
# import python_Hardware_learning
# a = python_Hardware_learning.wave(formula = "sin(x)/1")
# b = python_Hardware_learning.wave(formula = ".5 * sin(2*x)")
# a.plot(maxY = 1.2, pixHeight = 200, title = "Sin(x)", others=[b])
# c = a + b
# c.plot(maxY = 1.5, pixHeight = 200, title = "Sin(x) plus 0.5*Sin(2*x)")





# # -*- coding: utf-8 -*-
# # Function: 变量的作用域空间
# # name = "whole global name"
# # class Person:
# #     name = "class global name"
# #     def __init__(self,newPersonName):
# #         self.name = newPersonName
# #
# #     def showName(self):
# #         name = "wuyan"
# #         print("My name is %s" %(name))
# #         print("Your name is %s" % (self.name))
# #         print("His name is %s" % (Person.name))
# #
# # def Pobject():
# #     personObject = Person("xufang")
# #     personObject.showName()
# #     print("Her name is %s" % (name))
# #
# # if __name__ == "__main__":
# #     Pobject()
#
#
# # Function：画函数图像
# import sys
# from  tkinter import *
# from math import *
#
# class wave :
#     def __init__(self, points=400, formula = None):
#         self.data = [0.0]*points
#         self.points = points
#         if formula :
#             for p in range(points):
#                 x = p*pi*2/points
#                 self.data[p] = eval(formula)
#
#     def __add__(self, other):
#         target = wave(points = self.points)
#         for i in range(self.points):
#             target.data[i] = self.data[i] + other.data[i]
#             return target
#
#     def __mul__(self, other):
#         target = wave(points = self.points)
#         if type(other) == type(5) or type(other) == type(5.0):
#             for i in range(self.points):
#                 target.data[i] = self.data[i] * other
#         else :
#             for i in range(self.points):
#                 target.data[i] = self.data[i] * other.data[i]
#                 return target
#
#     def __sub__(self, other):
#         target = wave(points = self.points)
#         for i in range(self.points):
#             target.data[i] = self.data[i] - other.data[i]
#             return target
#
#     def integral(self):
#         ans = 0.0
#         for pt in self.data :
#             ans  = ans + pt
#         return ans * 2 * pi / self.points
#
#     def plot(self,title = "??", pixHeight = None, maxY = None,others = []):
#         if not pixHeight :
#             pixHeight = self.points*2/3 # pleasant ratio
#             pixWidth = self.points
#             # find max and min data to scale
#             if not maxY :
#                 maxY = max(max(self.data),-min(self.data))
#             offset = pixHeight/2
#             scale = offset/maxY
#             # create windows by Tk
#             win = Tk()
#             win.title(title)
#             canvas = Canvas(win,width = pixWidth, height = pixHeight)
#             #create zero line
#             canvas.create_line(0, offset,pixWidth,offset)
#             canvas.pack()
#             self.platOne(canvas, pixWidth,scale,offset)
#             for i in range(len(others)):
#                 others[i].plotOne(canvas, pixWidth, scale, offset)
#             if sys.platform == "win32":
#                 win.mainloop()
#     def plotOne(self, canvas, pixWidth, scale, offset):
#         for x in range(pixWidth):
#             y = offset - self.data[x] * scale
#             if x:
#                 canvas.create_line(x-1, yprev, x, y)
#                 yprev = y
#
#     def fft(self):
#             work = self *1 # Harmonics will be stripped from this
#             for harm in range(1,10):
#                 formula = "-sin(%d * x)" % harm
#                 area = (wave(formula = formula) * work).integral()
#                 amplitude = area/-pi
#                 if amplitude > .000001:
#                     print("Harmonic=",harm, "Amplitude=%.04f" %amplitude)
#                 takeAway = wave(formula = "sin(%d * x) * %f" %(harm, amplitude))
#                 work = work-takeAway
#
# def test():
#     p1 = wave(formula = "sin(x)/1")
#     p3 = wave(formula = "sin(3*x)/3")
#     p5 = wave(formula = "sin(5*x)/5")
#     mys = p1+p3+p5
#     mys.fft()
#
# if __name__ == "__main__" :
#     test()
#
#
# # # test code
# # import python_Hardware_learning
# # a = python_Hardware_learning.wave(formula = "sin(x)/1")
# # b = python_Hardware_learning.wave(formula = ".5 * sin(2*x)")
# # a.plot(maxY = 1.2, pixHeight = 200, title = "Sin(x)", others=[b])
# # c = a + b
# # c.plot(maxY = 1.5, pixHeight = 200, title = "Sin(x) plus 0.5*Sin(2*x)")






