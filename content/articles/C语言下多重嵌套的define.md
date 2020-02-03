Title: C 语言下多重嵌套的define
Date: 2019-04-28 13:47
Author: PwnForWhat
Category: Code
Tags: C, CPP
Slug: C语言下多重嵌套的define
Status: published


有以下一段宏：


``` c
#define _STR(x) _VAL(x)
#define _VAL(x) #x
```

原以为只是 define \_VAL(x) \#x 起效果，并不清楚 define \_STR(x) \_VAL(x) 的作用。

因为使用 int x = 5 去测试，发现无论是 \_STR() 还是 \_VAL() 都是输出 x

后来发现，如果改为在顶部添加

``` c
#define x 100
```

\_STR() 的值为 "100" 而 \_VAL()的值为 "x"

由此可以得知，所谓的 define \_STR(x) \_VAL(x) 用于获取十进制常量的意思，就是获取参数在define时的值（而非赋值操作的值），进而通过 \#x 转换为字符串量。

最后，附上测试的代码，你可以自行验证：

``` c
#include <stdio.h>
#define t 100
#define _STR(x) _VAL(x)
#define _VAL(x) #x
void print(char *p) {
      printf("%s\n", p);
}
int main(void) {
      print(_STR(t)"+");
      return 0;
}
```