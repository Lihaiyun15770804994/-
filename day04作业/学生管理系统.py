#!/usr/bin/python
#-*-:coding:utf-8 -*-
#-*-:author: 李海云-*-
'''
6.写一个学生管理系统
----------------------------------------------------------
|                    欢迎进入学生管理系统                   |
|                                                         |
| 1.学生信息录入      2.学生成绩查询     3.查找学生信息      |
| 4.录入学生成绩      5.课程平均值     6.所有学生信息        |
----------------------------------------------------------

学生信息：
学号：      姓名：      性别：     成绩：     电话'''
def welcome():
    print('''
----------------------------------------------------------
|                    欢迎进入学生管理系统                    |
|                                                         |
| 1.学生信息录入      2.学生成绩查询     3.查找学生信息          |
| 4.录入学生成绩      5.课程平均值     6.所有学生信息
|                  t.退出系统                              |
----------------------------------------------------------
    ''')
    return input("请输入您要操作的选项")


def saveStu(studict):
    stuId = input("请输入您的学号：")
    if stuId in studict:
        print("此学号已存在，请咨询老师...")
        return
    name = input("请输入您的姓名")
    sex = input("请输入您的性别：")
    score = 0
    phonenum = input("请输入你的电话:")
    student = {"stuId":stuId,"name":name,"sex":sex,"score":score,"phonenum":phonenum}
    studict[stuId] = student

def searchStu(stuDDict):
    stuId = input("请输入您的学号：")
    if stuId in stuDDict:
        stu = stuDDict.get(stuId)
        print("学号:%s，姓名:%s,性别:%s,成绩：%d,电话：%s"%(stu["stuId"],stu["name"],stu["sex"],stu["score"],stu["phonenum"]))
    else:
        print("您输入的学号不存在，请查证后查询...")

def searchscore(stuDfict):
    stuId = input("请输入您的学号：")
    if stuId in stuDfict:
        stu = stuDfict.get(stuId)
        for k,v in stu["score"].items():
            print(k,v)
    else:
        print("您输入的学号不存在，请查证后查询...")
def allstu(stuDgct):
    for x in stuDgct:
        print("学号:%s，姓名:%s,性别:%s,成绩：%d,电话：%s" % (stuDgct[x]['stuId'],stuDgct[x]['name'],stuDgct[x]['sex'],stuDgct[x]['score'],stuDgct[x]['phonenum']))
def scoreinput(stuDhct):
    while 1:
        stunum1=input("请输入学生的学号:")
        if stunum1 in stuDhct:
            score1=int(input("请输入你的语文成绩:"))
            score2=int(input("请输入你的数学成绩:"))
            score3=int(input("请输入你的英语成绩:"))
            score4=int(input("请输入你的物理成绩:"))
            score_dict={'语文':score1,'数学':score2,'英语':score3,'物理':score4}
            for y in stuDhct:
                if y==stunum1:
                    stuDhct[y]["score"]=score_dict
            break
        else:
            nn=input("你输入的学号不存在,是否继续输入/yes/no")
            if nn=="yes":
                print("请重新输入")
            else:
                break

def subjictaverage(stuDkct):
    num1=input("请输入你的学号:")
    res=0
    i=0
    for values in stuDkct[num1]['score'].values():
        print(values)
        res+=values
        i+=1
    print("你的课程平均值是%d"%(res/i))

stuDict = {}
while True:
    print(stuDict)
    num = welcome()
    if num == "1":
        print("学生信息录入")
        saveStu(stuDict)

    elif num == "2":
        print("学生成绩查询")
        searchscore(stuDict)
    elif num == "3":
        print("查找学生信息")
        searchStu(stuDict)
    elif num == "6":
        print("所有学生信息是:")
        allstu(stuDict)
    elif num=="4":
        scoreinput(stuDict)
    elif num=="5":
        subjictaverage(stuDict)
    elif num == "t":
        print("退出系统")
        break
    else:
        print("选项有误，请重新输入...")
stuDiict={'1905001': {'stuId': '1905001', 'name': 'jkl', 'sex': 'n', 'score': {'语文': 98, '数学': 98, '英语': 96, '物理': 94}, 'phonenum': '001'}}




