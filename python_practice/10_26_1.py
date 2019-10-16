'''
#float 相当于python中的double
#python 2 中不能用中文注释,需要加上 coding:utf-8
num = 10
pi = 3.14
#python 为动态类型编程语言,运行过程中，类型可以发生变化
name = "董皓宇"
name = 100

count = num + 1
'''
'''
num = 1000000000000000000000*1000000000000000000000000*10000000000000000000;
print(type(num)); #type为查看类型变量的函数
#python中int可以是无穷大
print(num);
'''


#字符串
#name = "donghaoyu"
#name2 = 'my name is "donghaoyu"'
#name3 = '""""'''"'"
#字符串前面加上r 表示原始字符串（raw_string）

#print(name2[1])#下标也是从0开始的
#print(name2[-1])#负数下标是从后往前，-1 等价于 len -1 
#print(name2[100])#会发生越界
#print(name2[1:4])#取字符串字串，1:4表示前闭后开的区间[1,4)，就是取下标123三个字符 y n
#切片操作(slice)

'''
a = "hello"
b = "world"
print(a+b);#字符串加法，拼接
print(a*3)#打印3倍的字符串a

#格式化字符串
num = 10
print('num = {}'.format(num))
s = f'num = {num}'
print(s)
'''

'''
#python 中只有字符串类型，没有字符类型
name = "hehe"
print(len(name)) #求长度
print(type(name[0]))

#bool 类型 
value = True
print(type(value))
print(value + 1)# True为1，False 为0，可以进行运算
'''

'''
#输入输出
#动态强类型的编程语言
#隐式类型转换越支持，类型越弱，反之越强
#s = input('please enter# ')#返回值类型为str类型
#print("s:", s)

num = input('please enter# ')
#print('num + 1:', num + 1) error
print('num + 1:', int(num) + 1)
'''
'''
a = 1 
b = 2
print(a / b) # 0.5
print(a // b) # 0

num1 = 100
num2 = 100

print(num1**num2) #100的100次方
#C++中，大数据运算中--->转换为字符串
#Java中，有现成的类，可以帮助处理
'''

'''
a = 1 
b = 2
c = 3
print(a < b < c)#python 中可以进行连续判断
print(b < c < a)
#and 表示逻辑与 or表示逻辑或 not表示逻辑非
#同样支持短路求值：在进行逻辑运算是，当第一个运算已经确定了整个式子结果，则不会在向下接着进行逻辑运算
#短路求值（Short-circuit evaluation，又称最小化求值），
#是一种逻辑运算符的求值策略。只有当第一个运算数的值无法确定逻辑运算的结果时，
#才对第二个运算数进行求值。例如，当AND的第一个运算数的值为false时，其结果必定为false；
#当OR的第一个运算数为true时，最后结果必定为true，
#在这种情况下，就不需要知道第二个运算数的具体值
print(a < b and b > c)
print ('haha' + 'hehe')
#字符串比较大小，按照字典序进行比较
'''

'''
#没有++ -- 的操作
num = 10
print(--num)
print(++num)

num += 1 #逐增操作
'''

'''
#list
a = [9, 6, 2, 7] #列表
#访问方式
print(a[-1])
a[0] = 100 #可以进行修改
arr = [9, 'hehe', 3, True， [2, 3, 4]] # 可以放置不同类型
print(arr)

# 元组(tuple)
a1 = (9, 6, 'hehe', 7)
a1[0] = 100 #error

# 列表是可变对象，
# 元组不可变对象

a = 10 #不可变对象
a = 20 #重新创建一个20将a于其关联起来

s = 'hehe'
a[0] = 'z' #也不可变
print(a)

#字典
a = {#键值对,大括号里面需要加','进行分隔
    'ip':'127.0.0.1', # 环回 ip 主要用于测试
    'port': 8080
}
print(a['ip'])
#json 出自于JavaScript 表示对象
'''







