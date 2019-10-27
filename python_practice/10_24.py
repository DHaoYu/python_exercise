'''
def add(x, y):
    return x + y

print(id(add))
print(type(add))
'''

'''
#python 中都是变量名字都是标签，目的：节省空间，节省时间（减少深拷贝），也是python中GC机制
#c++由于垃圾回收机制，所以没这么设计
#与 java中的引用比较相似，但是与c++中差别
a = 1
print(id(a))
b = 2
print(id(b))
#在b = 1时，是将b这个标签贴到 1 这个空间上
b = 1
print(id(b))
#在将a = 2，发现a用了b之前 2 的空间
a = 2
print(id(a))
'''
#python中是动态强类型 C语言是静态弱类型 Java是静态强类型 
#动态类型：一个变量在程序运行过程中类型发生改变
#静态类型：一个变量在程序运行过程中类型不能发生改变
#强类型：越不支持隐式类型转换，类型越强
#弱类型：越支持隐式类型转换，类型越弱

#强类型好：不会出现两个不同类型的运算之间的错误
'''
a = 1
b = 1.1
print(a + b)

a = 1
b = type(a)
print(b)
print(type(b)) #type 返回的是一个对象，这个对象的类型是type

#表示一个无意义的值
n = None

def func():
    print(10)

a = func()
print(a)#a = None
'''
'''
if None:#表示为False
    print('haha')
else:
    print('hehe')

#列表[] 元组()  字典{}
if (0, 0):
    print('haha')
else:
    print('hehe')
'''

'''
#比较值：比较对象内部值
a = [1, 2, 3, 4]
b = [1, 2, 3, 4]


if a == b:
    print('hehe')
else:
    print('haha')

#比较身份:比较对象id，id与地址是不同的
if id(a) == id(b):
    print('same')
else:
    print('not')

if a is b: #与上述相同 is、is not
    print('same')
else:
    print('not')
#比较类型
num = 100
print(type(num) == type(100))
'''
#类型工厂函数，可以通过int() float() str() 进行强转
#设计模式：为自己的的编程语言填坑

#a, b = 1, 2
#c = 1
#print(id(a), id(b), id(c))
'''
a = [1, 2, 3]
b = list(a)
print(a, b)

num = 3
print(~num)

a, b = divmod(10, 3)
print(a, b)
'''

