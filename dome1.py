'''十个数相加
a=int(input ('请输入第一个数'))
b=int(input('请输入第二个数'))
c=int(input('请输入第三个数'))
d=int(input('请输入第四个数'))
e=int(input('请输入第五个数'))
f=int(input('请输入第六个数'))
g=int(input('请输入第七个数'))
h=int(input('请输入第八个数'))
i=int(input('请输入第九个数'))
j=int(input('请输入第十个数'))
print("相加为：",(a+b+c+d+e+f+g+h+i+j))
'''


'''最大数
a=int(input ('请输入第一个数'))
b=int(input('请输入第二个数'))
c=int(input('请输入第三个数'))
d=int(input('请输入第四个数'))
e=int(input('请输入第五个数'))
f=int(input('请输入第六个数'))
g=int(input('请输入第七个数'))
h=int(input('请输入第八个数'))
i=int(input('请输入第九个数'))
j=int(input('请输入第十个数'))
print('最大数为：',max(a,b,c,d,e,f,g,h,i,j))
print("相加为：",(a+b+c+d+e+f+g+h+i+j))
miss=a+b+c+d+e+f+g+h+i+j
print('平均为:',(miss/10))
'''




'''区间数
import random
num=random.randint(50,150)
num=int(num)
print(num)
'''



'''三角形
a=int(input ('请输入第一个数'))
b=int(input('请输入第二个数'))
c=int(input('请输入第三个数'))
if a+b>c and a+c>b and b+c>a:
    print('能构成三角形')
elif a==b and a==c:
    print('等边三角形')
elif a==b or a==c or b==c:
    print('等腰三角形')
elif  a**a+b**b==c**c or a**a+c**c==b**b or c**c+b**b==a**a:
    print('直角三角形')
elif a+b<c and a+c<b and c+b<a:
    print('不构成三角形')
else:
    print('普通三角形')
'''



'''调换
a=56
b=78
print(a+22,b-22)
'''



'''登录
x="root"
c="admin"
i=0
u=3
while i<=2:
    a = input('请输入用户名')
    b = input('请输入密码')
    if a==x and b==c:
            print('登录成功')
            break
    else:
        print('用户名或密码输入错误，请重新登录')
        i=i+1
        if u==i:
            print('锁定')
'''



'''三角形
n = eval(input())#括号里面输入数量，代表最下面一行*的数量
for i in range(1,n+1,2):
    print('{0:^{1}}'.format('*'*i,n))
    '''



'''乘法表
i=1
while i<=9:
    j=1
    while j<=i:
        sum=j*i
        print('%dx%d=%2d'%(j,i,sum),end=('\t'))
        j+=1
    print()
    i+= 1
'''



'''乘法表
i=9
while i >= 1:
    j=1
    while j<=i:
        print('%dx%d=%-2d'%(j,i,j*i),end=('\t'))
        j += 1
    print()
    i-= 1
'''



'''#青蛙爬井
meter=0
day=0
while meter<20:
     meter+=3
     day+=1
     if meter>20:
        break
     else:
        meter-=2
print(day)
'''


'''阶乘
i=0
s=0
t=1
for i in range(1,21):
    t*=i
    s+=t
    print(s)
‘’‘




