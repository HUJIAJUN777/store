from selenium import webdriver
import time

driver=webdriver.Chrome()



driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[1]").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys('胡佳俊')

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[2]").send_keys('胡佳俊')

driver.find_element_by_xpath("//*[@id='pwd']").send_keys(123456)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[4]").send_keys(123456)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[1]/input[5]").click()

time.sleep(3)

driver.find_element_by_xpath("//*[@id='valid_age']").send_keys(21)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/select[1]").send_keys('男')

driver.find_element_by_xpath("//*[@id='classname']").send_keys('Python自动化')

driver.find_element_by_xpath("//*[@id='msform']/fieldset[2]/input[3]").click()

driver.find_element_by_xpath("//*[@id='reg_mail']").send_keys('846946095@qq.com')

driver.find_element_by_xpath("//*[@id='reg_phone']").send_keys(17683828216)

driver.find_element_by_xpath("//*[@id='msform']/fieldset[3]/textarea").send_keys('湖北')

driver.find_element_by_xpath("//*[@id='btn_reg']").click()

driver.get("http://localhost:8080/HKR/")

driver.find_element_by_xpath("//*[@id='loginname']").send_keys(17683828216)

driver.find_element_by_xpath("//*[@id='password']").send_keys(123456)

driver.find_element_by_xpath("//*[@id='submit']").click()
time.sleep(2)
#换头像
driver.find_element_by_xpath("//*[@id='img']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='ul_pic']/li[5]/img").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()

#评价
driver.find_element_by_xpath("//*[@id='form_table']/tbody/tr[2]/td[2]/select").send_keys('7(没有晚自习)')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tea_td']/select").send_keys('贾生')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='textarea']").send_keys('无')
time.sleep(2)
driver.find_element_by_xpath("//*[@id='subtn']").click()
time.sleep(1)
#点击确定按钮
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a").click()

#修改个人信息
driver.find_element_by_xpath("//*[@id='_easyui_tree_8']").click()
driver.find_element_by_xpath("//*[@id='info']/table/tbody/tr[9]/td[2]/textarea").send_keys('上山打虎')
time.sleep(1)
driver.find_element_by_xpath("//*[@id='btn_modify']").click()
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()
time.sleep(1)

#查询好友
driver.find_element_by_xpath("//*[@id='_easyui_tree_10']").click()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='tt']/div[1]/div[3]/ul/li[2]/a[2]").click()

#退出
time.sleep(1)
driver.find_element_by_xpath("//*[@id='top']/div/a[2]/img").click()
time.sleep(3)

driver.quit()
