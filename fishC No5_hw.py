#测试题：

#0. 在 Python 中，int 表示整型，那你还记得 bool、float 和 str 分别表示什么吗？
#bool:布尔类型；float:浮点型；str:字符串

#1. 你知道为什么布尔类型(bool)的 True 和 False 分别用 1 和 0 来代替吗？
#计算机是二进制的原因

#2. 使用 int() 将小数转换为整数，结果是向上取整还是向下取整呢？
#可以说是向下取整，a = 5.99 b = int(a) b = 5  截断取整，便于计算。 

#3. 我们人类思维是习惯于“四舍五入”法，你有什么办法使得 int() 按照“四舍五入”的方式取整吗？
#if a = 5.4 b = 5.6
#a = int(5.4 + 0.5) a = 5
#b = int(5.6 + 0.5) b = 6

#4. 取得一个变量的类型，视频中介绍可以使用 type() 和 isinstance()，你更倾向于使用哪个？
#取得的意思如果是给我一个变量类型，然后让我获得改变量是什么类型的话，我喜欢 type(),但还是建议使用isintance()函数

#5. Python3 可以给变量命名中文名，知道为什么吗？
#Pyhton3 源码文件默认使用utf-8编码  

#6. 【该题针对零基础的鱼油】你觉得这个系列教学有难度吗？
#有一定的难度

##动动手：

#0. 针对视频中小甲鱼提到的小漏洞，再次改进我们的小游戏：当用户输入错误类型的时候，及时提醒用户重新输入，防止程序崩溃。

#如果你尝试过以下做法，请举下小手：
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# 这种想法是因为 type(1) 会返回 <class 'int'>，如果 type(temp) 返回结果一致说明输入是整数。
while type(temp) != type(1):
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")


#或者可能这样：
temp = input("不妨猜一下小甲鱼现在心里想的是哪个数字：")
# not操作符的作用是将布尔类型的结果翻转：即取反的意思，not True == Flase
while not isinstance(temp, int):
    print("抱歉，输入不合法，", end='')
    temp = input("请输入一个整数：")


#以上方法的思路是正确的，不过似乎忽略了一点儿：就是 input() 的返回值始终是字符串，所以 type(temp) 永远是 <class 'str'>！  
    
#其实有蛮多的做法可以实现的，不过就目前我们学习过的内容来看，还不足够。

#所以，在让大家动手完成这道题之前，小甲鱼介绍一点新东西给大家！

#s 为字符串

s.isalnum()  所有字符都是数字或者字母，为真返回 True，否则返回 False。

s.isalpha()   所有字符都是字母，为真返回 True，否则返回 False。

s.isdigit()     所有字符都是数字，为真返回 True，否则返回 False。

s.islower()    所有字符都是小写，为真返回 True，否则返回 False。

s.isupper()   所有字符都是大写，为真返回 True，否则返回 False。

s.istitle()      所有单词都是首字母大写，为真返回 True，否则返回 False。

s.isspace()   所有字符都是空白字符，为真返回 True，否则返回 False。
         
#例如：
>>> s = 'I LOVE FISHC'
>>> s.isupper()
>>> True

#好了，文字教程就到这里，大家赶紧趁热打铁，改造我们的小游戏吧！

import random

times = 3
secret = random.randint(1,10)

print('------------------我爱鱼C工作室------------------')
guess = 0
print("不妨猜一下小甲鱼现在心里想的是哪个数字：", end=" ")

while (guess != secret) and (times > 0):
    temp = input()
    
    if temp.isdigit():
        guess = int(temp)
        if guess == secret:
            print("我草，你是小甲鱼心里的蛔虫吗？！")
            print("哼，猜中了也没有奖励！")
        else:
            if guess > secret:
                print("哥，大了大了~~~")
            else:
                print("嘿，小了，小了~~~")
            if times > 1:
                print("再试一次吧：", end='')
            else:
                print("机会用光咯T_T")
    else:
        print("抱歉，您的输入有误，请输入一个整数：", end='')

    times = times - 1 # 用户每输入一次，可用机会就-1

print("游戏结束，不玩啦^_^")


#1. 写一个程序，判断给定年份是否为闰年。（注意：请使用已学过的 BIF 进行灵活运用）

#这样定义闰年的:能被4整除但不能被100整除,或者能被400整除都是闰年。
temp = input 



#2. 请写下这一节课你学习到的内容：格式不限，回忆并复述是加强记忆的好方式！