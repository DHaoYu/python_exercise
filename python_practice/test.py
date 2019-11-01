'''
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0,20,100)   # 创建一个列表
plt.plot(x,np.sin(x))       # 对于每个点的sin值绘图
plt.show()                  # 显示
'''
'''
import qrcode

img = qrcode.make('./code.png')
img.show()
img.save("qr.png")
'''
'''
import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('https://github.com/DHaoYu')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.show();
'''

n = int(input())
 
pre = list(map(int,input().strip().split()))
ino = list(map(int,input().strip().split()))
 
 
def gen(pre, ino):
     
    if len(pre)<=1:
        return pre
     
    a = pre[0]
    idx = ino.index(a)
     
    left = gen(pre[1:idx+1], ino[:idx])
    right = gen(pre[idx+1:], ino[idx+1:])
     
    return left+right+[a]
 
print(' '.join([str(i) for i in gen(pre,ino)]))