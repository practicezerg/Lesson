import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random
from selenium.webdriver.chrome.options import Options


def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[2].replace("\n", "")
    password = slovo_test[3].replace("\n", "")
    return login, password

def msg_for_forum():
    l = ["Hi somebody wanna trade?", "anybody here? Go trade!", "Go trade with me-_-?", "May be stop blank?Go trade ))",
         "Any wanna purple cards?20 purple for 1 Combinable?", "Hey wanna trade? msg me!",
         "Check may be any card need you ?",
         "Looking for UpperDeck base, any set", "All available, send an offer!", "hi be free for trade?? or blank",
         "Taking any trades doesn’t have to be anything", "Looking for wishlist trades", "Looking for trades", "Let's trade something",
         "Trading physical cards for bases", "Trading bases cards for physical", "no redeemed please!", "Same Years set for any"
         "Duples for Duples?", "go trade and have good day", "hey wanna same trade today?"]
    msg_for_forum = l[random.randint(0, len(l) - 1)]
    return msg_for_forum


n = 1
while n > 0:
    login, password = pass_txt()
    msg_for_forum = msg_for_forum()
    print(login)
    print(password)
    print(msg_for_forum)
    # указываем браузер
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    # driver.maximize_window()
    # запрос на страницу
    driver.get("https://www.upperdeckepack.com/Chat/Sports")
    time.sleep(5)
    elem = driver.find_element(By.ID, "login-email").send_keys(login)
    elem2 = driver.find_element(By.ID, "login-password").send_keys(password)
    elem3 = driver.find_element(By.CLASS_NAME, "card-footer").click()
    time.sleep(4)
    elem4 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/textarea").send_keys(msg_for_forum)
    time.sleep(3)
    elem5 = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]").click()
    #ожидание 30 минут
    print("msg sended")
    time.sleep(1800)


driver.close()
driver.quit()
