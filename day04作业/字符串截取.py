#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-

str=input("请输入一个字符串:")
while 1:
    for i in str:
        if i == "_" or i >= "a" and i >= "A" or i >= "0" and i <= "9":
            pass
        else:
            jj = 0
            break
    else:
        jj=1
    if len(str)>=20 and jj==1:
        str1 = input("请输入一个字符;")
        if str1 in str:
            list1 = str.split(str1)
        for x in range(0,len(list1)):#还可以用:while ""  in list1:
            if "" in list1:#                          list1.remove("")
                list1.remove("")
        str3 = "".join(list1)
        print(list1)
        list2 = []
        for y in str3:
            if y not in list2:
                list2.append(y)
            else:
                pass
        str4 = "".join(list2)
        print(str4)
        break

    else:
        str=input("请重新输入:")



