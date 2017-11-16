<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 
#apply(func[, nkw][, kw]) ,尽量不用,未来版本会弃用
lamAdd = lambda x, y: x + y 
print apply(lamAdd,(1,2)) #3


#filter(func, seq) ,过滤序列
lamUsuallyAdd = lambda x:type(x)==type(1)
numList = [1,2,3,'a']
print filter(lamUsuallyAdd,numList) #[1, 2, 3]

#将函数func 作用于给定序列（s)的每个元素
#map(func, seq1[,seq2...])   
lamUsuallyAdd = lambda x, y=2: x+y 
list1 = [1,1,1]
list2 = [1,2,3]
list3 = [4,5,6]
print map(lamUsuallyAdd,list1) #[3, 3, 3]
print map(None,list1,list2,list3) #[(1, 1, 4), (1, 2, 5), (1, 3, 6)] 


#reduce(func, seq[, init])   
#对sequence中的item顺序迭代调用function，如果有init，还可以作为初始值调用，例如可以用来对List求和：
lamAdd = lambda x, y: x + y 
print reduce(lamAdd,range(1,5)) #10 
print reduce(lamAdd,range(1,5),20) #30 
</code></pre>
