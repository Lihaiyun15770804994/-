#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
x=1
y=1
for x in range(1,35):
    for y in range(1,35):
        if x+y==35 and 2*x+4*y==94:
            print("%d,%d"%(x,y))
        else:
            pass
