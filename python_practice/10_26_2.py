'''
#python
a = 'hehe'
b = a
print(id(a)) # 查看身份标识（）
print(id(b)) # 
'''

'''
# 代码块以及缩进
# python 中很少使用{}，一般进行缩进方式进行规定代码块
result = input("你是否愿意敲代码? 1 or 0")
if result == '1':
    print("11111111111")
    print("11111111111")
    if result == '1':
        print("dddddddd")
elif result == 0:
    print("00000000000")
    print("00000000000")
else:
    print('input error')
'''

'''
num = 1
while num <= 10:
    print(num)
    num += 1

#python中的for循环 类似于C++中的range based for Java中的for-each

for num in range(1, 11):
    print(num)

a = [1, 3, 4, 6]
str = 'donghaoyu'

for num in str:
    print(num)

keyval = {
    'ip':'127.0.0.1' ,
    'port':8080
}

for num in keyval:
    print(num, ':', keyval[num])
'''
'''
for num in range(1, 101):
    if num % 3 == 0 and num % 7 == 0:
        print(num)


a = 101

if a == 10:
    pass
else:
    print('111')
'''
'''
a = [1, 2, 3, 4]
# 列表推导 列表解析
b = [x ** 2 for x in a if x % 2 == 1]
# for num in a:
#     b.append(num ** 2)
#     print(b)
print(b)
'''
'''
# 写函数的规则
def add(x, y):
    ret = x + y
    return ret

# 同名函数会出现相互覆盖的问题，相互覆盖，没有重载的规则
# def add(x, y, z):
#     ret = x + y + z
#     return ret

# def add(x = 0, y = 0):  可以存在默认值，缺省参数

print(add('dong', 'haoyu'))
print(add(1, 2))
print(1, 'haoyu')
'''
'''
# 一个函数可以返回多个值
def get_point():
    x = 10
    y = 10
    return x, y
# 解包 unpack
a, b = get_point()
tmp = get_point() # 返回一个元组tuple
_, b = get_point() # 省去a值
print(a, b)
print(type(tmp))

# 函数也是一个对象
print(type(get_point)) # 函数这个对象的类型为function
'''
'''
f = open('f:/python_code/test1.txt', 'r') #open返回值的是一个文件类型对象

# f.write('hello world')

for line in f:
    print(line, end='')

f.close() # 及时关闭
'''

'''
f = open('f:/python_code/test1.txt', 'r') 

word_dict = {}
for word in f:
    word = word.strip() # str的方法，去掉头部和尾部的空白字符
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
f.close()
print(word_dict)
'''

