#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
#方法一:
'''str1=input("请输入一个字符串:")
str2=""
for i in range(len(str1)-1,-1,-1):
    str2+=str1[i]
print(str2)'''
#方法二:
'''str1=input("请输入一个字符串:")
list=[]
for i in range(len(str1)-1,-1,-1):
    list.append(str1[i])
    str2="".join(list)
print(str2)'''
#方法三:
'''str1=input("请输入一个字符串:")
list=[]
for i in range(1,len(str1)+1):
    list.append(str1[-i])
    str2="".join(list)
print(str2)'''
#方法四:
'''str1=input("请输入一个字符串:")
for i in range(len(str1)-1,-1,-1):
    print(str1[i],end="")

'''
#方法五:
'''str1=input("请输入一个字符串:")
str2=""
for i in range(1,len(str1)):
    str2+=str1[-i]
print(str2)'''
#:方法六:
str1=input("请输入一个字符串:")
print(str1[::-1])


