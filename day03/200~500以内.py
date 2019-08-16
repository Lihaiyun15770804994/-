#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
i=0
for s   in range(200,500):
    if  s%2==0  and s%7!=0:
        i+=1
print(i)