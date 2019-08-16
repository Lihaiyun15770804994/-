#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
'''写一个双色球彩票系统，系统可以随机产生一组数据，一组彩票数据有六位数，这六位数的的取值范围是0和1。

一张彩票是两块钱，用户可以选择购买彩票的张数，若余额充足，用户可以开始游戏，要求从控制台输入6位的0或者1

若用户输入的不对，要求用户重新输入，直到输入成功为止。若中奖的话，中奖金额为购买彩票金额的50倍，

若没中奖则打印继续努力！用户可以选择继续买票或者是退出。买票和退出的时候要求打印剩余金额。

余额不足的时候提示用户充值。
import  random

print("********游戏开始**********")
print("***********系统开始产生中奖数据*************")
lucyNum = []
while 1:
    n = int(input("请输入需要购买的张数"))
    for i in range(6):
       num = random.choice(["0", "1"])
       lucyNum.append(num)
    print(lucyNum)
    str1="".join(lucyNum)
    money = int(input("一张彩票2元，请充值您的金额："))

    print("您现在的余额为%d元"%money)

    print("温馨提示：中奖数据有六位数，每位数为0或者1")
    for j in range(n):
        while True:
           if money < 2:
              print("很抱歉，您的余额已不足！")
              break
           money -= 2
           while 1:
                numC = input("请输入您猜测的中奖数据")
                for i in numC:
                   if i =="0" or i=="1":
                       pass
                   else:
                       jj=0
                       break
                else:
                    jj=1
                if jj==1:
                   break
                else:
                   print("请重新输入:")
           if numC == str1:
              print("恭喜您中大奖了！")
              money*=50
           else:
              print("很抱歉，没有中奖,继续努力")
        j+=1
        print(j)
        if j==3:
            break

    print("您现在的余额为%d元"%money)
    con = input("请问还要继续么？继续请输入yes, 结束请输入no")
    if con == "no":
      break
      '''
#方法一:也可以行的通
'''import  random

print("********游戏开始**********")
print("***********系统开始产生中奖数据*************")
while 1:
    money = int(input("一张彩票2元，请充值您的金额："))
    n = int(input("请输入需要购买的张数"))
    lucyNum=[]
    for i in range(6):
       num = random.choice(["0", "1"])
       lucyNum.append(num)
    print(lucyNum)
    str1="".join(lucyNum)
    money-=2*n
    if money>=0:
        pass
    else:
        continue
    print("您现在的余额为%d元"%money)
    print("温馨提示：中奖数据有六位数，每位数为0或者1")
    for j in range(n):
           while 1:
                numC = input("请输入您猜测的中奖数据")
                for i in numC:
                   if i =="0" or i=="1":
                       pass
                   else:
                       jj=0
                       break
                else:
                    jj=1
                if jj==1:
                   break
                else:
                   print("请重新输入:")
           if numC == str1:
              print("恭喜您中大奖了！")
              money*=50
           else:
              print("很抱歉，没有中奖,继续努力")
    print("您现在的余额为%d元"%money)
    if money < 2:
        print("很抱歉，您的余额已不足,请充值!")
    con = input("请问还要继续么？继续请输入yes, 结束请输入no")
    if con == "no":
      break
      '''
#方法二:完美方案
import  random
money = int(input("一张彩票2元，请充值您的金额："))
while 1:
    if money<2:
        money = int(input("请充值您的金额："))
    n = int(input("请输入需要购买的张数"))
    str = ""
    for z in range(n):
        for i in range(6):
            num = random.choice(["0", "1"])
            str += num
    print(str)
    list=[]
    list1=[]
    for x in range(n):
        list.append(str[6*x:6*x+6])
    money-=2*n
    if money>=0:
        pass
    else:
        continue
    print("您现在的余额为%d元"%money)
    print("温馨提示：中奖数据有六位数，每位数为0或者1")
    numD=""
    while 1:
        for j in range(n):
            numC = input("请输入您猜测的中奖数据")
            numD+=numC
        for i in numD:
           if i =="0" or i=="1":
               pass
           else:
               jj=0
               break
        else:
            jj=1
        if jj==1:
           break
        else:
           print("请重新输入:")
    for x in range(n):
        list1.append(numD[6*x:6*x+6])
    for y in range(n):
        if list1[y]==list[y]:
            print("恭喜您中大奖了！")
            money*=50
        else:
            print("很抱歉，没有中奖,继续努力")
    print("您现在的余额为%d元"%money)
    if money < 2:
        print("很抱歉，您的余额已不足,请充值!")
    con = input("请问还要继续么？继续请输入yes, 结束请输入no")
    if con == "no":
        break

