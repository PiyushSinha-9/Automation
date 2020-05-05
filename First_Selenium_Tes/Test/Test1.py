
# opening google and serching something


from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome("/Users/piyush/Desktop/Automation/First_Selenium_Tes/Library/chromedriver")
# driver = webdriver.Firefox()
# driver = webdriver.Safari()
driver.set_page_load_timeout(10)
driver.get("http://google.com")
ele = driver.find_element_by_name("q")
ele.clear()
ele.send_keys("Piyush Sinha LinkedIn")
ele.send_keys(Keys.RETURN)
time.sleep(4)
driver.close()



