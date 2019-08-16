#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
money=int(input("请投入金额:"))
z=money
import random
while 1:
    if z>=5:
        z-=5
        print("开始游戏")
        a=random.randrange(0,2)
        if a==1:
            print("恭喜你中奖了")
            mon=random.randrange(1,10)
            print("你中奖的金额是%d"%mon)
            z+=mon
        else:
            print("很遗憾,未中")
        print("你当前的金额是%d"%z)
        str=input("是否继续:")
        if str=="是":
            pass
        else:
            break
    else:
        jj=input("余额不足是否继续充值:")
        if jj=="是":
            z+=int(input("请输入充值的金额:"))
        else:
            break



