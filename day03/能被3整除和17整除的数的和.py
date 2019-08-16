#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
num=1
sum=0
while   num<=100:
    if  num%3==0  or  num%17==0:
        sum=sum+num
        num=num+1
    else:
        num=num+1
print(sum)


