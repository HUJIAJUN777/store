from selenium import webdriver


commodity=webdriver.Chrome()

commodity.get('http://www.baidu.com')

commodity.maximize_window()

commodity.find_element_by_xpath("//*[@id='kw' and @name='wd']").send_keys('自动化测试')

ell=commodity.find_element_by_xpath("//*[@id='su']")

ell.click()

commodity.quit()