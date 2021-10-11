from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time

driver=webdriver.Chrome()



driver.get("http://localhost:8080/HKR/")

driver.maximize_window()

#登录
driver.find_element_by_xpath("/html/body/div/div/div[1]/div[2]/a[2]").click()

driver.find_element_by_xpath("//*[@id='loginname']").send_keys(13552648187)

driver.find_element_by_xpath("//*[@id='password']").send_keys('admin')

driver.find_element_by_xpath("//*[@id='submit']").click()

#按页查询
time.sleep(2)
driver.find_element_by_xpath("//*[@id='_easyui_tree_18']").click()
time.sleep(1)
ell=driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input")
ell.send_keys(Keys.CONTROL,'a')
ell.send_keys(5)

driver.find_element_by_xpath("//*[@id='history']/div/div/div[3]/table/tbody/tr/td[7]/input").send_keys(Keys.ENTER)

time.sleep(3)



#添加课程
driver.find_element_by_xpath("//*[@id='_easyui_tree_13']").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_panel']/div/div/div[1]/table/tbody/tr/td/a/span/span[1]").click()
time.sleep(1)
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[1]/td[2]/input").send_keys('上山打虎1111')
driver.find_element_by_xpath("//*[@id='course_form_add']/table/tbody/tr[2]/td[2]/textarea").send_keys('武松打虎1111')
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[7]/div[3]/a[1]/span").click()
driver.find_element_by_xpath("/html/body/div[10]/div[3]/a").click()



time.sleep(5)





driver.quit()