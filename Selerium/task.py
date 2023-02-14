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



driver = webdriver.Chrome()
driver.maximize_window()
url = "http://klavogonki.ru/"

driver.get(url)
login = "Ketsune-_-"
password = "dd4d6182"

elem1 = driver.find_element(By.XPATH, "//*[@id=\"login-link\"]/span").click()
elem2 = driver.find_element(By.XPATH, "//*[@id=\"username\"]")
elem2.send_keys(login)
elem3 = driver.find_element(By.XPATH, "//*[@id=\"password\"]")
elem3.send_keys(password)
elem4 = driver.find_element(By.XPATH, "//*[@id=\"login_form_submit\"]").click()
# начало самой игры
elem5 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"index\"]/div[1]/div[4]/div/a[2]"))).click()
elem6 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit_btn\"]"))).click()
elem_start = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[1]/div[2]/div[3]/table/tbody/tr[2]/td/div[3]/a"))).click()
time.sleep(15)
elem_text = ""
блок текста появляется через "/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[1]/div[1]"
elem_input = ""
сюда надо передавать"/html/body/div[7]/div/div/div[1]/table/tbody/tr/td[1]/div/table/tbody/tr/td/div[2]/div[2]/div[1]/div/div/div/div/div/div[2]/div[2]/input"
# span id afterfocus
time.sleep(100)
driver.close()
driver.quit()

# https://klavogonki.ru/g/?gmid=15031

