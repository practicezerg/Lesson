import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


# указываем браузер
driver = webdriver.Chrome()
# запрос на страницу
driver.get("http://www.python.org/%22")
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
time.sleep(20)
driver.close()
driver.quit()