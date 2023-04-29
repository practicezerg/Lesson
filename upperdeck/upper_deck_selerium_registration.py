import datetime
import time
import random
import requests
import json
from bs4 import BeautifulSoup
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def registration():
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    psw = ''  # предварительно создаем переменную psw.py
    for x in range(18):
        psw = psw + random.choice(list(random_string))
    name = names.get_full_name().split()
    first_name = name[0]
    second_name = name[1]
    email_add = ""
    for i in range(5):
        email_add = email_add + random.choice(list(random_string))
    email = second_name + email_add + "@gmail.com"
    username = second_name + email_add
    return first_name, second_name, psw, email, username


# запрос на страницу
driver = webdriver.Chrome()
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
Error_scripts = 0
ReG_is_ok = 0
tryroad = 10
while tryroad > 1:
    try:
        first_name, second_name, psw, email, username = registration()
        BirthDay = random.randint(1, 29)
        BirthMonth = random.randint(1, 12)
        BirthYear = random.randint(1975, 2003)
        confirm_psw = psw

        driver.maximize_window()
        driver.get("https://www.upperdeckepack.com/Registration")

        elem1 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[4]/div[1]/div/input")
        elem1.send_keys(first_name)

        elem2 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[4]/div[2]/div/input")
        elem2.send_keys(second_name)

        elem3 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[5]/div/input")
        elem3.send_keys(email)

        elem4 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[6]/div/select")
        elem4.send_keys("US")
        time.sleep(2)
        elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[1]/div/select")
        elem5.send_keys("December")
        elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[2]/div/select")
        elem5.send_keys(BirthDay)
        elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[3]/div/select")
        elem5.send_keys(BirthYear)
        elem6 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[9]/div/input")
        elem6.send_keys(username)
        elem7 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[11]/div[1]/div/input")
        elem7.send_keys(psw)
        elem8 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[11]/div[2]/div/input")
        elem8.send_keys(psw)
        elem8.send_keys(Keys.PAGE_DOWN)
        elem9 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[13]/label/input").click()
        time.sleep(1)
        elem10 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[16]/button").click()

        time.sleep(2)

        ReG_is_ok += 1
    except:
        print("Error")
        Error_scripts += 1
    print(ReG_is_ok, "удачных регистрации")
    print(Error_scripts, "ошибок при регистрации" )

    print("saved user+login")
    with open("users.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data[email] = psw
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    time.sleep(2)

    #попытка открытия пака
    print("Start Open Pack")
    driver.get("https://www.upperdeckepack.com/Store")
    elem11 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
    for _ in range(5):
        elem11.send_keys(Keys.DOWN)

    elem12 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a"))).click()
    time.sleep(2)
    elem13 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[3]/a/span"))).click()
    time.sleep(2)
    elem14 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[2]/button").click()
    time.sleep(5)
    print("Pack is opened")

    # передача карт
    driver.get("https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa")
    time.sleep(5)
    elem15 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
    time.sleep(1)

    elem16 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
    time.sleep(1)
    elem17 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/img").click()
    time.sleep(7)
    elem18 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
    elem19 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
    time.sleep(5000)
    elem20 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[4]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
    time.sleep(2)

    elem21 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"submit-trade\"]"))).click()



    # elem11 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
    # elem11.send_keys(Keys.DOWN)
    # elem12 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
    # elem12.send_keys(Keys.DOWN)
# elem13 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a"))).click()
# elem14 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[3]/a/span"))).click()
# time.sleep(2)
# elem15 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[2]/button").click()
# # elem16 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button")
# time.sleep(2)
# начало оффера
# driver.get("https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa")
# time.sleep(3)
# elem16 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
# time.sleep(500)
# elem17 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[3]/div[1]/div/div[1]/div/a/i")
# elem17.send_keys(Keys.DOWN)
# # elem17.click()
# time.sleep(1)
# elem18 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[3]/div[1]/div/div[1]/div/a/i").click()
# time.sleep(1)
# elem19 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[3]/div[3]/div[1]/div/div[1]/div/a/i").click()
# time.sleep(1)




time.sleep(15)

driver.close()
driver.quit()