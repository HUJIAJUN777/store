from threading import Thread

import time

basket=0
money=60

class EggTarts(Thread):
    name=''
    count=0

    def run(self) -> None:

        global basket
        global money

        while True:
            if basket <= 0:
                basket += 1
                self.count += 1
                print(self.name,'成功做了：%d个'% self.count)
            elif basket >= 500:
                time.sleep(3)
                print(self.name,'成功做了：%d个'% self.count)
            elif money <= 0:
                break

class Client(EggTarts):
    username=''
    counts=0


    def run(self) -> None:

        global basket
        global money

        while True:
            if money > 0:
                money -= 2
                self.counts += 1
                basket -= 1
                if basket <= 0:
                    time.sleep(2)
                print(self.username,'成功购买了一个')
            else:
                print(self.username,'总共抢到了：',self.counts,'个蛋挞')

                break







a1=EggTarts()
a2=EggTarts()
a3=EggTarts()

a1.name='胡厨师'
a2.name='懂厨师'
a3.name='李厨师'

a1.start()
a2.start()
a3.start()

b1=Client()
b2=Client()
b3=Client()
b4=Client()
b5=Client()
b6=Client()

b1.username='小王'
b2.username='小李'
b3.username='小陈'
b4.username='小赵'
b5.username='小胡'
b6.username='小懂'

b1.start()
b2.start()
b3.start()
b4.start()
b5.start()
b6.start()
