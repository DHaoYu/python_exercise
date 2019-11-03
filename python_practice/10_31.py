#模块 和 包
#模块:.py文件   包:是一个文件包
'''
import os
print(id(os), type(os)) #os也是一个对象
#print(os.__doc__) #查看os帮助文档
import sys

sys.path.append(r'd:\...') # 添加包和模块的路径
#print(mymath.calc.add(10, 20))
for path in sys.path:
    print(path)
'''
'''
# 命名空间
import sys, os #可以写到一行中，但是不推荐
import os #写两行，好看些
#按照一定的顺序库进行导入，--->先将py标准库，然后为py第三方库 然后是自定义模块
import sys as s #as后可以跟别名s
op = os #因为模块是个对象，所以可以进行赋值操作 效果和as相同
#        from 可以直接将一个模块的某个函数导入指定名字
from os.path import exists #只从os.path 中导入exists，不需要加任何前缀，可以直接使用
exists('d:/aaa.txt') #可以直接使用
# 耦合：两者之间关联关系程度
'''

#import sys 
#import sys #导入第二遍时，会被忽略 只执行一遍 执行这个过程视为：加载 
#会生成一个__pycache__的文件，会包含导入的模块（二进制）
#python 中有一中操作，先导入一个模块，在程序运行过程中，把模块修改，如果想让修改生效，可以使用relode重新加载

'''
def multi_sum(*args):
    s = 0
    for item in args:
        s += item
    return s

print(multi_sum(1, 2, 3, 4))  # 通常*之后的内容是一个元组

#print(multi_sum(1, 2, 3, '1')) error
a = (1, 2, 'a', 'b')
print(a)
'''
'''
def do_something(name, age, gender = "man", *args, **kwds): #两个**表示传递的是一个字典（实参需要用=之间关联）
    print('name: %s, age: %d, gender: %s' %(name, age, gender))
    print('high: %d, weight: %d' %(args[0], args[1]))
    print(kwds)

do_something('zhangsan', 18, 'man', 180, 60, math=99, english=100)
'''
'''
y = 5
print('y is a -' if y < 0 else 'y is a +') #可以直接在print函数中使用
x = -1 if y < 0 else 1 #可以用于赋值
print(x)

a = [1, 2, 3, 4, 5]
result = [i*i for i in a]
print(result)
'''

a = [1, 2, 3, 4, 5]
b = ['a', 'b', 'c', 'd']
#a[2:2] = b
#print(a)
a[3:] = b
print(a)