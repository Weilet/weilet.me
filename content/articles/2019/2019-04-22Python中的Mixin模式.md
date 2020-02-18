Title: Python中的Mixin模式
Date: 2019-04-22 10:12
Author: PwnForWhat
Category: Tech
Tags: Python, OOP
Slug: Python中的Mixin模式
Status: published


### 什么是Mixin
Mixin是面向对象程序设计语言中的类，提供了方法的实现。

### 为什么需要 Mixin

[首先我们需要明白，Python 中是支持多继承的。那么，你可能会问，既然 Python 支持多继承，那多继承和 使用 Mixin 有什么不同呢？]{.md-plain} [从逻辑角度上看，多继承混淆了子类的属性，继承关系应当是 is-a 的关系的，至于其他多余的、不能从父类获取，应当利用其他方法去添加。]{.md-plain} [在 Java 中，interface 解决了这个问题。一个类继承了父类后，如果需要其他属性，可以通过实现接口来解决。这使得代码的可读性变强。]{.md-plain} [同样，在 Python 中，只有一个父类，至于继承的 Mixin，只是提供了方法的实现。它的名字应当是这样的 NameMixin，而且它应该具备以下特点：

-   首先它必须表示某一种功能，而不是某个物品，如同Java中的Runnable，Callable等
-   其次它必须责任单一，如果有多个功能，那就写多个Mixin类
-   然后，它不依赖于子类的实现
-   最后，子类即便没有继承这个Mixin类，也照样可以工作，就是缺少了某个功能。 （参考思诚之道）

### 具体例子

``` python
class FlyMixin(Object):
    def fly():
        pass
class Airplane(Transportation, FlyMixin):
    # 将 FlyMixin 中的 fly 实现
    def fly(self):
        print(f'{self} is flying')
        # 其他代码
```

### 注意

由于继承顺序的问题，应当将主类放在子类继承的最左边。
