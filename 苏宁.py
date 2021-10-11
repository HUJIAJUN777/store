from selenium import webdriver
import time

commodity=webdriver.Chrome()

commodity.get('https://www.suning.com/')

commodity.maximize_window()

commodity.find_element_by_xpath("//*[@id='searchKeywords']").send_keys('手机')
time.sleep(1)

commodity.find_element_by_xpath("//*[@id='searchSubmit']").click()


commodity.find_element_by_xpath("//*[@id='pop418']/a").click()

commodity.find_element_by_xpath("//*[@id='ssdsn_search_pro_baoguang-1-1-1_1_01:0000000000_12235115639-gg']").click()

data=commodity.window_handles

commodity.switch_to.window(data[1])

commodity.find_element_by_xpath("//*[@id='addCart']").click()

time.sleep(5)

commodity.quit()