# -*- coding: utf-8 -*-
#!/usr/bin/python3
import math
from collections import Iterable
import string
import time
import random
from sys import stdout
from dateutil import parser

# print('%2d-%03d' % (3, 1))  # %2d 2代表占2位字节
# print('%.2f' % 3.1415926)   # %.2f取小数点后2位

# s1 = 72
# s2 = 85
# r = (s2 - s1)*100/s2
# print ('小明成绩提高%.1f%%' % r)
# print r

# classmates=['tom','jack','lily']
# classmates.append('jim')    # 在列表末尾，增加一个名字
# classmates[1]    # 查找list中位置为1的元素，索引从0开始
# classmates.insert(1,'helll')   # 将元素插入指定位置，插入到位置为1的元素位置，原来位置元素向后移
# classmates.pop(1)   # 删除位置为1的元素  pop()默认从末尾开始删除
# classmates[0]='mary'  # 直接替换元素，给位置为0的元素赋值
# print classmates
# print classmates[1]

# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]  # list中可以为list，list元素数据类型可以不同
# print L[0][0],L[1][1],L[2][2]

# high = 1.75
# height = 80.5
# BMI = height/high**2
# print BMI
# if BMI < 18.5:
#     print('过轻')
# elif 18.5 < BMI <25:
#     print('正常')
# elif 25 < BMI <28:
#     print('过重')
# elif 28 < BMI <32:
#     print('肥胖')
# else:
#     print('严重肥胖')
# sum = 0
# for i in range(101):  # for n in ...循环后面加：
#     sum = sum + i
# print sum

# sum = 0
# n = 99
# while n > 0:     # 此处n从小到大开始循环
#     sum = sum + n
#     n = n - 2
# print sum 

# L = ['Bart', 'Lisa', 'Adam']
# for n in L:      # for循环可以针对list循环
#     print n

# n = 0
# while n <= 100:
#     if n > 10:
#         break  # break语句结束当前循环
#     print n
#     n = n + 1
# s = set([1,2,3])  #set只存key，不存value  创建set时，需要传入list作为输入集合
# a = (1,[1,2])
# d = {a:2}   # dict的key为不可变对象，将tuple设为key，报错TypeError: unhashable type: 'list'
# d[a]=(1,2,[1,3])  # 将d的key a赋值(1,2,[1,3])
# s.add((2,3))  # add(key)方法可以添加元素到set中
# s.remove(3)   # remove(key)方法  删除set中元素   d.get('Thomas', -1) key不存在，可以将value赋值 -1 'Thomas' in d两种方法判断key是否存在
# L= [1,1]
# s.add(5)
# print type(s)
# print s
# print d

# n1 = 255
# n2 = 1000
# print (hex(n1),hex(n2))   # hex为内置函数，将数值转换为16进制

# def my_abs(x):  # 参数x代表一个位置，叫位置参数
#     if not isinstance(x,(float,int)):    # isinstance()为内置函数，判断一个对象是否是一个已知类型
#         raise TypeError('bad operand type') 
#     if x < 0:
#         return -x
#     else:
#         return x
# print my_abs('a')

# def quadratic(a, b, c):
#     #int x,y,z,d
#     z = b * b - 4 * a * c
#     d = math.sqrt(z)  # math.sqrt()求平方根函数
#     x = (-b + d)/(2*a)
#     y = (-b - d)/(2*a)
#     return x,y
    
# print quadratic(2,3,1)

# def calc(*numbers):  # *代表可变参数
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print calc(1,2,3)

# def person(name,age,**kw):  # **代表关键字参数
#     return('name:',name,'age:',age,'other:',kw)
# extra = {'city':'beijing','job':'enigeer'}
# print person('jim',23,**extra)

# 命名关键字参数
# def person(name,age,**kw):
#     if 'job' in kw:   # 检查是否有city和job参数
#         pass
#     if 'city' in kw:
#         pass
#         print ('name:',name,'age:',age,'other:',kw)
# person('lily',23,city='beijing',add='chaoyang')  # 调用者仍可以传入不受限制的关键字参数

# 限制关键字参数名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数
# def person(name,age,* job,city):
#     return (name,age,job,city)
# print person('lily',23,job='enigeer',city='beijing')

# def product(*nums):  # *args是可变参数，args接收的是一个tuple，**kw是关键字参数，kw接收的是一个dict
#     sum = 1 
#     for n in nums:
#         sum = sum * n
#     return sum
# product(5)
# product(1,2,3)
# product(1,3,6,7)
# if product(5) != 5:
#     print('测试失败1')
# elif product(1,2,3) != 6:
#     print('测试失败!')
# elif product(1,3,6,7) != 126:
#     print('测试失败!')
# else:
#     try:
#         product()
#         print('测试成功!')
#     except TypeError:
#         print('测试失败!')

# 递归函数 定义：如果一个函数在内部调用本身，叫递归函数
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         n = n * fac(n - 1)
#         return n
# print fac(1000)  # 报错：RuntimeError: maximum recursion depth exceeded  超过最大递归深度 任何递归函数，都存在栈溢出问题

# 切片
# L = ['tom','michael','lily','jim','alice']
# print L[0:3]  # L[:3]如果索引第一个为0还可以省略  取索引 0，1，2
# print L[1:3]  # 取索引1，2
# L = list(range(100))
# print L
# print L[:10]  # 取前10数  索引0-9
# print L[-10:]   # 取后10个数 
# print L[10:20]  # 取前11-20个数  L里面的数指的是索引数字
# print L[::5]  # 每5个取一个
# # tuple和字符串也可以切片，操作结果类型仍然为他们本身的类型
# print 'abcde'[:3]
# print (1,2,3)[:1]

# def trim(s):
#     if s[:1]=='*' and s[-1:]=='*':
#         return s[1:-1]
#     elif s[:1]=='*':
#         return s[1:]
#     elif s[-1:]=='*':
#         return s[:-1]
# print trim('*hello')
# print trim('hello*')
# print trim('*hello*')
# print trim('****hello  world*****')

# 迭代（Iteration） 通过for...in完成
# d = {'a':1,'b':2}
# for k,v in d.items():  # d.items迭代dict中key和values
#     print (k,v)
# for v in d.values():  # d.values迭代dict中values值
#     print v

# print isinstance('abc',Iterable)  # 判断字符串‘ABC’是否可迭代
# Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
# for i,value in enumerate([1,2,3]):
#     print (i,value)

# def findMinAndMax(L):
#     min = max = L[0]  # 将min和max 初始化为L[0]
#     if L ==[]:
#         return (none,none)
#     for n in L:
#         if min > n:  # min初始化为第一个元素，n和min比较
#             min = n   # 将比min小的值n 赋值给min
#         if max < n:
#             max = n
#     return (min,max)
# print findMinAndMax([9,3,4,6,8])
# print findMinAndMax([1,])

# 列表生成式
# print [x * x for x in range(1,11)]   # 写列表生成式时，把要生成的元素x * x放到前面，后面跟for循环，就可以把list创建出来
# print [x * x for x in range(1,11) if x % 2 == 0]  # 加if判断，筛选出偶数的平方
# print [x+y  for x in ('a','b','c') for y in ('a','b','c')]  # 2层循环
# d = {'a':'a','b':'e','c':'w'}   
# print [k+'='+v for k,v in d.items()]  # 此处key 和value类型要一致，不能key:value='a':1

# L1 = ['Hello', 'World', 18, 'Apple', None]
# print [n.lower() for n in L1 if isinstance(n,str)]

# 生成器  Python中，这种一边循环一边计算的机制，称为生成器：generator  使用yeild返回值函数
# L = [x * x for x in range(1,10)]  # 列表[]
# print L
# g = (x * x for x in range(1,10))  # 最外层的[]和() L是一个list，而g是一个generator 
# for n in g:   # for循环可以迭代generator
#     print n

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1    # print位置放到这行下面，结果会有区别
#     return 'done'
# print fib(6)

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     #return 'done'
# for n in fib(6):  # for 循环可以迭代带yield的generator function
#     print n

# 迭代器 iterator
# 可以直接作用于for循环的有list，tuple，dict，set，str   还有generator,包括生成器和带yield的generator function,
# 这些可直接作用于for循环的对象成为可迭代对象：Iterable，可以使用isinstance()判断一个对象是否是Iterable对象：
# print isinstance((),Iterable)  # 判断tuple是否是可迭代
# print isinstance([],Iterable)
# print isinstance('abc',Iterable)
# print isinstance((x for x in range(10)),Iterable)

# 凡是可作用于for循环的对象都是Iterable类型；
# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；
# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。
# Python的for循环本质上就是通过不断调用next()函数实现的

# map/reduce  map()函数接收两个参数，一个是函数，一个是Iterable
# def normalize(name):
#     return name.capitalize()
# print map(normalize,['adam', 'LISA', 'barT'])

# reduce 把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算，其效果就是：
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# def add(x,y):
#     return x * 10 + y
# print reduce(add,[1,2,3,4,5])  
# def char2num(s):
#     digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
#     return digits[s]
# print reduce(add, map(char2num, '13579'))

# # filter()内置函数，用于过滤序列 也接收一个函数和一个序列
# def is_odd(s):
#     return s % 2 == 1
# print list(filter(is_odd,[1,3,2,5,7,3]))

# def not_empty(s):
#     return s and s.strip()   # s.strip()此方法是移除序列为空的字符
# print filter(not_empty,['A', '', 'B', None, 'C', '  '])
# sorted 排序算法，可以接收一个key函数来实现自定义的排序
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# def by_name(n):
#     return n[0].lower()
# print sorted(L, key = by_name)   # 前面是list 后面是key
# def by_score(s):
#     return -s[1]
# print sorted(L, key = by_score)

# 返回函数

# 匿名函数 关键字lambda表示匿名函数，冒号前面的x表示函数参数。匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果
# print list(map(lambda x : x * x,[1,2,3,4]))   # lambda 函数可以直接当函数传入
# print list(filter(lambda n : n % 2 == 1,range(1,20)))  

# dict = {}
# dict['one'] = "This is one"
# dict[2] = "This is two"
# print dict['one']
# print dict[2]
# print dict

# i = 2
# while 1:            # 循环条件为1必定成立
#     print i         # 输出1~10
#     i += 1
#     if i > 10:
#        break     # 当i大于10时跳出循环

# a = 10
# b = 20
# if bin(a) and bin(b):
#     print a and bin(b)
# a = 10
# b = 20
# # print bin(b)
# # print bin(a)
# if b and a:
#     print b and a


# for i in range(1,5):
#     for j in range(1,5):
#         for k in range(1,5):
#             if (i != k) and (j != k) and (i != j):
#                 print i,j,

# for i in range(1,85):
#     if 168 % i == 0:
#         j = 168 / i
#     if i > j and (i + j) % 2 == 0 and (i - j) % 2 == 0:
#         m = (i + j)/2
#         n = (i - j)/2
#         x = n * n - 100
#         print x


# 列表转换为字典
# key = [1,2]
# value = ['a','b']
# print dict([key,value])

# 有2个磁盘文件A,B，各存放一行字母，合并内容存到c
# if __name__ =='__mian__':
# fp = open('test1.txt')
# a = fp.read()
# fp.close()

# fp = open('test2.txt')
# b = fp.read()
# fp.close()

# fp = open('test3.txt','w')
# l = list(a + b)
# # l.sort()
# s = ''
# s = s.join(l)
# fp.write(s)
# fp.close()


# 从键盘输入字符串，小写转换大写，输出到磁盘文件test中
# if __name__ == '__main__':
#     fp = open('test.txt','w')
#     string = raw_input('please input a string:\n')
#     string = string.upper()
#     fp.write(string)
#     fp = open('test.txt','r')
#     print fp.read()
#     fp.close()

# 从键盘输入一些字符，写入文件上，直到#为止

# str1 = raw_input('please input a string:\n')
# str2 = raw_input('please input anothor string:\n')
# ncount = str1.count(str2)
# print ncount

# for i in range(1,10):
#     print 
#     for j in range(1,i+1):
#         print '%d*%d=%d'%(i,j,i*j)
# 字符串日期转换为易读的日期格式

# dt = parser.parse("Aug 28 2015 12:00am""")
# print dt

# n=1
# while n <= 7:
#     a= int(raw_input('input a number:\n'))
#     while a < 1 or a > 50:
#         a = int(raw_input('input a number:\n'))
#     print a * "*"
#     print 2*'*'
#     n += 1


# class student:
#     x = 0
#     c = 0
# def f(stu):
#     stu.x = 20
#     stu.c = 'c'
# a = student()
# a.x = 3
# a.c = 'a'
# f(a)
# print a.x,a.c

# i = int(raw_input('jinglirun'))
# arr = [100000,60000,4000000,2000000,100000,0]
# rat = [0.01,0.015,0.03,0.05,0.075,0.1]
# r = 0
# for idx in range(0,6):
#     if i >arr[idx]:
#         r+=(i-arr[idx]*rat[idx])
#         print(i-arr[idx])*rat[idx]
#         i =arr[idx]
# print r
# l = []
# for i in range(3):
#     x = int(raw_input('integer:\n'))
#     l.append(x)
# l.sort()
# print l
# a = [1,2,3]
# b = a[:]
# print b

# for i in range(1,10):
#     print 
#     for j in range(1,i+1):
#         print "%d*%d = %d"%(i,j,i*j)

# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# time.sleep(1)
# print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
# print time.time()
# print time.localtime(time.time())


# for m in range(100,1000):
#     i = m/100
#     j=m/10 %10
#     k=m%10
#     print i,j,k
#     if m == i**3 + j**3 +k**3:
#         print m


# product_list=[
#     ('Iphone',5800),
#     ('Mac Pro',9800),
#     ('Bike',800),
#     ('Watch',10600),
#     ('Coffee',31),
#     ('Alex Python',120)
#     ]
# shopping_list=[]
# salary =raw_input("Please input your salary:")
# if salary.isdigit(): #判断输入的字符串是否由纯数字组成
#     salary=int(salary) #是纯数字组成转换成int类型
#     while True:
#         for num,item in enumerate(product_list):
#             print(num,item)
#         user_choice = raw_input("Please choice your item:")
#         if user_choice.isdigit():
#             user_choice=int(user_choice)
#             if user_choice < len(product_list) and user_choice >= 0:
#                 p_item = product_list[user_choice]
#                 if p_item[1] <= salary:
#                     shopping_list.append(p_item)
#                     salary -= p_item[1]
#                     print("added %s into shopping car,your current balence is \033[31;1m%s\033[0m" %(p_item,salary))
#                 else:
#                     print("your money is not enough to buy,you have \033[41;1m%s\033[0m left" %(salary))
#             else:
#                 print("your choice %s is out of shopping_list" %(user_choice))
#         elif user_choice == 'q':
#             print("shopping_list".center(50,"*"))
#             for i in shopping_list:
#                 print(i)
#             print("your current balence:",salary)
#             exit()
#         else:
#             print("Invalid option!!")
# else:
#     print("invalid salary!!")



# x = 0
# def grandpa():
#     x = 1
#     def dad():
#         x = 2
#         def son():
#             x = 3
#             print(x)
#         son()
#     dad()
# grandpa()
# print(x)

# print random.uniform(5,10)

# for i in range(5):
#         n = 0
#         if i != 1: n += 1 
#         print i,n
#         if i == 3: n += 1
#         if i == 4: n += 1
#         if i != 4: n += 1
#         if n == 3: print 64 + i

#列表转换成字典
# i = ['1','2','3']
# l = [1,2,3]
# j = [4,5,6]
# print dict([i,l,j])

# fp=open('test1.txt')
# a=fp.read()
# print a
# fp.close()
# fp=open('test2.txt')
# b=fp.read()
# fp.close()

# fp=open('test3.txt','w')
# l=list(a+b)
# print l
# l.sort()
# print l
# s='-'
# s=s.join(l)
# print type(l)
# print type(s)
# fp.write(s)
# fp.close()


# a = raw_input('please input a string:')
# b = a.upper()
# fp = open('test.txt','w')
# fp.write(b)
# fp=open("test.txt")
# print fp.read()
# fp.close()

# fp = open('test4.txt','w')
# a=''
# a = raw_input('please input a string:')
# while a != '#':
#     fp.write(a)
#     stdout.write(a)
#     a = raw_input('')
# print('your input a #:')
# exit()

# filename = raw_input('输入文件名:\n')
# fp = open(filename,"w")
# ch = raw_input('输入字符串:\n')
# while ch != '#':
#     fp.write(ch)
#     stdout.write(ch)
#     ch = raw_input('')
# fp.close()  

# str1=raw_input('please input a string:')
# str2=raw_input('please input a son string:')
# ncount=str1.count(str2)
# print ncount

# dt=parser.parse("Aug 28 2015 12:00AM")
# print dt

# play_it = raw_input("do you want to play it.('Y'or'N')")
# while play_it=='Y':
#     # c=raw_input('input a character:\n')
#     i=random.randint(0,2**32)%100
#     print 'please input number you guess:\n'
#     a=time.time()
#     guess=int(raw_input('input your guess:'))
#     while guess != i:
#         if guess>i:
#             print ('please input a smaller')
#             guess=int(raw_input('input your guess:'))
#         else:
#             print ('please input a bigger:')
#             guess=int(raw_input('input your guess:'))
#     b=time.time()
#     var=b-a
#     print var
#     if var < 15:
#         print 'you are very clever!'
#     elif var < 25:
#         print 'nomal'
#     else:
#         print 'so stupid'
#     print 'congradulations'
#     print 'you guess number is %d'%i
#     play_it=raw_input('continue')

# start = time.time()
# for i in range(1000):
#     print i
# end = time.time()
# print end - start

# testList=[10086,'中国移动',[1,2,4,5]]
# print len(testList)
# print testList[1:]
# testList.append('i am new here!')
# print len(testList)
# print testList[-1]
# print testList.pop(1)
# print len(testList)
# print testList

# a = int(raw_input('输入四个数字：'))
# aa = []
# aa.append(a%10)
# aa.append(a%100/10)
# aa.append(a%1000/100)
# aa.append(a/1000)
# print aa
# for i in range(4):
#     aa[i]+=5
#     aa[i]%=10
# for i in range(2):
#     aa[i],aa[3 - i] = aa[3 - i],aa[i]
#     print aa
# for i in range(3,-1,-1)

# n = 1
# while n<=7:
#     a = input('please input a number:')
#     if a<50 and a>1:
#         print a*'*'
#     else:
#         print 'failed'
#     n+=1
# print 'no inputing'

# class student:
#     x=0
#     c=0
#     def __init__(self,x,c):
#         self.x=x
#         self.c=c
# a=student(3,'a')
# # a.x=3
# # a.c='a'
# print a.x,a.c

# b=input('input a number:\n')
# a=9
# n=1
# while (1):
#     if a%b==0:
#         break
#     else:
#         a=a*10+9
#         n=n+1
# print '%d 个 9 除于 %d 为整数' % (n,b)
# r = a/b
# print r
# a = '。'
# str='bring'
# mylist = ['Brazil', 'Russia', 'India', 'China']
# mylist2 = ['Brazil', 'Russia', 'India', 'China']
# print a.join(str)
# print mylist+mylist2

# sum=4
# s=4
# for j in range(2,9):
#     print sum
#     if j==2:
#         s*=7
#     else:
#         s*=8
#     sum+=s
# print sum

# a = 809
# for i in range(10,100):
#     b = i * a
#     if b >= 1000 and b <= 10000 and 8 * i < 100 and 9 * i >= 100:
#         print b,' = 800 * ', i, ' + 9 * ', i

# i = 0
# j = 1
# x = 0
# while (i < 5) :
#     x = 4 * j
#     for i in range(0,5) :
#         if(x%4 != 0) :
#             break
#         else :
#             i += 1
#         x = (x/4) * 5 +1
#     j += 1
# print x

# str1 = raw_input('input string:\n')
# str2 = raw_input('input string:\n')
# str3 = raw_input('input string:\n')
# print str1,str2,str3
    
# if str1 > str2 :
#     str1,str2 = str2,str1
# if str1 > str3 :
#     str1,str3 = str3,str1
# if str2 > str3 :
#     str2,str3 = str3,str2
 
# print 'after being sorted.'
# print str1,str2,str3

# person = {"li":18,"wang":50,"zhang":20,"sun":22}
# m='li'
# for key in person.keys():
#     if person[m]<person[key]:
#         m=key
# print '%s%d'%(m,person[m])
    
#     if person[m]<person[value]:
#         m=key
# print '%s,%d'%(m,person[value])
# pr=[]
# for i in range(5):
#     a = raw_input('please input a number')
#     pr.append(a)
#     print pr
# pr.reverse()
# print pr

# N=input('please input how people:')
# student=[]
# for i in range(5):
#     student.append(['','',[]])
# def input_stu(stu):
#     for i in range(N):
#         stu[i][0]=raw_input('input student number:\n')
#         stu[i][1]=raw_input('input student name:\n')
#         for j in range(3):
#             stu[i][2].append(int(raw_input('score:\n')))
# def output_stu(stu):
#     for i in range(N):
#         print '%-6s%-10s'%(stu[i][0],stu[i][1])
#         for j in range(3):
#             print '%-8d'% stu[i][2][j]
# input_stu(student)
# print student
# output_stu(student)

# def log(N):
#     return len(N)
# N = raw_input('please input a number:')
# a = log(N)
# print a
# nmax = 50
# n = int(raw_input('请输入总人数:'))
# num = []
# for i in range(n):
#     num.append(i + 1)
 
# i = 0
# k = 0
# m = 0
 
# while m < n - 1:
#     if num[i] != 0 : k += 1
#     if k == 3:
#         num[i] = 0
#         k = 0
#         m += 1
#     i += 1
#     if i == n : i = 0
 
# i = 0
# while num[i] == 0: i += 1
# print num[i]

# n = int(raw_input('整数 n 为:\n'))
# m = int(raw_input('向后移 m 个位置为:\n'))
# num=[]
# for i in range(n):
#     num.append=int(raw_input('please input a number:'))
# print num
# def move(array,n,m):
#     array_end=array[n-1]
#     for i in range(n-1,-1,-1):
#         array[i]=array[i+m]

# def inp(numbers):
#     for i in range(6):
#         numbers.append(int(raw_input('输入一个数字：')))
# def arr_max(array):
#     max=0
#     for i in range(1,len(array)-1):
#         p=i
#         if array[p]>array[max]:
#             max=p
#     k=max
#     array[0],array[k]=array[k],array[0]
# def arr_min(array):
#     min=0
#     for i in range(1,len(array)-1):
#         p=i
#         if array[p]<array[min]:
#             min=p
#     l=min
#     array[5],array[l]=array[l],array[5]
# def outp(numbers):
#     for i in range(len(numbers)):
#         print numbers[i]
# a=[]
# inp(a)
# arr_max(a)
# arr_min(a)
# print 'result：'
# outp(a)

# def inp(numbers):
#     for i in range(6):
#         numbers.append(int(raw_input('输入一个数字:\n')))
# p = 0
 
# def arr_max(array):
#     max = 0
#     for i in range(1,len(array) - 1):
#         p = i
#         if array[p] > array[max] : max = p
#     k = max
#     array[0],array[k] = array[k],array[0]
# def arr_min(array):
#     min = 0
#     for i in range(1,len(array) - 1):
#         p = i
#         if array[p] < array[min] : min = p
#     l = min
#     array[5],array[l] = array[l],array[5]
 
# def outp(numbers):
#     for i  in range(len(numbers)):
#         print numbers[i]
 

# array = []
# inp(array)        # 输入 6 个数字并放入数组
# arr_max(array)    # 获取最大元素并与第一个元素交换
# arr_min(array)    # 获取最小元素并与最后一个元素交换
# print '计算结果：'
# outp(array)

# n1 = int(raw_input('n1 = :\n'))
# n2 = int(raw_input('n2 = :\n'))
# n3 = int(raw_input('n3 = :\n'))
# # def max_min(p1,p2):
# #     return p2,p1
# if n1>n2:
#     n1,n2=n2,n1
# if n1>n3:
#     n1,n3=n3,n1
# if n2>n3:
#     n2,n3=n3,n2
# print n1,n2,n3
# str1 = "this is string example....wow!!!";
# str2 = "exam"
# print len(str1)
# print str1.find(str2)
# print str1.find(str2, 10)
# print str1.find(str2, 40)

# a = 234
# b = ~a
# print 'The a\'s 1 complement is %d' % b
# a = ~a
# print 'The a\'s 2 complement is %d' % a
# max=lambda x,y:(x>y)*x+(x < y) * y
# min=lambda x,y:(x<y)*x+(x>y)*y
# a=10
# b=20
# print max(a,b)
# print min(a,b)

# num = int(raw_input('please input a number:'))
# def sq(num):
#     b = num*num
#     return b
#     if b<50:
#         print 'stop'
#     else:
#         num = int(raw_input('please input a number:'))
#         return b
# again=1
# while again:
#     num = int(raw_input('please input a number:'))
#     print 'reslut:%d'% (sq(num))
#     if sq(num)>50:
#         again=1
#     else:
#         again=0

# t=sq(num)
# print t
# sum=0
# for i in range(101):
#     sum = sum+i
# print sum

# X = [[12,7,3],
#     [4 ,5,6],
#     [7 ,8,9]]
 
# Y = [[5,8,1],
#     [6,7,3],
#     [4,5,9]]
 
# result = [[0,0,0],
#          [0,0,0],
#          [0,0,0]]
# for i in range(len(X)):
#     for j in range(len(X[0])):
#         result[i][j]=X[i][j]+Y[i][j]
# for r in result:
#     print r
# for i in range(3):
#     result = map(lambda a,b:a+b, X[i],Y[i])
#     result.append(result)
# print result

# a = [9,6,5,4,1]
# a.reverse()
# print a
# for i in range(0,10):
#     print(a.pop())
# a = [1,4,6,9,13,16,19,28,40,100,0]
# print '原始列表'
# for i in range(len(a)):
#     print a[i]
# N=int(raw_input('please input a number:'))
# end = a[9]
# if N>end:
#     a[10]=N
# else:
#     for i in range(10):
#         if a[i]>N:
#             temp1=a[i]
#             a[i]=N
#             for j in range(i+1,11):
#                 temp2=a[j]
#                 a[j]=temp1
#                 # temp1=temp2  
#             break
# print 'result:'
# for i in range(11):
#     print a[i]
# sum=0
# a=[]
# for i in range(3):
#     a.append([])
#     print a
#     for j in range(3):
#         a[i].append(int(raw_input('a[0][i]')))
        
# for i in range(3):
#     sum +=a[i][i]
# print sum 

# print '输入10个数字:'
# N=10
# l=[]
# for i in range(10):
#     l.append(int(raw_input('please input a number:')))
# print l
# for i in range(9):
#     min=i
#     for j in range(i+1,10):
#         if l[min]>l[j]:
#             min=j
#     l[i],l[min] = l[min],l[i]
# print '排列之后：'
# for i in range(10):
#     print l[i]

# print '请输入10个数字:\n'
# a=[]
# for n in range(10):
#     a.append(int(raw_input('输入一个数字:\n')))
# a.sort()
# for i in range(10):
#     print a[i]
# print 'result'
# print a

# for  num in range(100):
#     if num>1:
#         for j in range(2,num):
#             if num%j==0:
#                 break
#         else:
#             print num
# def hello_world():
#     return 'hello_world'
# def three_hellos():
#     return 'hello_world'*3
# print hello_world()
# print three_hellos()
# L = ['1','2','3','4','5']
# stri=','
# si=stri.join(L)
# print si
# a = ['one', 'two', 'three']
# for i in a[::-1]:
#     print i
# letter=raw_input('please input:')
# if letter=='M':
#     print 'Monday'
# elif letter=='T':
#     print 'please input the second letter:'
#     letter1=raw_input('please input the second letter:')
#     if letter1=='u':
#         print 'Tuesday'
#     elif letter1=='h':
#         print 'Thursday'
#     else:
#         print 'error input'
# elif letter=='W':
#     print 'Wednesday'
# elif letter=='S':
#     print 'please input the second letter:'
#     letter1=raw_input('please input the second letter:')
#     if letter1=='u':
#         print 'Sunday'
#     elif letter1=='a':
#         print 'Saturday'
#     else:
#         print 'error input'
# elif letter=='F':
#     print 'Firday'
# else:
#     print 'error'
# a=int(raw_input('input 5 number:'))
# ge=a%10
# shi=a%100/10
# bai=a%1000/100
# qian=a%10000/1000
# wan=a/10000
# if ge==wan and shi==qian:
#     print 'huiwenshu'
# else:
#     print 'no huiwens'
# s=raw_input('Pleae enter 5 numbers:>>>')
# list(s)
# li1=[]
# li2=[]
# for i in s:
#     li1.append(i)
#     li2.append(i)
# li2.reverse()
# print(li1,li2)
# if li1== li2:
#     print('Yes')
# else:
#     print('No')
# def age(n):
#     if n == 1:
#         c = 10
#     else: c = age(n - 1) + 2
#     return c
# print age(5)

# def fact(j):
#     sum = 0
#     if j == 0:
#         sum = 1
#     else:
#         sum = j * fact(j - 1)
#         print 'sum%d=%d*%d'%(sum,j,fact(j-1))
#     return sum
 
# print fact(3)
# ji=1
# sum=0
# for i in range(1,21):
#     ji=i*ji
#     sum+=ji
# print sum

# for n in range(1,21):
#     s+=i/j
#     t=i
#     i=i+j
#     j=t
# print s
# i=2.0
# j=1.0
# s=0.0
# for n in range(1,21):
#     s+=i/j
#     i,j=i+j,i
# print s

# x=1
# for i in range(9,0,-1):
#     x2=(x+1)*2
#     x=x2
# print x
# tour = []
# height = []
 
# hei = 100.0 # 起始高度
# tim = 10 # 次数
 
# for i in range(1, tim + 1):
#     # 从第二次开始，落地时的距离应该是反弹高度乘以2（弹到最高点再落下）
#     if i == 1:
#         tour.append(hei)
#     else:
#         tour.append(2*hei) 
#     hei /= 2
#     height.append(hei)
 
# print('总高度：tour = {0}'.format(sum(tour)))
# print('第10次反弹高度：height = {0}'.format(height[-1]))
# N=int(raw_input('please input a number:'))
# Y=int(raw_input('please input a value'))
# s=[]
# b=0
# for i in range(1,N+1):
#     b=b+Y
#     Y=Y*10
#     s.append(b)
#     print b
# s=reduce(lambda x,y:x+y,s)
# print s
s=raw_input('please input a string:')


