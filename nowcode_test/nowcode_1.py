#在一个字符串中找出最长的数字串，
#abcd12345ed125ss123058789 --->123058789,9
#def Solution(str):
#str = Solution(input())
import re
#print(max(re.findall(r"\d*", input()), key=len))
#print(re.findall(r"\d*", input()))
'''
arr = re.split(r'\D*', input())


print(str(arr))

print(max(arr, key=len))
#print(max(input().split(r'\D*'), key=len))
'''
#//计算糖果 A-B A+B B-C B+C已知，求ABC
'''
a, b, c, d = list(map(int,input().split()))
print((a+c)/2,(b+d)/2,(d-b)/2) if c-a == b+d else print('No')
'''

#十进制转换位n进制问题，输入十进制m和进制n，进行转换 7 2--> 111
#print(int('18', 16)) 将16进制的数转化为10进制的数
#print(int('10', 8)) #将8进制的数转化为10进制的数
'''
table = 'ABCDEF'
s = ''
m, n = map(int, input().split())
while m:
    if m < 0:
        m = -m
        print('-', end='')
    m, f = divmod(m, n)
    if f > 9:
     
        f = table[f-10]
    s += str(f)
print(s[::-1])
'''

#a, b = map(int,input().split())
#a = int(input())
#b = int(input())
#print(a + b)

#i like beijing.  ---> bejing. like i
print(' '.join(input().split()[::-1]))