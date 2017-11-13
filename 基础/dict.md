#dict

<pre><code>
#!/bin/env python
# -*- coding:utf8 -*- 


dictA = dict() #定义一个空dict

dictA["a"] = "A" #赋值

dictA["a"] = "Aa" #更新

dictB = {"b":"B"} #定义一个有值的dict

dictB["c"] = "c"

print 'dictB["b"]:', dictB["b"] #访问dictB ,结果B
print dictB.get("b",None) #用get访问可以指定如果没有对应的键返回什么值

del dictB["b"]  #删除一个元素
print dictB #结果:{'c': 'c'}

dictB.clear() #清空dictB
print dictB #结果{}

dictC = {"a":"A","b":"B","c":[1,2,3]}
print len(dictC) #dictC的长度，结果 3

import copy

dictD = dictC
dictE = copy.copy(dictC)
dictF = copy.deepcopy(dictC)

dictC["d"] = "d" 
dictC["c"].append(4)
print dictD #结果{'a': 'A', 'c': [1, 2, 3, 4], 'b': 'B', 'd': 'd'}
print dictE #结果{'a': 'A', 'c': [1, 2, 3, 4], 'b': 'B'}
print dictF #结果{'a': 'A', 'c': [1, 2, 3], 'b': 'B'}
#结论 python 对象默认都是引用的，所以如果不想两个一样的字典互相干扰，就用deepcopy或copy
#那deepcopy 和 copy的区别是 copy 如果字典里的键有子对象，那修改这个子对象一样会干扰copy的，
#如果用deepcopy就不会有干扰 ,记得deepcopy是完全断绝关系就是了

print dir(dict) #查看一个对象支持哪些方法

#方法及描述
#dict.clear()     删除字典dict中的所有元素
#
#dict.copy()      返回字典dict的浅表副本
#
#dict.fromkeys()  创建一个新的字典，设置键为seq 和值为value
#
#dict.get(key, default=None) 对于键key，返回键，如果不是在字典的值或默认
#
#dict.has_key(key) 如果在字典dict中存在键key，则返回true，否则返回 false
#
#dict.items()     返回字典的（键，值）元组对的列表
#
#dict.keys()      返回字典的键的列表
#
#dict.setdefault(key, default=None)  类似get()，但会设定dict[key]=default如果key不是已经在于字典中
#
#dict.update(dict2)   增加字典dict2的键值对到字典中
#
#dict.values()      返回字典dict的值列表

</code></pre>
