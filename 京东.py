from selenium import webdriver


commodity=webdriver.Chrome()

commodity.get('http://www.jd.com')

commodity.maximize_window()

commodity.find_element_by_xpath("//*[@id='key' and @accesskey='s']").send_keys('显卡')

ell=commodity.find_element_by_xpath("//*[@class='button']")

ell.click()

commodity.quit()