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
</code></pre>    
