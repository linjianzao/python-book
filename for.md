#for

####语法:
<pre><code>
for iterating_var in sequence:
   statements(s)
</code></pre>

####for、in、continue
<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 

for item in ["mail","surfing","homework","chat"]:
    if item == "mail":
        continue #跳过这次for
    print item
    
</code></pre>
执行结果:<br> 
surfing<br>
homework<br>
chat<br>


####素数:除了1和它本身外，不能被其他自然数整除
<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 
for num in range(10, 20):  #range构造出从10开始到19结束的list, [10,11...,19]
    for i in range(2,num): #构造出除1和它本身以外的 list
        if num%i == 0:     #是否能被整除 
            j = num/i
            print '%d 等于 %d * %d' % (num,i,j)
            break  #退出这次循环
    else: #for else, 这种语法是，for循环完后执行一次else操作,上面的break会打断不是素数的情况
        print num,"是素数"
</code></pre>
结果:<br>
10 等于 2 * 5<br>
11 是素数<br>
12 等于 2 * 6<br>
13 是素数<br>
14 等于 2 * 7<br>
15 等于 3 * 5<br>
16 等于 2 * 8<br>
17 是素数<br><br>
18 等于 2 * 9<br>
19 是素数<br>




