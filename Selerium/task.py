"""задача эмулировать ввод текста и обыграть партнеров"""
"""напишите скрипт который автоматически будет писать текст, соответственно обгоняя других учатников"""
"""
Адрес: ilovemymam@gmail.com
Логин: Ketsune-_-
Новый пароль: dd4d6182"""

import requests
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS


driver = webdriver.Chrome()
driver.maximize_window()
options_chrome.add_argument('user-data-dir=C:\\Users\\Admins\\AppData\\Local\\Google\\Chrome\\User Data')
url = "http://klavogonki.ru/"

driver.get(url)
login = "Ketsune-_-"
password = "dd4d6182"

elem1 = driver.find_element(By.XPATH, "//*[@id=\"login-link\"]/span").click()
elem2 = driver.find_element(By.XPATH, "//*[@id=\"username\"]").send_keys(login)
elem3 = driver.find_element(By.XPATH, "//*[@id=\"password\"]").send_keys(password)
elem4 = driver.find_element(By.XPATH, "//*[@id=\"login_form_submit\"]").click()

elem_psw = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/form/table/tbody/tr[3]/td/div/input").send_keys(password)
time.sleep(20000)
elem_capth = driver.find_element(By.XPATH,"/html/body/div[2]/div[3]/div[1]/div/div/span").click()
time.sleep(20000)
elem_going = driver.find_element(By.XPATH,"/html/body/div[6]/div/div/div/form/table/tbody/tr[5]/td/input").click()
# начало самой игры
elem5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"index\"]/div[1]/div[4]/div/a[2]"))).click()
elem6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit_btn\"]"))).click()
elem_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[3]/a"))).click()
wait_text = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]/span/span[2]")))
time.sleep(30)
url_test = driver.page_source

soup = BS(url_test, features="html.parser")
res = soup.find("div", class_="full")
print(res)
for span in res.findAll('span', {'style': 'display:none;'}):
    span.decompose()

print(res)
for i in res:
    print(i.text)
# time.sleep(200000)
res_text = "test"
# elem_text = ""
# блок текста появляется через "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]"
# elem_input = ""
# input_text = driver.find_element(By.XPATH, "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]").send_keys(res_text)
time.sleep(200000)

# driver.close()
# driver.quit()

# https://klavogonki.ru/g/?gmid=15031

