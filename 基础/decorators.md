<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 

#@deco1(deco_arg)
#@deco2
#def func(): pass
#这等价于：
#func = deco1(deco_arg)(deco2(func))

from time import ctime, sleep

def tsfunc(func):
    def wappedFunc():
        print '[%s] %s() called' % (ctime(), func.__name__)
        return func()
    return wappedFunc


@tsfunc
def foo():
    pass 

foo()
sleep(4)

for i in range(2):
    sleep(1)
    foo()
    
@<修饰1>
@<修饰2>
def <函数名>:
    <函数体>    
翻译:    
<函数名> = <修饰1>(<修饰2>(<函数名>))    
    
</code></pre>    
