#! /usr/bin/env python
# -*- coding: utf-8 -*-
a=[5,7,1,2,3,9,8]
print(a.sort())
# print(a.reverse())
print(len(a))
for i in range(len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            tmp=a[i]
            a[i]=a[i+1]
            a[i+1]=tmp
    print(a)