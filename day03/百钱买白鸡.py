#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
x=1
y=1
z=1
for x in range(1,21):
    for y in range(1,34):
        for z in range(1,98):
            if x+y+z==100 and 5*x+3*y+z/3==100:
                print("%d,%d,%d"%(x,y,z))
            else:
                pass