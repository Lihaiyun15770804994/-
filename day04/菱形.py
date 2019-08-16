#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
n=int(input("请输入一个数:"))
if n%2==0:
    for i in range(1,n):
        if i<=n/2:
            for j in range(1, abs(n - i) + 1):
                print(end=" ")
            for k in range(1,2*i):
                print("*",end="")
        else:
            a=n/2
            b=i-a
            i=a-b
            j=1
            while j<abs(n+1-i):
                print(end=" ")
                j+=1
            k=1
            while k<2*i:
                print("*",end="")
                k+=1
        print(" ")
else:
    for i in range(1,n):
        if i<=(n-1)/2:
            for j in range(1, abs(n - i) + 1):
                print(end=" ")
            for k in range(1,2*i):
                print("*",end="")
        else:
            a=(n-1)/2
            b=i-a
            i=a-b+1
            j=1
            while j<abs(n+1-i):
                print(end=" ")
                j+=1
            k=1
            while k<2*i:
                print("*",end="")
                k+=1
        print(" ")