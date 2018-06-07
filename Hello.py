#!/usr/bin/env python 
# -*- coding:utf-8 -*-
print ("hello world") #注意到print是一个函数
#这是一个注释
#注释说明细节，注释是一个好东西
#字面常量

age = 20
name = 'Swaroop'
print ('{0} was {1} years old when he wrote this book'.format(name, age))
print ('Why is {0} playing with that python?'.format(name))

print ('''这是一段多行字符串。这是它的第一行。
This is the second line.
"What's your name?," I asked.
He said "Bond, James Bond."
''') #可以在三引号之间自由地使用单引号与双引号

age = 20
name = 'CaoJian'
print ("{0} was {1} years old when he studied python".format(name,age))
#format函数中从 0 开始计数
print ("{} was {} years old when he studied python".format(name,age))
print ("{} was {} years old when he studied python".format(age,name))
#format函数也可以不指定顺序
#format 方法所做的事情便是将每个参数值替换至格式所在的位置

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))
#注意 print 总是会以一个不可见的“新一行”字符（\n）结尾
#重复调用 print将会在相互独立的一行中分别打印
#防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾
print('a', end='')
print('b', end='')
print('/')
#或者你通过 end 指定以空格结尾：
print('a',end=' ')
print('b',end=' ')
print('c')