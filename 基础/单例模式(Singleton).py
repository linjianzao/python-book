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
 
print '------------------------------------------------------------------------------------------' 
 
 
#实现一:重载new 
#来源:http://ghostfromheaven.iteye.com/blog/1562618 
#将一个类的实例绑定到类变量_instance上,   
#如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回   
#如果cls._instance不为None,直接返回cls._instance   
class Base(object): 
    def __new__(cls, *arg, **kw): #重载__new__ 
        if not hasattr(cls, '_instance'): 
            ori = super(Base,cls) 
            cls._instance = ori.__new__(cls, *arg, **kw) 
        return cls._instance 
 
class MyClass(Base): 
    a = 1 
 
 
if __name__ == '__main__': 
    print "实现一" 
    one = MyClass() 
    two = MyClass() 
    two.a = 2 
    print one.a 
     
    one.b = 3 
    print two.b 
 
    print ('one:',one) 
    print ('two:',two) 
    print 'one id:',id(one) 
    print 'two id:',id(two) 
    print '------------------------------------------------------------------------------------------' 
 
 
#实现二:共享属性 
#来源:http://ghostfromheaven.iteye.com/blog/1562618 
#所谓单例就是所有引用(实例、对象)拥有相同的状态(属性)和行为(方法)   
#同一个类的所有实例天然拥有相同的行为(方法),   
#只需要保证同一个类的所有实例具有相同的状态(属性)即可   
#所有实例共享属性的最简单最直接的方法就是__dict__属性指向(引用)同一个字典(dict)   
class Borg(object): 
    _state = dict() 
    def __new__(cls,*arg,**kw): 
        ob = super(Borg,cls).__new__(cls,*arg,**kw) 
        ob.__dict__ = cls._state 
        return ob 
 
 
class MyClass2(Borg): 
    a = 1 
 
if __name__ == '__main__': 
    print "实现二" 
    one = MyClass2() 
    two = MyClass2() 
    two.a = 2 
    print one.a 
     
    one.b = 3 
    print two.b 
 
    print ('one:',one) 
    print ('two:',two) 
    print 'one id:',id(one) 
    print 'two id:',id(two) 
 
    print '------------------------------------------------------------------------------------------' 
 
#实现三:实现二的简化版 
class Borg(object): 
    __shared_state = dict() 
 
    def __init__(self): 
        self.__dict__ = self.__shared_state  
         
 
class YourBlog(Borg): 
    pass 
 
if __name__ == '__main__': 
    print "实现三" 
    rm1 = YourBlog() 
    rm2 = YourBlog() 
    rm1.a = 2  
    print rm1.a 
     
    rm2.a = 3 
    print rm1.a 
 
    print ('rm1:',rm1) 
    print ('rm2:',rm2) 
    print 'rm1 id:',id(rm1) 
    print 'rm2 id:',id(rm2) 
 
    print '------------------------------------------------------------------------------------------' 
         
 
 
#实现四:元类、本质上是实现一的升级（或者说高级）版 
#使用__metaclass__（元类）的高级python用法   
#来源:http://ghostfromheaven.iteye.com/blog/1562618 
class Singleton2(type): 
    def __init__(cls,name,bases,dict): 
        super(Singleton2,cls).__init__(name,bases,dict) 
        cls._instance = None 
 
    def __call__(cls,*arg,**kw): 
        if cls._instance is None: 
            cls._instance = super(Singleton2,cls).__call__(*arg,**kw) 
        return cls._instance 
class MyClass3(object): 
    __metaclass__ = Singleton2 
 
if __name__ == '__main__': 
    print "实现四" 
    one = MyClass3() 
    two = MyClass3() 
    two.a = 2 
    print one.a 
     
    one.b = 3 
    print two.b 
 
    print ('one:',one) 
    print ('two:',two) 
    print 'one id:',id(one) 
    print 'two id:',id(two) 
 
    print '------------------------------------------------------------------------------------------' 
 
 
#实现五:装饰器、也是方法1的升级（高级）版本 
#单例类本身根本不知道自己是单例的,因为他本身(自己的代码)并不是单例的   
 
def singleton(cls,*arg,**kw): 
    instances = dict() 
    def _singleton(): 
        if cls not in instances: 
            instances[cls] = cls(*arg,**kw) 
        return instances[cls] 
    return _singleton 
 
@singleton 
class MyClass4(object): 
    a = 1 
    def __init__(self,x=0): 
        self.x = x 
 
if __name__ == '__main__': 
    print "实现五" 
    one = MyClass4() 
    two = MyClass4() 
    two.a = 2 
    print one.a 
     
    one.b = 3 
    print two.b 
 
    print ('one:',one) 
    print ('two:',two) 
    print 'one id:',id(one) 
    print 'two id:',id(two) 
 
    one.x = 4 
    print one.x 
    print two.x 
    print '------------------------------------------------------------------------------------------' 
