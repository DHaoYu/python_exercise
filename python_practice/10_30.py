#文件操作
'''
#f 句柄（遥控器）运用遥控器来操作文件
f = open('d:/test.txt', 'r')
print(type(f))
f.close() #及时关闭 否则会导致文件资源泄露
'''
'''
#with 保证 closei被调用到， with中的as对象称之为 上下文管理器
def func():
    with open('d:/test.txt', 'r') ad f: #open为内建函数
        #做各种文件操作
        pass
    #当with中的语句调用完，就会关闭f下的文件资源
'''
#print(dir(__builtins__)) #查看内建函数
#乱码问题:编码方式不统一
#文件存储有一种编码方式（win默认：gbk,utf8）， 代码读取文件也有一种编码方式（unicode）
'''
with open("d:/test.txt", 'r', encoding='utf8') as f:
    print(f.readlines())  #readlines 以列表方式读，每一个元素都是一行数据
    for line in f:
        print(line)
'''

#help(open)
#文件指针（光标） seek
'''
import os.path
my_path = 'd:/aaa/bbb/ccc.txt'
print(os.path.basename(my_path))
print(os.path.dirname(my_path))
print(os.path.split(my_path)) #元组 前面为路径， 后面为文件
print(os.path.splitext(my_path)) #元组，前面为路径加文件， 后面为文件后缀
'''
'''
import os.path as op
my_path = 'd:/aaa/bbb/ccc.txt'
print(op.exists(my_path)) #判断该文件是否存在（绝对路径）
'''

#文件系统操作,在os模块里
#import os
# os.fork()
'''
my_path = 'F:\python_code'
print(os.listdir(my_path)) #以列表形形式展开
print(os.walk(my_path)) #以列表形形式展开
print(os.rename(my_p))
'''
'''
my_path = 'F:\python_code'
for item in os.walk(my_path):
    print(item) #第一个是当前目录，第二个是当前路径下的子目录，第三个是当前目录下的文件
os.path.join() #可以将路径合并 
'''
#import shutils #更接近于linux命令

#异常处理
'''
prin('hehe') #函数写错了。程序会抛出异常
a = [1, 2, 3]
print(a[100]) #下标越界异常
'''
'''
try:
    a = [1, 2, 3]   
    print(a[100])
    prin(a[1]) #如果被python解释器捕获，就会直接终止程序
except IndexError as e: #e为异常 = IndexError
    print(e)
print('after except') #捕获完异常之后，后面的代码不受影响
'''
'''
try: #一个try语句，可以和多个except 语句相结合
    a = [1, 2, 3]
    prin(a[1]) #nameerror
except IndexError as e:
    print(e)
except NameError as e:
    print(e)
'''
'''
try:
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind()
    sock.listen()
except:
    print()
'''
'''
try:
    a = [1, 2, 3]
    print(a[1]) #nameerror
except IndexError as e:
    print(e)
else: #没有异常的话，就执行 else
    print('没有异常')
print('...') #可以执行到
#except 可以不带任何异常语句，捕获所有可能出现的异常
#finally：无论是否发生异常，这个代码都会执行到
finally:
    print("finally") 
#with 本质上就是try except finally 的综合
'''
'''
def divi(x, y):
    if y == 0:
        raise Exception('div 0')
    return x / y
divi (10, 0)
'''

