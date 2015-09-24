#list

<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 

#list 删改查操作

li = list() #定义一个空的元祖
liA = ("a",) #定义只有一个值的元组，注意后面的逗号

liB = ("a","b","c")
print "liB[0]:",liB[0] #用下标访问元组，下标从0开始 ,结果a

print "liB[-1]:",liB[-1] # 结果 c

print "liB[2:3]:",liB[2:3] #切片访问['b', 'c'], 从下标1开始，到长度3为止

print "liB[1:1]:",liB[1:1] #结果是[] ,

print "liB[0:3:2]:",liB[0:3:2] #结果['a', 'c'] ,第三个参数是间隔多少

print "liB[1:]:",liB[1:] #从第二个元素开始取全部,['b', 'c'] 

print len([1, 2, 3]) #结果3

print [1, 2] + [4, 5] #结果[1, 2, 4, 5]

print ['Hi!',] * 4 #结果['Hi!', 'Hi!', 'Hi!', 'Hi!']

print 3 in [1, 2, 3] #结果True

print max([1,2,3]) #结果3

print sum([1,2,3]) #结果6

print zip([1,2,3]) #结果[[1,], [2,], [3,]]

print zip([1,2,3],[4,5,6],[7,8]) #结果[[1, 4, 7], [2, 5, 8]]

delList = [1,2,3]
del delList[0]
print "delList:",delList  #结果[2, 3]

for x in [1, 2, 3]: print x, #结果: 1 2 3
</code></pre>
<br><br>

####list(iter) 把一个可迭代对象转换成一个元组对象

<br><br>
####列出索引和值
<pre><code>
for k,v in enumerate(liB):
    print k,v
</code></pre>
结果
0 a
1 b
2 c
