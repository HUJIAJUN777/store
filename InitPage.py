'''
    1.数据类：
        只准备数据部分：不参与任何操作。
    任务1：
        将这个框架的数据源集中写到excel表里，使用xlrd读取
        xlrd参数化，mysql的参数化。
'''
import pandas as pd
import xlrd
import pymysql




class  InitPage:
    login_success_data=[]




    wd = xlrd.open_workbook(r'HKR.xlsx', encoding_override=True).sheet_by_name('Login')

    row=wd.nrows

    for i in range(1,row):
        data=wd.row_values(i)
        if isinstance(data[1],float)==True:
            data[1]=int(data[1])

        dict={'username':data[0],'password':str(data[1]),'expect':data[2]}

        login_success_data.append(dict)

    success=[]
    con=pymysql.connect(host='localhost',user='root',password='root',database='zgnyyh')
    cursor=con.cursor()

    sqll='select * from user'

    cursor.execute(sqll)

    data3=cursor.fetchall()
    for i in data3:
        if isinstance(i[1],float)==True:
            i[1]=int(i[1])
            dict3=dict2={"username": i[0], "password": i[1], "expect": i[2]}
            success.append(dict3)

    con.commit()

    cursor.close()
    con.close()


#
#
#
    # login_success_data = xlrd.read()

    # login_error_data = [
    #     # id : msg_uname
    #     {"username": "jason1213123123123", "password": "1234567", "expect": "账户名错误或密码错误!别瞎弄!"},
    #     {"username": "不再爱了", "password": "123456789898945", "expect": "账户名错误或密码错误!别瞎弄!"}
    # ]
    #





















