#!/bin/env python
# -*- coding:utf8 -*- 

#定义：确保一个类只有一个实例，而且自行实例化并向整个系统提供这个实例。 
#单例模式根据实例化对象时机的不同分为两种：
#饿汉式单例:在单例类被加载时候，就实例化一个对象交给自己的引用；
#懒汉式单例:在调用取得实例方法的时候才会实例化对象。代码如下：

class Node(object):
    pass

n = Node()
m = Node()
n.a = 1 
m.a = 2 
print n.a 
print m.a 

class Borg(object):
    __shared_state = dict()

    def __init__(self):
        self.__dict__ = self.__shared_state 
        
    def __str__(self):
        return self.state


class YourBlog(Borg):
    pass

if __name__ == '__main__':
    rm1 = Borg()
    rm2 = YourBlog()
    rm1.a = 'aaa'
    rm2.a = 'vvv'
    print rm1.a
    print rm2.a
    rm1.b = 3 
    rm2.b = 4 
    print rm1.b
    print rm2.b
