def welcome():
    print("==============================================")
    print("|------------中国工商银行账户管理系统------------|")
    print("|------------1、开户              ------------|")
    print("|------------2、取钱              ------------|")
    print("|------------3、存钱              ------------|")
    print("|------------4、转账              ------------|")
    print("|------------5、查询              ------------|")
    print("|------------6、退出              ------------|")
    print("==============================================")
import random
bank={}
#{'Frank': {'account': 15394946, 'password': '123456', 'country': '中国', 'province': '北京', 'street': '起码路', 'door': '001', 'money': 0, 'bank_name': '工商银行起码路分行'}}
bank_name="工商银行起码路分行"
#                 一一对应  ，  不是名称对应
def bank_adduser(account,username,password,country,province,street,door):
    if  len(bank) >100 :return 3#bank_adduer=3
    if username in bank:return 2#bank_adduer=2
    bank[username]={
        "account": account,#键：你输入的值account=random.randint(10000000,99999999)
        "password": password,# password = input("请输入您的密码")
        "country": country,#country = input("\t\t请输入您的国家")
        "province": province,
        "street": street,
        "door": door,
        "money":0,
        "bank_name":bank_name
    }
    print(bank)
    return 1#bank_adduer=1
def adduser():
    username=input("请输入您的用户名")
    password = input("请输入您的密码")
    print("请输入您的地址")
    country = input("\t\t请输入您的国家")
    province = input("\t\t请输入您的省份")
    street = input("\t\t请输入您的街道")
    door = input("\t\t请输入您的门牌号")
    account=random.randint(10000000,99999999)
    status=bank_adduser(account,username,password,country,province,street,door)
    if status == 1:
        print("恭喜你开户成功下面是你的信息")
        info = '''
                    ------------个人信息------------
                    用户名:%s
                    账号：%s
                    密码：*****
                    国籍：%s
                    省份：%s
                    街道：%s
                    门牌号：%s
                    余额：%s
                    开户行名称：%s
                '''
        # 每个元素都可传入%
        print(info % (username, account, country, province, street, door, bank[username]["money"], bank_name))

#存款
def saving():
    account:str=input('请输入您的账号')
    money=int(input('请输入您的存款金额'))
    if account in bank:
        bank[account]['money']=bank[account]['money']+money
        print(bank[account]['money'])
    else:
        print('您输入的账号不存在')

#取款
def withdrawal():
    accunt:str=input('请输入账号')
    password:str=input('请输入密码')
    if password==bank[accunt]['password']:
        money=int(input('请输入取款金额'))
        if accunt in bank:
            if bank[accunt]['money']-money<0:
                print('对不起，您的余额不足！')
            elif bank[accunt]['money']-money>0:
                bank[accunt]['money']=bank[accunt]['money']-money
                print('您的余额还剩:',bank[accunt]['mony=ey'])
        else:
            print('您输入的账号不存在')
    else:
        print('您输入的密码错误')

#转账
def transfer():
    global bank
    accunt:str=input('请输入账号')
    password:str=input('请输入密码')
    if password==bank[accunt]['passwprd']:
        if accunt in bank:
            str=input('请输入转账账号')
            if accunt in bank:
                money=int(input('请输入转账金额：'))
                if bank[accunt]['money'] - money < 0:
                    print('账户余额不足')
                elif bank[accunt]['money']-money>0:
                    bank[accunt]['money']=bank[accunt]['money']-money
                    bank[str]['money']=bank[str]['money']+money
                    print('转账成功，您的余额还剩：',bank[accunt]['money'])
                    print(bank)
            else:
                print('您输入的对方账号不存在')
        else:
            print('输入账号不存在')
    else:
        print('输入密码错误')

#查询
def lnquire():
    global bank
    accunt:str=input('请输入查询账号')
    if accunt in bank:
        password:str=input('请输入密码')
        if password==bank[accunt]['password']:
            print(bank[bank]['password'])
            print(bank[bank]['username'])
            print(bank[bank]['account'])
            print(bank[bank]['country'])
            print(bank[bank]['province'])
            print(bank[bank]['street'])
            print(bank[bank]['money'])

        else:
            print('您输入的密码不存在')
    else:
        print('您输入的账号不存在')











while True:
    welcome()
    begin=input("请选择业务")
    if begin == "1":
        print("1、开户")
        adduser()
    elif  begin == "2":
        print("2、取钱")
        withdrawal()
    elif  begin == "3":
        print("3、存钱")
        saving()
    elif  begin == "4":
        print("4、转账")
        transfer()
    elif  begin == "5":
        print("5、查询 ")
        lnquire()
    elif  begin == "6":
        print("6、退出")
        break

