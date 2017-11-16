#tuple

<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 

#tuple 删改查操作

tu = tuple() #定义一个空的元祖
tuA = ("a",) #定义只有一个值的元组，注意后面的逗号

tuB = ("a","b","c")
print "tuB[0]:",tuB[0] #用下标访问元组，下标从0开始 ,结果a

print "tuB[-1]:",tuB[-1] # 结果 c

print "tuB[2:3]:",tuB[2:3] #切片访问元组('b', 'c'), 从下标1开始，到长度3为止

print "tuB[1:1]:",tuB[1:1] #结果是() ,

print "tuB[0:3:2]:",tuB[0:3:2] #结果('a', 'c') ,第三个参数是间隔多少

print "tuB[1:]:",tuB[1:] #从第二个元素开始取全部,('b', 'c') 

#元组由于不可变，所以只能del 整个元组 不能单独删除元组元素

print len((1, 2, 3)) #结果3

print (1, 2) + (4, 5) #结果(1, 2, 4, 5)

print ('Hi!',) * 4 #结果('Hi!', 'Hi!', 'Hi!', 'Hi!')

print 3 in (1, 2, 3) #结果True

print max((1,2,3)) #结果3

print min((1,2,3)) #结果1

for x in (1, 2, 3): print x, #结果: 1 2 3

print max((1,2,3)) #结果3

print sum((1,2,3)) #结果6

print zip((1,2,3)) #结果[(1,), (2,), (3,)]

print zip((1,2,3),(4,5,6),(7,8)) #结果[(1, 4, 7), (2, 5, 8)]

</code></pre>
<br><br>
tuple(iter) 把一个可迭代对象转换成一个元组对象
<br><br>
####列出索引和值
<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 
for k,v in enumerate(tuB):
    print k,v
    
</code></pre>
结果:<br>
0 a<br>
1 b<br>
2 c<br>
<br><br>
