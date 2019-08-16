#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
#用while循环倒着九九乘i=9
'''
while i>0:
    k=8
    while k>i-1:
        print(end="        ")
        k-=1
    j=i
    while j>0:
        z=i*j
        print("%d*%d=%d" % (j, i, z), end="\t")
        j-=1
    print(" ")
    i-=1
    #用for循环倒着九九乘法表
for i in range(9,0,-1):
    for k in range(8,i-1,-1):
        print(end="        ")
    for j in range(i,0,-1):
        z=i*j
        print("%d*%d=%d"%(j,i,z),end="\t")
    print(" ")
#正着:for:
for i in range(1,9+1):
    for j in range(1,i+1):
        z=i*j
        print("%dx%d=%d"%(j,i,z),end="\t ")
    print(" ")
#while:
i = 1
while i <= 9:
    j = 1
    while j <= i:
        sum = j*i
        print("%dx%d=%d"%(j,i,sum),end="    ")
        j += 1
    print("")
    i += 1