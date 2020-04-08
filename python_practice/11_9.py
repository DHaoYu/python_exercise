#类和对象
'''
#继承
class Parent:
    def __init__(self):
        self.pmsg = 'i am father'
    
    def PrintMeg(self):
        print(self.msg)

class Child(Parent):
    def __init__(self): #会发生覆盖
        #Parent.__init__(self) #解决方法，在此处显式调用以下父类的初始化函数
        super().__init__() #获取父类对象
        self.cmsg = 'i am child'

c = Child()
print(c.cmsg)
print(c.pmsg) #__init__ 子类把父类中的初始化函数覆盖了，所以无法在继承父类中的pmsg
'''
'''
#多态 py中多态和继承没有关系
#从函数实现者角度看，实现者并不知道x y是什么类型，但是只要支持相加操作，都可以相加
#就是python中的多态   ---也就是C++中的静态多态(模板T类型)

#python中的鸭子类型的多态
def add(x, y):
    return x + y

print(add(1, 2))
print(add('hello', 'world'))
print(add([1, 2, 3], [4, 5, 6]))
'''
'''
#类中内建函数
#hasattr 
class C:
    val = 100

#print(getattr(C, 'val')) #获得属性/方法
delattr(C, 'val') #删除属性/方法
#print(C.val)
#print(dir(C))
#super 获取父类

class Time:
    def __init__(self, hour, min):
        self.hour = hour
        self.min = min

    def __str__(self):
        return f"{self.hour}:{self.min}"
    def __len__(self):
        return len(f"{self.hour}:{self.min}")
t = Time(15, 20)
print(t) #打印除了对象的属性信息
print(len(t))
'''