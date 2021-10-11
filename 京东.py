from selenium import webdriver
import time

commodity=webdriver.Chrome()

commodity.get('https://www.jd.com/')

commodity.maximize_window()

commodity.find_element_by_xpath("//*[@id='key' and @accesskey='s']").send_keys('显卡')

ell=commodity.find_element_by_xpath("//*[@class='button']")

ell.click()

time.sleep(3)


commodity.find_element_by_xpath("//*[@id='J_goodsList']/ul/li[1]/div/div[1]/a/img").click()

data=commodity.window_handles

commodity.switch_to.window(data[1])

time.sleep(3)

commodity.find_element_by_xpath("//*[@id='InitCartUrl']").click()

commodity.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/div[3]").click()

commodity.find_element_by_xpath("//*[@id='loginname']").send_keys(17683828216)
time.sleep(1)

commodity.find_element_by_xpath("//*[@id='nloginpwd']").send_keys("131415hjj")
time.sleep(1)

commodity.find_element_by_xpath("//*[@id='loginsubmit']").click()




time.sleep(5)

commodity.quit()