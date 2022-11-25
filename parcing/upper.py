import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# указываем браузер
driver = webdriver.Chrome()
# запрос на страницу
driver.get("https://www.upperdeckepack.com/Collection")
time.sleep(5)
elem = driver.find_element(By.ID, "login-email")
# elem.clear()
elem.send_keys("gane.simonov.81@list.ru")
elem2 = driver.find_element(By.ID, "login-password")
elem2.send_keys("Topless81")
# elem3 = driver.find_element(By.CLASS_NAME, "form-check-input white").is_selected()
# print(elem3)
# if elem3 is
elem4 = driver.find_element(By.CLASS_NAME, "card-footer").click()

# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
time.sleep(20)
driver.close()
driver.quit()
