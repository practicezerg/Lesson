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



def send_cards(driver):
	"Отправка карт донору"
	try_send = 5
	while try_send > 0:
		write_step(f"{get_str_date_now()}		send_cards(driver) start send cards!")
		try:
			driver.get(url_donor)
			time.sleep(5)
			# you get button
			#debug("get button")
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
			time.sleep(10)
			# choose one card
			#debug("one card")
			WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
			#driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i").click()
			# add my items
			#debug("add me item")
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/img").click()
			time.sleep(5)
			# add my 1
			#debug("add my 1")
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/a/i").click()
			# add my 2
			#debug("add my 2")
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div[3]/div/a/i").click()
			# add my 3
			#debug("add my 3")
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[4]/div[1]/div[2]/div/div[3]/div/a/i").click()
			time.sleep(5)
			# submite trade
			driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/button").click()
			# accept submite trade
			driver.find_element(By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div/button[1]").click()
			time.sleep(5)
			soup = BS(driver.page_source, features="html.parser")
			text1 = soup.find('div', class_="desktop-only pl-3 text-success")
			check_text = text1.text
			if check_text == "Trade Successfully Sent!":
				write_step(f"{get_str_date_now()}		send_cards(driver) cards sended!")
				break
			else:
				try_send -= 1
				write_error(f"send_cards(driver) Не удалось отправить карты")
				write_error(f"send_cards(driver) {try_send} осталось попыток")
		except Exception as e:
			debug(f"Ошибка {e}")
			try_send -= 1
			write_error(f"send_cards(driver) {try_send} осталось попыток")
			write_error(f"send_cards(driver) ошибка {e}")
	write_step(f"{get_str_date_now()}		send_cards(driver) start send done!")



