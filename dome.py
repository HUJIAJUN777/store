'''猜字
import random
num=random.randint(0,10)
moni=100
i=0
while i<=10:
    a = int(input("请输入一个数字"))
    num=int(num)
    if num>a:
        print('太小了')
        moni=moni-10
        print('资金还剩：', moni)
    elif num<a:
        print('太大了')
        moni=moni-10
        print('资金还剩：',moni)
    else:
        print('猜对了，数字为：',num,'资金还剩',moni)
        break
    i=i+1
'''



