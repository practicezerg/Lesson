import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
import names


def pass_txt():
    open_file = open("../working/Complited/upperdeck/Check msg and offers/pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password


login, password = pass_txt()
print(login)
print(password)
# рандомим имя. Пока не знаю зачем
name_male = names.get_first_name(gender="male") + "\n"
print(name_male)
# указываем браузер
driver = webdriver.Chrome()
# запрос на страницу
driver.get("https://www.upperdeckepack.com/Collection")
time.sleep(5)
elem4 = driver.find_element(By.ID, "login-email")
# elem.clear()
elem4.send_keys(login)
elem2 = driver.find_element(By.ID, "login-password")
elem2.send_keys(password)
elem3 = driver.find_element(By.CLASS_NAME, "card-footer").click()
time.sleep(3)
# начало оффера
# driver.get("https://www.upperdeckepack.com/Marketplace?search={}".format(name_male))
driver.get("https://www.upperdeckepack.com/Checklists/Hockey/2020-21-UD-Series-2-Hockey")
time.sleep(5)
# elem = driver.find_element(By.LINK_TEXT, "/Checklists/Hockey/2020-21-UD-Series-2-Hockey").click()
# elem.clear()
# выбор карточки

# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source




time.sleep(20)
driver.close()
driver.quit()
