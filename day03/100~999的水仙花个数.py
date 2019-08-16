#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
i=0
for     s in range(100,1000):
    a1=s//100
    a2=s//10%10
    a3=s%10
    if  s==pow(a1,3)+pow(a2,3)+pow(a3,3):
            i+=1
            print(s)
    else:
        pass
print(i)

