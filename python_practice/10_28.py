#序列 字典
'''
#序列进行值的比较时，是有序的，
a = [1, 2, 3]
b = [1, 2, 1]
print(a == b)
#字典进行值的比较时，是无序的
a = {
    'ip' : '127.0.0.1',
    'port' : 8080
}
b = {
    'port' : 8080,
    'ip' : '127.0.0.1'
}
print(a == b)
'''
'''
#判定某值是否在列表中存在
a = [1, 2, 3, 4]
print(10 in a) #进行遍历比较
a = 'hello world'
print('hello' in a) #按照字符进行比较

a = 'hello'
b = ' world'
print(a + b) #a和b并没有改变，而是创建了新的对象c = a+b

a = [1, 2]
b = [3, 4]
print(a + b)
a.extend(b) #将b拼接到a上,并没有返回对象，只是进行拼接
print(b)
print(a)
'''

a = ['aaa', 'bbb', 'ccc']
#result = ''
#for i in a: #i为a的第一个数据
#    #每次循环都创建了一个result新对象，要进行大量的数据拷贝
#    result += i #直接+=i就可以

result = ''.join(a) #''内部表示拼接的中间的分隔符是什么
print(result)

'''
#序列的切片操作---通过下标进行切片
a = [1, 2, 3, 4, 5, 6]

print(a[0:-1])
print(a[0:])
print(a[::2]) #每隔两个元素切一次 +=
print(a[::-1]) #逆序
print(a[::-2]) #从 最后一个位置进行-=

#求序列长度 len
print(len(a))
print(min(a))

a = 'qewrtret'
b = [1, 2, 3, 4]
print(''.join(sorted(a))) #将序列组合成为一个字符串
print(''.join(str(b))) #将序列组合成为一个字符串
print(sum(b))
'''
'''
a = [1, 2, 3, 4]

def find(input_list, x):
    for i, value in enumerate(input_list): #获取键值对的方式
        if value == x:
            return i
    else:
        return None
'''
'''
a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]
for i in zip(a, b, c): #zip--扣扣子，就是将a中的1与b中的4，可以拉链多个序列
    print(i)
#也可以使用zip来构造字符串
'''
'''
#模块和包
#import 导入整个模块
#from import 导入模块中的指定名字
#print(globals()) #查看全局变量
#包 就是一个特殊的目录，里面必须包含__init__.py 特定文件：负责对包进行初始化
import mymath.calc
print("test.py:", __name__)
print("calc.py:", mymath.calc.__name__)
print(mymath.calc.add(10, 20))
'''
'''
#字符串是不可变对象
#列表是可变对象，元组不可变
a = 'abcd'
# error a[0] = '1' 这样无法修改字符串对象
a = '1' + a[1:]  #只能创建新的空间，将标签a贴到新空间上，然后如果就空间不使用，就会用垃圾回收进行回收
print(a)
'''
'''
#除去列表和字典，其他都是不可变对象
#不可变对象的一个最大的优点：线程安全
a = 10
print(id(a))
a += 1
print(id(a))
'''
'''
#格式化替换
a = 10
s = f'a = {a}'
print(s)
print('a =',a)

a = 'hello\n world'
b = r'hello\n world' #原始字符串，里面的\n不做转义
print(a)
print(b)   
'''
'''
a = 'hello world haha hehe'
print('[', a.center(50), ']') #居中显式
print(a.split(' ')) #切分，按照' '返回一个列表
b = a.split(' ')
print(';'.join(b)) #合并
print(''.join(a)) #合并
'''
'''
a = 'hello'
print('[' + a.center(50) + ']')
print('[' + a.ljust(50) + ']')
print('[' + a.rjust(50) + ']')
#python 中不带'\0' C之后的语言中，都不带'\0'
'''
'''
a = [1, 2, 3, 4]
a.append(5) #追加
a.append([5, 6]) #直接将[5, 6]视为为一个元素
print(a)
a.extend([1, 5, 6]) #将参数中的列表中的元素，依次插入a
del(a[0]) #把对用列表中的元素删掉
del(a) #将标签a删掉
b = [1, 2, 2, 3, 4]
b.remove(2) #按照值删除，将第一个2给删除
print(b)
print(3 in b) #查找3是否在b中

print([1, 2, 3] == [3, 2, 1]) #按照每个值进行比较
print(b.count(3))
'''