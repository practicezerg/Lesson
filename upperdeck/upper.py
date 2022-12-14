import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import random


def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password

def msg_for_forum():
    l = ["Hi somebody wanna trade?", "anybody here? Go trade!", "Go trade with me-_-?", "May be stop blank?Go trade ))",
         "Any wanna purple cards?20 purple for 1 Combinable?", "Hey wanna trade? msg me!",
         "Check may be any card need you ?",
         "Looking for UpperDeck base, any set", "All available, send an offer!", "hi be free for trade?? or blank",
         "Taking any trades doesn’t have to be anything"]
    msg_for_forum = l[random.randint(0, len(l) - 1)]
    return msg_for_forum


login, password = pass_txt()
login = "unknown_rus@mail.ru"
password = "Xmzk8825x"
msg_for_forum = msg_for_forum()
print(login)
print(password)
print(msg_for_forum)
# указываем браузер
driver = webdriver.Chrome()
driver.maximize_window()
# запрос на страницу
driver.get("https://www.upperdeckepack.com/Chat/Sports")
time.sleep(5)
elem = driver.find_element(By.ID, "login-email").send_keys(login)
elem2 = driver.find_element(By.ID, "login-password").send_keys(password)
elem3 = driver.find_element(By.CLASS_NAME, "card-footer").click()
time.sleep(15)
# time.sleep(50000)
elem4 = driver.find_element(By.CLASS_NAME, "character-countdown").send_keys(msg_for_forum)
time.sleep(5)
elem5 = driver.find_element(By.CLASS_NAME, "fa fa-arrow-down ").click()


time.sleep(50000)
driver.close()
driver.quit()
