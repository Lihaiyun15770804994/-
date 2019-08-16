#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
# str1=input("请输入一个字符串:")
# list2=list(str1)
# def sort(list1):
#     for i in range(0,len(list1)-1):
#         for j in range(0,len(list1)-1-i):
#             if list1[j]>list1[j+1]:
#                 list1[j],list1[j+1]=list1[j+1],list1[j]
#             else:
#                 pass
#     return list1
# print(sort(list2))



def mymax(*args):
    if len(args)>0:
        maxnum=args[0]
        for x in args:
            if x>maxnum:
                maxnum=x
    return maxnum
print(mymax(1,3))

