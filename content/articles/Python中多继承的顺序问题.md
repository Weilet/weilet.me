Title: Python中多继承的顺序问题
Date: 2019-04-23 22:47
Author: PwnForWhat
Category: Code
Tags: Python, OOP
Slug: Python中多继承的顺序问题
Status: published


### 从左到右


``` python
class A(Object):
    def __init__(self):
        pass
    def say(self):
        print('I am a A')
class B(Object):
    def __init__(self):
        pass
    def say(self):
        print('I am a B')

class C(A, B):
    def __init__(self):
        pass

c = C()
c.say()

# I am a A
# 搜索过程如下，先搜索A，A中有say()，调用A类中的say()，结束
```

### 广度优先

``` python
class A():
    def __init__(self):
        pass
    def say(self):
        print('I am a A')
class B(A):
    def __init__(self):
        pass
class C(A):
    def __init__(self):
        pass
    def say(self):
        print('I am a C')
class D(B,C):
    def __init__(self):
        pass
d =  D()
d.say()

# I am a A
# 搜索过程如下，先搜索B，B中没有，搜索C，C中有say()，结束
# 事实上，调用的方法会先从子类的父类遍历寻找，然后是父类的父类，直到寻找完所有的超类
```

### 总结

以上两点是 Python 中关于继承顺序容易弄混的地方。

你可以调用 \_\_mro\_\_ 查看继承的图谱，它是一个从子类出发，直到 Object 的元组