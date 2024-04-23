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






def opening_pack(driver):
	"""
	Открытие пака
	Если больше 5 попыток, то есть смысл начать занова
	"""
	try:
		count_try = 0
		write_step(f"{get_str_date_now()}		opening_pack(driver) Start Open Pack")
		answer = False
		while not answer:
			if count_try > 5:
				write_error("opening_pack(driver) Попыток c ошибкой больше 5")
				return False
			count_try += 1
			driver.get(url_store)
			time.sleep(5)
			# забираем нужный нам Xpah for pack
			path_xpah = choose_pack()
			# точка опоры для прокрутки
			#debug("na4alo otkritiya")
			# кликаем на choose your pack
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/a").click()
			#debug("vibiraem sam pack")
			# выбираем конкретный пак
			driver.find_element(By.XPATH, path_xpah).click()	
			#debug("gmem knopky open")
			# жмем кнопку open
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[2]/button").click()
			# нужно с ожиданием открыть ещё раз пак на новой странице
			#debug("ese raz otrivaem pack na novoi stranice")
			time.sleep(5)
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[1]/button").click()
			#debug("proveraem kolicestvo kart")
			answer = check_nums_cards(driver)
		write_step(f"{get_str_date_now()}		opening_pack(driver) done")
		return True
	except Exception as e:
		debug(f"Ошибка {e}")
		write_error(f"opening_pack(driver) ошибка {e}")




def check_nums_cards(driver):
	"""
	Проверка количества карт у пользователя
	"""
	write_step(f"{get_str_date_now()}		 check_nums_cards(driver) Start")
	driver.get(url_dashboard)
	# ожидание полной закгрузки страницы
	time.sleep(5)
	soup = BS(driver.page_source, features="html.parser")
	list_text1 = soup.find_all('div', class_='highlight-count count-text')
	#debug(list_text1)
	for pos in list_text1:
		if "Items" in pos:
			num_cards = pos.text
			#debug(num_cards)

	if num_cards != "0 Items":
		write_step(f"{get_str_date_now()}		 check_nums_cards(driver) done with 3 cards")
		return True
	write_step(f"{get_str_date_now()}		 check_nums_cards(driver) done with cards 0")
	return False


def choose_pack():
	"""
	Вынес сюда что бы не засорять XPAH
	"""
	# mvp 23-24
	#path_xpah = "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[3]/a/span"
	# ud_ser 22-23 extended
	#path_xpah = "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/a/span"
	# ud ser 1 23-24
	path_xpah = "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/a/span"
	return path_xpah