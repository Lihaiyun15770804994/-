#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
'''list1 = [1, 2, 3]
list2 = ['hello', 'yes', 'no']
list3 = list1 + list2
print(list3)
list1 = [1, 2, 3]
list2 = list1 * 2
print(list2)
list1 = [1, 2, 3, 'hello', 'yes', 'no']
print(list1[2:4])
list1 = [[1, 2, 3],[2, 3, 4],[5, 4, 9]]
list1 = [1,2,3]
list2 = [3, 4,5,6]
list1.extend(list2)
print(list1)
num = 1
while num <= 100:
    if num % 2 == 0:
        continue
    print(num)
    num+=1
list1 = [1, 2, 3]
a=list1.index(3)
print(a)
n=int(input(""))
list=n
a=list[1]
print(a)
list=input()
list.sort()
print(list)




list1=[]
list2=input()
for i in list2:
    list1.append(i)
print(list1)
赋值来求:for i in range(1,6):

    for j in range(1,abs(3-i)+1):
        print( end="    ")
    if i<=3:
        for k in range(1,2*i):
            print("*",end="\t")
    else:
        i=abs(3-i)
        for k in range(1,-2*i+6):
            print("*",end="\t")
    print(" ")

#练习2
#str=input("请输入一个字符串:")
n=len(str)
for r in str:
    if r=='_' or r>='a' and r<='z' or r>='A' and r<='Z':
        if a<=20:






元组来求:
tuple=("  *  "," *** ","*****"," *** ","  *  ")
for i in tuple:
    print(i)'''


'''tuple=("  *  "," *** ","*****"," *** ","  *  ")
print(tuple)

#赋值来求


for i in range(1,6):

    for j in range(1,abs(3-i)+1):
        print( end="    ")
    if i<=3:
        for k in range(1,2*i):
            print("*",end="\t")
    else:
        i=abs(3-i)
        for k in range(1,-2*i+6):
            print("*",end="\t")
    print(" ")
#for i in range(1,6):

    for j in range(1,abs(3-i)+1):
        print(end=" ")
    if i<=3:
        for k in range(1,2*i):
            print("*",end="")
    else:
        i=abs(3-i)
        for k in range(1,-2*i+6):
            print("*",end="")
    print(" ")
st=input("请输入一个字符串:")
a=len(st)
str1=""
#自己的办法:for x in range(a-1,-1,-1):
    print(st[x],end="")
#老师的办法:
stra=""
for x in range(1,a):
    stra+=str1[-x]
print(stra)
还有一种:
for x in range(a-1,-1,-1):
    stra+=str1
print("stra")
''''''

str1="jfshfa"
print(str1)
str="fjkdshkjahkj"
print(str.rsplit("a"))
'''
'''list1=[1,2,3,1,2,1,2,3,"hah","good","True","False","True","None"]
list2=[1,2,3,1,2,1,2,3,"hah","good","True","False","True","None"]
a=len(list1)

for x in range(0,a):
    for y in range(0,a):
        list1[x]==list2[y]
        list1=del list1[y]
print(list1)'''
'''time1=input("请输入一个时间:")
if ":" in time1:
    list1 = time1.split(":")
str1="".join(list1)
if "[" in str1:
    list1 = str1.split("[")
str2="".join(list1)
if "]" in str2:
    list1 = str2.split("]")
str3="".join(list1)
sz=int(str3[0])*10+int(str3[1])
fz=int(str3[2])*10+int(str3[3])
mz=int(str3[4])*10+int(str3[5])
if mz+1==60:
    mz=0
    fz+=1
    if fz == 60:
        fz = 0
        sz += 1
        if sz ==24:
            sz = 0
else:
    mz+=1
print("[0%d:0%d:0%d]"%(sz,fz,mz))'''

'''time1=input("请输入一个时间:")
if ":" in time1:
    list1 = time1.split(":")
str1="".join(list1)
if "[" in str1:
    list1 = str1.split("[")
str2="".join(list1)
if "]" in str2:
    list1 = str2.split("]")
str3="".join(list1)
sz=int(str3[0])*10+int(str3[1])
fz=int(str3[2])*10+int(str3[3])
mz=int(str3[4])*10+int(str3[5])
if mz+1==60:
    mz=0
    fz+=1
    if fz == 60:
        fz = 0
        sz += 1
        if sz ==24:
            sz = 0
else:
    mz+=1
print(("[%02d:%02d:%02d]" %(sz,fz,mz)))
'''
#对字符串进行平均截取:
'''str1="dasdjahjahdhj21212"
print(str1)
list=[]
print(str1[0:6])
for i in range(0,3):
    list.append(str1[6*i:6*i+6])
print(list)'''
'''
import  random

print("********游戏开始**********")
print("***********系统开始产生中奖数据*************")
lucyNum = []
while 1:
    money = int(input("一张彩票2元，请充值您的金额："))
    n = int(input("请输入需要购买的张数"))
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
'''
list=[]
print("请输入你的信息按学号,姓名,性别输入")
for i in range(3):
    str=input("请输入你的学生信息:")
    list.insert(i,str)
print(list)
list1=[]
list1.append(list)
print(list1)
list.insert'''
'''
list1=["hello","good","haha"]
x=0
while x <len(list1):
    print("%d %s"%(x,list1[x]))
    x+=1
    '''
'''import turtle
for i in range(5):
    turtle.forward(100)
    turtle.right(144)
turtle.fillcolor("red")
turtle.done()
'''
'''import  turtle
turtle.begin_fill()
turtle.fillcolor("red")
for i in range(4):
    turtle.forward(100)
    turtle.right(90)
turtle.end_fill()
turtle.done()
#元组的创建
'''
'''t1=()
t2=12,34
t3=(34,45)
T4=(1,)
#若元组中只有一个元素,后面加上一个逗号,消除歧义.

元组的访问
元组名[index]
index

'''
'''tuple=("  *  "," *** ","*****"," *** ","  *  ")
for x in tuple:
    print(x)'''

'''
import  turtle
turtle.begin_fill()
turtle.fillcolor("red")
turtle.up()
turtle.goto(-200,200)
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(200)
turtle.end_fill()
turtle.goto(-190,160)
turtle.right(90)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(40)
    turtle.right(144)
turtle.end_fill()
turtle.goto(-160,180)
turtle.left(36)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.right(15)
turtle.end_fill()
turtle.goto(-140,160)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
turtle.goto(-135,135)
turtle.right(21)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
turtle.goto(-160,110)
turtle.left(36)
turtle.fillcolor("yellow")
turtle.begin_fill()
for i in range(5):
    turtle.forward(20)
    turtle.right(144)
turtle.end_fill()
turtle.done()
'''
'''
x=0
list=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                list.append(i*100+j*10+k)
                print("%d%d%d"%(i,j,k))
                x+=1
print(list)
print(x)
'''
'''str1=input("请输入一行字符:")
x=0
y=0
z=0
k=0
for i in str1:
    str2="abc"+i
    a=str2.isalpha()
    if a==True:
        x+=1
    elif i==" ":
        y+=1
    elif i>="0" and i<="9":
        k+=1
    else:
        z+=1
print("%d,%d,%d,%d"%(x,y,z,k))
'''
'''li = ["hello",'seven',["mon",["h","kelly"],'all'],123,446]
print(li[2][1][1])
li[2][2]="ALL"
print(li)
'''
'''I=int(input("请输入你当月的利润:"))
if I <=10:
    x=I*0.1
elif I<20:
    x=10*0.1+(I-10)*0.075
elif I<40:
    x=10*0.1+10*0.75+(I-20)*0.05
elif I<60:
    x=10*0.1+10*0.75+20*0.05+(I-40)*0.03
elif I<100:
    x = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03+(I-60)*0.015
else:
    x = 10 * 0.1 + 10 * 0.075 + 20 * 0.05 + 20 * 0.03+40*0.015+(I-100)*0.01
print(x)

'''
'''import random
qujian=input("请输入数字区间例如[2:6]:")
List=qujian.strip()[1:-1].split(":")
num1=int(List[0])
num2=int(List[1])
num=random.randint(num1,num2)
print(num)
i=0
while 1:
    print("你们要猜的数字在%d到%d之间"%(num1,num2))
    numc=int(input("玩家请输入猜的数:"))
    i+=1
    if numc==num:
        print("恭喜你,猜中了")
        break
    elif numc>num:
        print("你猜的高了")
        num2=numc
    else:
        num1=numc
        print("你猜的低了")
print(i)
'''
'''d1={1:2,2:3,3:4}
d2={2:3,3:4,4:5}
d2.update(d1)
print(d2)
print([x*x for x in range(1,101)])
'''
'''def jiechen (n):
   res=1
   sum=0
   for x in range(1,n+1):
      res*=x
      sum+=res
   return sum
sum=jiechen(5)
print(sum)
'''
'''
def qiuhe():
   sum=0
   for x in range(1,n+1):
      sum+=x
   return sum
def jiechen(n):
   re=1
   for y in range(1,n+1):
      re*=y
   return re
'''
'''import time

'''''''
geci_dict={}
geci2_dict={}
li=musiclrc.splitlines()
li.remove("")
timelist=[]
print(li)
for x in li:
   gecilist=x.split("]")#遍历歌词列表
   geci=gecilist[-1]#提取歌词信息
   shijian=gecilist[:-1]#提取时间信息列表
   for y in shijian:
      shijian_str=y[1:]#去除"["
      shijianlist=shijian_str.split(":")#按冒号切片
      fen=int(shijianlist[0])
      miao1=float(shijianlist[1])
      miao2=int(miao1)
      timee=fen*60+miao2
      timelist.append(timee)
      geci_dict[timee]=geci
timelist.sort()
for sj in timelist:
   value=geci_dict[sj]
   geci2_dict[sj]=value
print(geci2_dict)
i=0
for key in geci2_dict:
   if i==0:
      time.sleep(timelist[i])
      print(geci2_dict[key])
   else:
      time.sleep(timelist[i]-timelist[i-1])
      print(geci2_dict[key])
   i+=1


'''
# def outAge(func):
#     def inner(age):
#         if age>160 or age<0:
#             print("见鬼了")
#         else:
#             func()
#     return inner
#
# @outAge
# def getAge(age):
#     print('我今年%d岁了'%age)
# getAge(180)
# def panduan(str1):
#     if len(str1)>=5:
#         return True
#     else:
#         return False
#
# print(panduan("ahdajhfja"))
# def gcd(m,n):
#     x=abs(m)
#     y=abs(n)
#     if x<y:
#         x,y=y,x
#     while x%y!=0:
#         r=x%y
#         x=y
#         y=r
#     print(y)
#     return y
# # gcd(5,12)
# # def hanshu(obj):
# #     for i in obj:
# #         if i=="" or i==" ":
# #             return  True
# #     return False
# # print(hanshu('dhajdha'))
# def gbs(m,n):
#     print(m*n/gcd(m,n))
# gbs(18,8)

# def logger(func):
# 	def inner(*args,**kwargs):
# 		print("***********")
# 		return func()
# 	return inner
#
# @logger
# def myPrint():
# 	print("you are very good")
#
# myPrint()
import functools
import operator
# def int2(str, base=2):
# 	return int(str, base)
# print(int2("10")
# def getyuebei(m,n):
# 	ji=m*n
# 	r=None
# 	while m%n!=0:
# 		r=m%n
# 		m=n
# 		n=r
# 	print(n)
# 	return n
# getyuebei(8,12)
add2=functools.partial(operator.add,100)
print(add2(20))

