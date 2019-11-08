#面向对象编程，封装继承多态

#面向过程：类似于编年史 1900年发生什么，1901年发生什么
#面向对象：类似于记传史 某个人这一生是干了什么
# 抽象---具体    类和实例  实例==对象   python对象包含（id，type，val）

#围绕着一个类对应着两种角色（两类人）
#类的实现者       类的使用者
#封装的意思是让类的使用者不需要了解类的实现者是怎样实现的
#封装是为了让使用者使用起来更简单，成本更低
#接口，类的使用者提供给类的使用者去调用的方式
#组合/包含 --has（有）a
#继承 --is（是）
#派生/多态 --是封装的更进一步
#使用者既不需要了解实现者是怎么实现的这个类，同时也不需要实现者实现的这个类是什么类型
#自省/反射 人请自己是个什么类型是谁
'''
#属性和方法
#object 是所有类的父类
class Test:
    "这是一个用来测试类创建语法的类"
    def __init__(self, a = 11, b = 101): #__init__只要实例化，就会调用
        self.x = a #一个类的实例属性(变量)最好放在__init__里面
        self.y = b #
    def Print(self): #self 表示当前这个实例this 
        '实例方法：成员函数/普通函数'
        self.num = 10 #num这个变量就是成员变量（属性）
        print(self.x, self.y)
    

test1 = Test()
test2 = Test()

test1.Print() #等价于 Test.Print(test1)
#Test.Print(test1)
a = list() #list也是一个类
'''
'''
class Test:
    val = 1000 #类属性(静态成员变量)
    def __init__(self, a = 10, b = 100):
        self.x = a
        self.y = b
    def Print(self):
        print('Test.Print')
    
    #装饰器 @ 
    @staticmethod #等价于下面的函数调用也是编程静态方法
    def Func():
        'Python 静态方法 ！= C++/Java静态方法'
        print('in Func') #静态函数不能调用静态成员函数val
    
    @classmethod #变成类方法
    def Func2(cls): #cls表示当前的类，python中类也是一个对象
        '类方法'
        print(cls.val)
    # Func = staticmethod(Func) #将Func设置为静态方法
    

test = Test()
print(Test.val)) #调用类属性（静态成员）
# Test.Func() 
'''
'''
#访问权限 __成员表示私有成员
#有些变成语言用首字母来区分public private，go
# 有些区分使用 __ python 
#组合 将多个类组合成一个
class Student:
    def __init__(self, name, score = 100):
        self.name = name
        self.score = score

class ClassRoom:
    def __init__(self, name=""):
        self.name = name

class SchoolMaster:
    def __init__(self, name="zhangsan"):
        self.name = name

class SchoolName:
    def __init__(self, name="XUFE"):
        self.name = name

class School:
    def __init__(self):
        self.school_master = SchoolMaster('张三')
        self.class_room  = [ClassRoom('101'), ClassRoom('102')]
        self.school_name = SchoolName()
        self.students = [Student('李四', 99), Student('王五')]
'''
'''
class Cat:
    def __init__(self):
        self.head = Head()
        self.feet = []

class EShortCat(Cat):
    def __init__(self):
        self.name = '英短'
        
class AShortCat(Cat):
    def __init__(self):
        self.name = '美短'

class CShortCat(Cat):
    def __init__(self):
        self.name = '中短'

class SDCat(CShortCat):
    def __init__(self):
        self.name = '山东猫'
'''
'''
#当出现同名方法或者属性的时候，子类会覆盖掉父类的方法和属性（不受参数类型或者个数影响）
#__init__ 这个函数也会被覆盖，可以解决这个问题
class Parent:
    def __init__(self):
        self.mes = 'i am father'
    
    def PrintMes(self):
        print(self.mes)

class Child(Parent):
    def __init__(self):
        #Print.__init__() #调用以下父类
        #super.__init__() #同理
        self.mes = 'i am child'
    
    def PrintMes(self): #子类与父类中有同名函数或者属性，则会发生覆盖
        super.__init__()
        print(self.mes)

c = Child()
c.PrintMes()
p = Parent()
p.PrintMes() 
print(c.mes) 
print(p.mes)
'''

