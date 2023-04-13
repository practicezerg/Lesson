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
    time.sleep(2)
    elem1 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[3]/div[1]/div/input").send_keys(first_name)
    elem2 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[3]/div[2]/div/input").send_keys(second_name)
    elem3 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[4]/div/input").send_keys(email)
    elem4 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[5]/div/select").send_keys("US")
    elem6 = driver.find_element(By.XPATH,
                                "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[6]/div/input").send_keys(username)
    elem7 = driver.find_element(By.XPATH,
                                "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[8]/div[1]/div/input").send_keys(
        psw)
    elem8 = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[8]/div[2]/div/input").send_keys(psw)
    elem_iagree = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[10]/label/input").click()
    elem_byclick = driver.find_element(By.XPATH,"/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").click()
    elem_byclick = driver.find_element(By.XPATH,
                                       "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").send_keys(Keys.PAGE_DOWN)
    time.sleep(3)
    elem_button_create_accpount = driver.find_element(By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div[1]/form/div[13]/button").click()
    time.sleep(3)
    try:
        time.sleep(2)
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
            if Error_rega >= 10:
                driver.close()
                driver.quit()


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
    error_pack = 0
    while n > 0:
        try:
            print("Start Open Pack")
            res_open_pack = open_pack2()
            if res_open_pack == "Error":
                driver.get("https://www.upperdeckepack.com/Store")
                time.sleep(5)
                elem12 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
                for _ in range(5):
                    elem12.send_keys(Keys.DOWN)
                elem13 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a"))).click()
                time.sleep(2)
                # выбор самого пака
                elem_ud22_23 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
                    (By.XPATH, "/html/body/div[3]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/a/span"))).click()
                time.sleep(5)
                elem15 = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH,  "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[2]/button"))).click()
                elem_open = WebDriverWait(driver, 15).until(
                    EC.element_to_be_clickable((By.XPATH,  "//html/body/div[3]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button"))).click()
                time.sleep(10)
                res_open_pack = open_pack2()
                if res_open_pack == "ok":
                    n = n - 1
                    print("Pack is opened")
                else:
                    print("No Cards")
            else:
                n = n - 1
        except:
            print("Error with open pack")
            error_pack += 1
            if error_pack > 5:
                driver.close()
                driver.quit()

def send_cards():
    n = 1
    while n > 0:
        try:
            driver.get("https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa")
            time.sleep(5)
            elem16 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
            time.sleep(1)

            elem17 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
            time.sleep(1)
            elem18 = driver.find_element(By.XPATH,
                                         "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/img").click()
            time.sleep(7)
            elem19 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[3]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
            time.sleep(3)
            elem21 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[3]/div/div[4]/div/div[3]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
            elem22 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
                                                                                 "/html/body/div[3]/div/div[4]/div/div[3]/div/div/div[3]/div/div[4]/div[1]/div[2]/div/div[3]/div/a/i"))).click()

            elem23 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "/html/body/div[3]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/button")))).click()
            time.sleep(3)
            elem23_5 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div/button[1]")))).click()
            # elem23_9 = WebDriverWait(driver, 15).until(
            #     EC.element_to_be_clickable(((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div/button[1]")))).click()
            # page = driver.page_source
            # soup = BS(page, features="html.parser")
            # text1 = soup.find("div", class_="modal-content")
            # for i in text1:
            #     accept = i.text
            #     print(accept)
            # if accept == "YesNo":
            #     elem23_9 = WebDriverWait(driver, 15).until(
            #         EC.element_to_be_clickable(((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div/button[1]")))).click()

            driver.get("https://www.upperdeckepack.com/Dashboard")
            time.sleep(15)
            soup1 = BS(driver.page_source, features="html.parser")
            text1 = soup1.find_all("div", class_="highlight-count count-text")
            l_res = []
            for i in text1:
                number_trades = i.text
                l_res.append(number_trades)
            res = l_res[2].replace(" Sent Trades", "")
            res = int(res)
            if res >= 1:
                    print("Cards Sended")
                    driver.close()
                    driver.quit()
                    break



        except Exception as e:
            print(e)
            print("erorr with send")

def logging_accept():
    with open("psw.txt", "r", encoding="utf-8") as file:
        slovo_test = file.readlines()
        login = slovo_test[0].replace("\n", "")
        psw = slovo_test[1].replace("\n", "")
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.upperdeckepack.com/Trading/Received")
    login = "gane.simonov.81@list.ru"
    psw = "Topless81"
    time.sleep(2)
    login_input = driver.find_element(By.XPATH,
                                      "/html/body/div[4]/div/div/div/div[2]/div/form/div[2]/div[1]/div/input").send_keys(
        login)
    psw_input = driver.find_element(By.XPATH,
                                    "/html/body/div[4]/div/div/div/div[2]/div/form/div[2]/div[2]/div/input").send_keys(
        psw)
    sign_in = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(((By.XPATH, "/html/body/div[4]/div/div/div/div[2]/div/form/div[3]/button")))).click()

    try_accept_trade = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        ((By.XPATH, "/html/body/div[3]/div/div[4]/div/div/div/div/div[2]/div[3]/a/div[5]")))).click()
    press_accept = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        ((By.XPATH, "/html/body/div[3]/div/div[4]/div/div[1]/div/div[4]/div/div/div[1]/button")))).click()
    accept_accept = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(((By.XPATH, "/html/body/div[7]/div/div/div/div[3]/div/button[1]")))).click()
    time.sleep(2)
    driver.get("https://www.upperdeckepack.com/Dashboard")
    time.sleep(3)
    soup1 = BS(driver.page_source, features="html.parser")
    text1 = soup1.find_all("div", class_="highlight-count count-text")
    l_res = []
    for i in text1:
        number_trades = i.text
        l_res.append(number_trades)
    res = l_res[3].replace(" Trades Received", "")
    res = int(res)
    if res == 0:
        print("Trade accepted by pdsdosoaaa")
        driver.close()
        driver.quit()

def main():
    rega_final()
    open_pack()
    send_cards()
    # with open("psw.txt", "r", encoding="utf-8") as file:
    #     slovo_test = file.readlines()
    #     login = slovo_test[0].replace("\n", "")
    #     psw = slovo_test[1].replace("\n", "")
    logging_accept()
    print("script done")

loop = 5
while loop >=4:
    driver = webdriver.Chrome()
    driver.maximize_window()
    main()