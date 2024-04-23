# -*- encoding: utf-8 -*-

import requests
import json
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as BS
import time
#mine scripts
from config import *
from write_errors_log import write_error
from function_for_log import *


def reg_new_user(json_for_new_user, driver):
	"""
	"first_name":first_name,
	"second_name":second_name,
	"psw":psw,
	"email":email,
	"username":username,
	"birthday":birthday,
	"birthmonth":birthmonth,
	"birthyear":birthyear,
	"""
	debug(json_for_new_user)
	"""Попытка регистрации нового юзера"""
	try:
		driver.get(url_registration)
		elem_first_name = driver.wait_for_element_visible("/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[3]/div[1]/div/input", timeout=10).send_keys(json_for_new_user["first_name"])
		elem_last_name = driver.type("/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[3]/div[2]/div/input", json_for_new_user["second_name"])
		elem_email = driver.type( "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[4]/div/input",json_for_new_user["email"])
		#elem_country = driver.type( "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[5]/div/select", "US")
		# Находим элемент выпадающего списка
		select_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[5]/div/select")
		# Создаем экземпляр класса Select с найденным элементом
		select = Select(select_element)
		# Выбираем опцию по видимому тексту
		select.select_by_value("US")
		elem_username = driver.type("/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[6]/div/input", json_for_new_user["username"])
		elem_psw = driver.type("/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[8]/div[1]/div/input", json_for_new_user["psw"])
		elem_re_psw = driver.type("/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[8]/div[2]/div/input", json_for_new_user["psw"])
		elem_iagree = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/label/input").click()
		elem_byclick = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").click()
		#debug("попытка прокрутки")
		elem_byclick = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").send_keys(Keys.PAGE_DOWN)
		#debug("крутим!")
		elem_button_create_account = WebDriverWait(driver, 50).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[13]/button"))).click()
		time.sleep(5)
		page_source = driver.page_source
	
		soup1 = BS(driver.page_source, features="html.parser")
		check_username = soup1.find("span", class_="username")

		# Проверка никнейма с сайта личной страницы и с тем что мы получили при регистрации
		if check_username.text != json_for_new_user["username"]:
			write_error(f'Полученные данные не совпадают или не удалось зарегестрироваться. Получили = {check_username.text}, а должны были получить {json_for_new_user["username"]}')
			debug(f'Полученные данные не совпадают или не удалось зарегестрироваться. Получили = {check_username.text}, а должны были получить {json_for_new_user["username"]}')
		
		write_step(f"{get_str_date_now()}		reg_new_user() done")

		# Сохраняем данные аккаунтов созданных
		json_for_accounts = {
			json_for_new_user["email"] : {
				"username": json_for_new_user["username"],
				"psw": json_for_new_user["psw"],
			}
		}
		#debug(json_for_accounts)
		write_json_user(json_for_accounts)

	except Exception as e:
		debug(f"Ошибка {e}")
		write_error(f"reg_new_user() ошибка {e}")


	
def write_json_user(json_for_accounts):
	"""Дозапись в файл json"""
	with open(f"{path_for_log}accounts.json", "r", encoding="utf-8") as r:
		json_temp = json.load(r)
	
	json_temp.update(json_for_accounts)

	with open(f"{path_for_log}accounts.json", "w", encoding="utf-8") as w:
		json.dump(json_temp, w)
	write_step(f"{get_str_date_now()}		write_json_user(json_for_accounts) done")
