# !/usr/bin/python
# -*- coding: UTF-8 -*-
# super 函数用法意义
class FooParent(object):
    def __init__(self):
        self.parent = 'I\'m the parent.'
        print('Parent1')
        print('Parent2')

    def bar(self, message):
        print("%s from Parent" % message)


class FooChild(FooParent):
    def __init__(self):
        # super(FooChild,self) 首先找到 FooChild 的父类（就是类 FooParent），然后把类FooChild的对象  转换为类 FooParent 的对象
        super(FooChild, self).__init__()
        print('Child')

    def bar1(self, message):
        super(FooChild, self).bar(message)
        print('Child bar fuction')
        print(self.parent)
        print('%s from child' % message)


if __name__ == '__main__':
    fooChild = FooChild()
    fooChild.bar1('HelloWorld')
