# -*- encoding: utf-8 -*-

import random
from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
#my scripts
from list_messenges import *
from config import *
from telegram_msg import tg_msg_log
from str_date import *
from write_errors_log import *

	

def logging(driver):
	"""
	Подключение к серверу
	"""
	try:
		driver.get(url_forum)
		time.sleep(5)
		# autorization
		elem_login = driver.type("/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[1]/div/input", login_main)
		elem_psw = driver.type("/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/input", psw_main)
		elem_signin = driver.wait_for_element_visible("/html/body/div[2]/div/div/div/div[2]/div/form/div[3]/button", timeout=10).click()
		time.sleep(5)
		msg = take_random_msg()
		#debug(msg)
		# Нужен sleep, так как стоит долгая защита от спама. Подбором 40 секунд выставил
		time.sleep(40)
		elem_area_for_text = driver.wait_for_element_visible("/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/textarea", timeout=50).send_keys(msg)
		elem_byclick = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]").click()
			
		# строка, в которую нужно вставить текст
		"/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[1]/textarea"
		# кнопка отправки текста
		"/html/body/div[1]/div/div[4]/div/div[2]/div/div[1]/div[2]/div/div/div/div/div[2]"

		text = f"{get_str_date_now()}	Script upperdeck_forum_msg   выполнен успешно"
		tg_msg_log(text)

	except Exception as e:
		write_error(f"{get_str_date_now()} Script upperdeck_forum_msg  ошибка {e} ")
		#debug(e)


def take_random_msg():
	"Выбирает случайное сообщение"
	msg = random.choice(list_msg)
	return msg


def main():
	
	#False - отключает визуализацию
	with Driver(headed=False) as driver:
		driver.maximize_window()
		driver.implicitly_wait(30)
		logging(driver)


main()