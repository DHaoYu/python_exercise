#print("America money: ", eval(input("please enter chinese money: "))/6.7)

# print("User says: ", input())

'''
num = input("请输入一个数字：")
l = list(num)
sum = 0
for i in l:
    x = int(i, 10)
    sum += x*x*x
print("各个数字立方和: ", sum)
'''
'''
while True:
    a = float(input("请输入三角形的边a:"))
    b = float(input("请输入三角形的边b:"))
    c = float(input("请输入三角形的边c:"))
    if a+b>c and a+c>b and b+c>a:
        s = (a * b * (1 - ((a ** 2 + b ** 2 - c ** 2) / (2 * a * b)) ** 2) ** 0.5 / 2)
        print("三角形的边分别为:a=", a,", b=", b, " c=", c)
        print("三角形的面积 =", s)
    else:
        print("三角形不合法")
'''
'''
while True:
    try:
        score = eval(input("请输入成绩:"))
    except Exception as e:
        print("again")
        continue
    if 0 <= score < 60:
        print("不及格")
    elif score < 70:
        print("及格")
    elif score < 80:
        print("中等")
    elif score < 90:
        print("良好")
    elif score <= 100:
        print("优秀")
    else:
        print("输入不合法")
'''

'''
while True:
    money = float(input("请输入工资："))
    if money > 144000:
        sum = (money-5000)*0.2-16920
    elif money > 36000:
        sum = (money-5000)*0.1-2520
    elif money > 5000:
        sum = (money-5000)*0.03
    else:
        sum = 0
    print("应交税款为:%f" %sum)
'''
'''
letter = input("请输入字母：")
if letter == 's':
    letter = input("请输入第二个字母：")
    if letter == 'a':
        print ('星期六')
    elif letter  == 'u':
        print ('星期日')
    else:
        print ('输入错误')
elif letter == 'f':
    print ('星期五')
elif letter == 'm':
    print ('星期一') 
elif letter == 't':
    letter = input("请输入第二个字母：")
    if letter  == 'u':
        print ('星期二')
    elif letter  == 'h':
        print ('星期四')
    else:
        print ('输入错误')     
elif letter == 'w':
    print ('星期三')
else:
    print ('输入错误')
'''

'''
str=input("请输入字符串: ")
res = []
for i in str:
    res.append(ord(i))
print("这个字符串的ASCII为: ", res)
'''

#print(len(input("请输入字符串: ").split()))

'''
str = input("请输入一行字符串: ")
alpha = 0
digit = 0
space = 0
others = 0
for c in str:
    if c.isalpha():
        alpha+=1
    elif c.isdigit():
        digit+=1
    elif c.isspace():
        space+=1
    else:
        others+=1
print("英文字母= %d 个,空格= %d 个,数字= %d 个,其他= %d 个"
      %(alpha,space,digit,others))
'''

a_set=[1,2,3,4]
for i in a_set:
    for j in a_set:
        for k in a_set:
            if i != j and i!=k and j!=k:
                print(i,j,k,end=',  ')
    print('\n')
