#coding=utf-8
class people:
    # 定义基本属性
    name = ''
    age = 0
    __weight = 0

    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    def speak(self):
        print("%s speak:I am %d years old"%(self.name,self.age))
p = people('tom',10,20)
p.speak()

class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        people.__init__(self,n,a,w)
        self.grade = g
    def speak(self):
        print("%s say:I am %d years old,i am %d grade"%(self.name,self.age,self.grade))
s = student('tom',10,30,3)
s.speak()

class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("i am %s,i am a speaker,my topic is %s"%(self.name,self.topic))
class sample(speaker,student):
    a = ''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
test = sample("tim",25,80,4,"python")
test.speak()

class Parent:
    def myMethod(self):
        print('use parent method')
class Child(Parent):
    def myMethod(self):
        print ("use son method")
c = Child()
c.myMethod()
# super(Child,c).myMethod()
