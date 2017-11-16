#while

####语法:
<pre><code>
while expression:
    while_suite
</code></pre>
<br>
<br>
    
####例子
<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 

count = 0 
while count < 3:
    print count
    count += 1
    
</code></pre>
<br>
<br>

####用作守护进程
<pre><code>
a = 1
while True:
    if a == 5:
        break  #退出while
    print a
    a += 1
</code></pre>
结果:<br>
1<br>
2<br>
3<br>
4<br>
