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
from seleniumbase import Driver
#mine scripts
from config import *
from write_errors_log import write_error
from function_for_log import *
from telegram_msg import *



def accept_trade():
	"""
	Принятие трейда ответной стороной
	"""
	write_step(f"{get_str_date_now()}		accept_trade() start")
	try:
		#False - отключает визуализацию
		with Driver(headed=False) as driver:
			driver.maximize_window()
			# Устанавливаем максимальное время ожидания в 30 секунд для всех элементов
			driver.implicitly_wait(30)

			driver.get(url_received)
			time.sleep(8)
			# autorization
			driver.type("/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[1]/div/input", login_upper)
			driver.type("/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/input", psw_upper)
			# sign in
			driver.wait_for_element_visible("/html/body/div[2]/div/div/div/div[2]/div/form/div[3]/button", timeout=10).click()
			time.sleep(5)
			# accept_trade
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[3]/a/div[5]").click()
			# press_accept
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[1]/div/div[4]/div/div/div[1]/button").click()
			# confirm accept
			driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div/button[1]").click()
			# Проверка что приняли трейд
			driver.get(url_dashboard)
			time.sleep(3)
			soup1 = BS(driver.page_source, features="html.parser")
			list_text1 = soup1.find_all("div", class_="highlight-count count-text")
			for pos in list_text1:
				if "Items" in pos:
					num_cards = pos.text
			nums_cards = num_cards.split()[0]
			num_temp = int(nums_cards) - 50
			if int(num_temp) % 15 == 0:
				text_for_tg = f"Накидали 15 карт - всего карт {nums_cards}!"
				tg_msg(text_for_tg)
		text = f"{get_str_date_now()}	Script main_upper_scripts   выполнен успешно"
		tg_msg_log(text)
		write_step(f"{get_str_date_now()}		accept_trade() done")
		return True

	except Exception as e:
		write_error(f"{get_str_date_now()} Script accept_trade()  ошибка {e} ")
		return True