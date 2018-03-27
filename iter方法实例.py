#! /usr/bin/env python
# -*- coding: utf-8 -*-
class fib(object):
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b = self.b,self.a+self.b
        return self.a

    def __getitem__(self, item):
        if isinstance(item,int):
            a,b=1,1
            for i in range(item):
                a,b=b,a+b
            return a

        if isinstance(item,slice):
            start=item.start
            stop=item.stop
            if start is None:
                star = 0
            a,b=1,1
            l=[]
            for i in range(stop):
                a,b=b,a+b
                if i >= start:
                    l.append(a)
            return l

print(fib()[1:5])
print(fib()[5])
for i in fib():
    print(i)
    if i >100:
        break