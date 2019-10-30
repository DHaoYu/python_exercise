'''
a = [9, 23, 2, 10]
print(a.sort()) #sort函数没有返回值
print(a) 
print(sorted(a))
'''
'''
#实现栈
a = []
a.append(4)
print(a)
a.pop() #出栈
print(a)
a.pop(0) #出队列
'''
'''
#深浅拷贝问题
import copy
#元组不能进行深拷贝
#因为元组不能进行修改
a = [1, 2, 3]
b = a #浅拷贝
b = copy.deepcopy(a) #深拷贝
print(id(a), id(b))
'''
'''
a = (1, 2, 3)
a = a = (4,) #加上,表示()不是运算符优先级
print(a)

#元组不可变：如果元组内部包含着可变对象，该可变对象是可以修改的，元组的id是不可变的
b = ([1, 2], [3, 4])
print(a[0])
b[0][0] = 100
print(b[0])
#元组的好处：避免不知情下的修改
#字典的键key也是不可变的对象

#list 不能够hash、字典 因为list是可变对象
a = ()
b = {
    a: 10
    }
'''
'''
#字典创建
a = {}
a = dict(([1, 2], [3, 4]))
print(a)

#插入
b = {
    'ip' : '127.0.0.1',
    'port' : 8080
}
#key是不可修改的
b['proto'] = 'tcp' #存在就是查找，不错在就是插入

for key in b:
    print(key, b[key])

#删除
del(b['proto']) 
#查找
print(b['port']) #存在直接打印val  不存在的话，给用户抛异常
'''
#字典中的内置函数
'''
a = {
    'ip' : '127.0.0.1',
    'port' : 8080
}

print(len(a))
print(a.keys()) #返回所有的key
print(a.values()) #返回所有的value
print(a.items()) #返回一个整理好的元组
'''

#集合
'''
a = set([1, 2, 3])
b = set([3, 2, 1])
c = set([1, 2, 2, 3])
print(a)
print(c) #集合中的元素不能重复，会进行去重
print(a == b)
'''
'''
a = set([1, 2, 3])
b = set([3, 4, 5, 6])
print(a & b) #求交集
print(a | b) #求并集
print(a - b) #求差集
print(a ^ b) #求对称差集（）

#数据去重
a = [1, 2, 2, 3, 3, 5]
b = list(set(a)) #通过集合去重，转换为列表
print(b) 
'''
