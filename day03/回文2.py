#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
i=0
for s in range(10000,100000):
    m=s
    y=0 #要对y进行重新赋值,不然y会继承.
    while   s>0:
        y=y*10+s%10
        s//=10
    if  y==m:
        i+=1
        print(y)
    else:
        pass
print(i)
