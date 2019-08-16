#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
i=0
for s in range(10000,100000):
    a1=s//10000
    a2=s//1000%10
    a4=s//10%10
    a5=s%10
    if a1==a5 and a2==a4:
        i+=1
        print(s)
    else:
        pass
print(i)



