import random
import json
import time
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS


def info_for_rega():
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    psw = ''  # предварительно создаем переменную psw
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
    BirthDay = random.randint(1, 29)
    BirthMonth = random.randint(1, 12)
    BirthYear = random.randint(1975, 2003)

    return first_name, second_name, psw, email, username, BirthDay, BirthMonth, BirthYear


def rega(first_name, second_name, psw, email, username, BirthDay, BirthMonth, BirthYear):

    driver.get("https://www.upperdeckepack.com/Registration")
    elem1 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[4]/div[1]/div/input").send_keys(first_name)
    elem2 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[4]/div[2]/div/input").send_keys(second_name)
    elem3 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[5]/div/input").send_keys(email)
    elem4 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[6]/div/select").send_keys("US")
    time.sleep(2)
    elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[1]/div/select").send_keys("December")
    elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[2]/div/select").send_keys(BirthDay)
    elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[8]/div[3]/div/select").send_keys(BirthYear)
    elem6 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[9]/div/input").send_keys(username)
    elem7 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[11]/div[1]/div/input").send_keys(psw)
    elem8 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[11]/div[2]/div/input")
    elem8.send_keys(psw)
    elem8.send_keys(Keys.PAGE_DOWN)
    elem9 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[13]/label/input").click()
    time.sleep(1)
    elem10 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div[1]/form/div[16]/button").click()
    time.sleep(3)
    try:
        elem11 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div/div[2]/div[1]/div[1]/span/div")
        return "ok"
    except:
        return "err"

def write_data(email, psw):
    print("saved user+login")
    with open("users.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    data[email] = psw
    with open('users.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    time.sleep(2)


def rega_final():
    Rega_is_ok = 0
    Error_rega = 0
    n = 2
    while n > 1:
        try:
            first_name, second_name, psw, email, username, BirthDay, BirthMonth, BirthYear = info_for_rega()
            a = rega(first_name, second_name, psw, email, username, BirthDay, BirthMonth, BirthYear)
            if a == "ok":
                Rega_is_ok += 1
                print("Успешных регистраций", Rega_is_ok)
                write_data(email, psw)
                n = n - 2
            else:
                Error_rega += 1
                print("Завершилось ошибкой", Error_rega)
        except:
            Error_rega += 1
            print("Завершилось ошибкой", Error_rega)


def open_pack2():
    driver.get("https://www.upperdeckepack.com/Collection")
    time.sleep(5)
    soup1 = BS(driver.page_source, features="html.parser")
    text1 = soup1.find_all("span", class_="filter-count")
    text1 = (str(text1)).lstrip("[<span class=\"filter-count\"> ").replace("</span>]", "")
    if text1 == "(0)":
        return "Error"
    else:
        return "ok"


def open_pack():
    n = 1
    while n > 0:
        try:
            print("Start Open Pack")
            driver.get("https://www.upperdeckepack.com/Store")
            time.sleep(2)
            elem12 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
            for _ in range(5):
                elem12.send_keys(Keys.DOWN)
            elem13 = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a"))).click()
            time.sleep(2)
            elem14 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                (By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[3]/a/span"))).click()
            time.sleep(2)
            elem15 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[2]/button").click()
            time.sleep(5)
            res_open_pack = open_pack2()
            if res_open_pack == "ok":
                n = n - 1
                print("Pack is opened")
            else:
                print("No Cards")
        except:
            print("Error with open pack")


driver = webdriver.Chrome()
driver.maximize_window()

rega_final()
open_pack()
time.sleep(5000)
print("script done")
driver.close()
driver.quit()