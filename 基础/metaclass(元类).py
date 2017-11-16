#!/bin/env python
# -*- coding:utf8 -*- 
class ListMetaclass(type):
    def __new__(cls,name,bases,attrs):
        attrs['add'] = lambda self,value:self.append(value)
        return type.__new__(cls,name,bases,attrs)

class Mylist(list):
    __metaclass__ = ListMetaclass

l = Mylist()
l.add(1)
print l
