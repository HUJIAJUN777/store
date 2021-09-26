from HTMLTestRunner import HTMLTestRunner
import  unittest
import zmail


tests=unittest.defaultTestLoader.discover(r'E:\py1\h\单元测试',pattern='Test*.py')


rubber=HTMLTestRunner.HTMLTestRunner(
    title='这是计算器测试报告',
    description='计算器加减乘除报告',
    verbosity=1,
    stream=open(file='计算器报告.html',mode='w+',encoding='utf-8')
)



rubber.run(tests)


file=open('计算器报告.html','r',encoding='utf-8')
msg=file.read()


msg_content={
    'subject':'主题：计算器测试报告',
    'content_text':'计算器加减乘除测试用例报告',
    'attachments':'计算器报告.html'
}

reviceser=['13552648187@163.com']

sender={'username':'846946095@qq.com','pwd':'szntkjupkkbdbdhf'}

server=zmail.server(sender['username'],sender['pwd'])

server.send_mail(reviceser,msg_content)