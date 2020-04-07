#print(globals())
#print('11_7 :', __name__)

#以下可以作为执行代码，如果把该文件当成main文件，此时，if就可以执行了
#if __name__ == '__main__' :
#    print("test code")
'''
#模块 和 包Package(为一个目录，包含多个模块)
#包就是一个特殊的目录(如my_math)，里面必须包含__init__.py文件（负责对包进行初始化），在当前目录下，
import my_math.calc
print(my_math.calc.add(10, 20))
print(my_math.calc.sub(20, 10))
print(type(my_math))

import sys
print(sys.path) #zip文件，也可以被当成一个包
'''
'''
import sys
print(len(sys.argv)) #argv 命令行参数 len 求列表个数没有算python这个参数
print(sys.executable) #打印python解释器exe路径，一个电脑上可以安装多个版本python

# sys.exit()直接关掉当前解释器
print(sys.getsizeof(200)) #一个整型变量也是一个对象，该整形对象有（id，type，val，等等）
print(sys.getsizeof(1000000000000000000000000000000000000)) #分配更多内存来存储
print(sys.getsizeof('hehehehe'))# 33
print(sys.getsizeof([])) # 36
print(sys.platform) #查看操作系统的平台
print(sys.version) #查看版本
'''
#import sys
#import os 
#os为混杂操作系统接口
#print(os.getenv('PATH'))
'''
ret = os.fork() #os在win平台下，没有fork接口
if ret == 0:
    print('child pid: ', os.getpid())
elif ret > 0:
    print('father pid: ', os.getpid())
    ret = os.wait()
    print('child ret: '+str(ret))
else:
    print('fork error')
'''

#print(os.getloadavg()) #获取系统负载，win也没有


#all and any
x = [True, False, True]
if(any(x)):
    print('at least one True')
if(all(x)):
    print('all is True')
if(any and not all(x)):
    print('at least one true and false')