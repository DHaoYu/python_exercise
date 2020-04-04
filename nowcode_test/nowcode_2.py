#不要二  将欧几里得距离（勾股距离）为2的地方不放蛋糕
'''
x,y=list(map(int, input().split()))
if x % 4 == 0 or  y % 4 == 0:print(int(x*y//2))
elif x % 2 == 0 and y % 2 == 0:print(((x*y)//2+1) + 1)
else:print(x*y//2 + 1)
'''

#把字符串转换成整数
'''
def StrToInt(s):
    try: #进行以下代码
        print(int(s)) 
    except: //如果try中出现异常，则except进行捕获和处理
        print(0)

print(StrToInt(input()))
'''