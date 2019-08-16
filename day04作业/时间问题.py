#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
'''#走了弯路:
time1=input("请输入一个时间:")
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
if mz>=10 and fz<=9 and sz<9:
    jj=1
elif mz>=10 and fz<=9 and sz>=10:
    jj=2
elif mz>=10 and fz>=10 and sz<9:
    jj=3
elif mz>=10 and fz>=10 and sz>=10:
    jj=4
elif mz<9 and fz>=10 and sz<9:
    jj=5
elif mz<9 and fz>=10 and sz>=10:
    jj=6
elif mz<9 and fz<9 and sz>=10:
    jj=7
else:
    jj=8
   # print("[%d:%d:%d]"%(sz,fz,mz))
if jj==8:
    print("[0%d:0%d:0%d]"%(sz,fz,mz))
elif jj==7:
    print("[%d:0%d:0%d]" %(sz,fz,mz))
elif jj==6:
    print("[%d:%d:0%d]" %(sz,fz,mz))
elif jj==5:
    print("[0%d:%d:0%d]" %(sz,fz,mz))
elif jj==4:
    print("[%d:%d:%d]" %(sz,fz,mz))
elif jj==3:
    print("[0%d:%d:%d]" %(sz,fz,mz))
elif jj==2:
    print("[%d:0%d:%d]" %(sz,fz,mz))
else:
    print("[0%s:0%s:%d]" %(sz,fz,mz))
'''
#快速的方法:
time1=input("请输入一个时间:")
if ":" in time1:
    list1 = time1.split(":")
str1="".join(list1)
if "[" in str1:
    list1 = str1.split("[")
str2="".join(list1)
if "]" in str2:
    list1 = str2.split("]")
print(list1)
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






