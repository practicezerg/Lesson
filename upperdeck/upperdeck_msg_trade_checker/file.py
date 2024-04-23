import random
import json
import time
import names
import requests
from seleniumbase import Driver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from urllib3.exceptions import NewConnectionError
from bs4 import BeautifulSoup as BS
from datetime import datetime

'''
Для  логирования используется библиотека import logging
перед всем кодом после библиотек прописываем 
logging.basicConfig(filename='parser.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
дальше в коде при необходимости пишем logging.info(текст сообщения) если хотим 
записать сообщение о каком то процессе
или logging.error(текст сообщения) если нужно записать что тут была ошибка

если у функции много аргументов, для читабильности лучше не писать их все в одну строчку
Пример
не читабильно 
a = rega(first_name, second_name, psw, email, username, BirthDay, BirthMonth, BirthYear, driver)

читабильно 
a = rega(
    first_name,
	second_name,
	psw,
	email,
	username,
	BirthDay,
	BirthMonth,
	BirthYear,
	driver
)
еще лучше если называть переменные как они написаны в функции
например функция write_debug(info_subject)
вызываем write_debug(info_subject="info_for_rega() done")

после return или другой подобной функции писать нечего не нужно, так как дальше уже код не пройдет

Если вызывать driver как переменную, тот ее обязательно нужно закрывать иначе и лучше всего использвоать with 

'''





def take_time_now():
	"""
	Получаем время события
	"""
	time_now = datetime.now().replace(microsecond=0)
	formatted_time = time_now.strftime("%d-%m-%Y %H:%M:%S")
	return formatted_time


def write_debug(info_subject):
	"""
	Пишет все действия для отладки о ошибки
	"""
	with open("send_card_upper_debug.txt", "a", encoding="utf-8") as w:
		formatted_time = take_time_now()
		w.write(f"{formatted_time}		{info_subject}\n")
		
		
		
def info_for_rega() -> str:
	"""
	Создает всю информацию по регистрации
	return str
	"""
	random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
	psw = ""
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
	# BirthDay = random.randint(1, 29)
	# BirthMonth = random.randint(1, 12)
	# BirthYear = random.randint(1975, 2003)
	write_debug("info_for_rega() done")
	return first_name, second_name, psw, email, username


def rega(first_name, second_name, psw, email, username, driver) -> str:
	"""
	Происходит регистрация пользователя
	Возвращает ok или err
	Для дальнейшей работы
	"""
	try:
		driver.get("https://www.upperdeckepack.com/Registration")
		time.sleep(2)
		WebDriverWait(driver, 20).until(
			EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[3]/div[1]/div/input"))).send_keys(first_name)
		#elem_first_name = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[3]/div[1]/div/input").send_keys(first_name)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[3]/div[2]/div/input").send_keys(second_name)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[4]/div/input").send_keys(email)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[5]/div/select").send_keys("US")
		driver.find_element(By.XPATH,
									"/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[6]/div/input").send_keys(username)
		driver.find_element(By.XPATH,
									"/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[8]/div[1]/div/input").send_keys(
			psw)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[8]/div[2]/div/input").send_keys(psw)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/label/input").click()
		driver.find_element(By.XPATH,"/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").click()
		driver.find_element(By.XPATH,
										   "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[10]/div/label/input").send_keys(Keys.PAGE_DOWN)
		time.sleep(3)
		driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div[1]/form/div[13]/button").click()
		time.sleep(10)
		try:
			time.sleep(2)
			elem11 = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div[1]/div[2]/div/div/section[1]/ul/li[4]/a/span")
			return "ok"
		except Exception as e:
			write_debug(e)
			main()
		write_debug("debug ~ rega() done")
	except TimeoutException:
		print("Element did not load within the time limit.")
		write_debug("Element did not load within the time limit.")
		main()
	except NewConnectionError as error_with_connect:
		write_debug(f"Ошибка подключения {error_with_connect}")
		main()

def write_data(email, psw):
	print("saved user+login")
	with open("users.json", "r", encoding="utf-8") as file:
		data = json.load(file)

	data[email] = psw
	with open('users.json', 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)
	time.sleep(2)
	print("debug ~ write_data() done")


def rega_final(driver):
	"""
	Стартовая функция
	"""
	Rega_is_ok = 0
	Error_rega = 0
	n = 2
	while n > 1:
		try:
			first_name, second_name, psw, email, username = info_for_rega()
			a = rega(first_name, second_name, psw, email, username, driver)
			if a == "ok":
				Rega_is_ok += 1
				print("Успешных регистраций", Rega_is_ok)
				#write_data(email, psw)
				n = n - 2
			else:
				Error_rega += 1
				print("Завершилось ошибкой", Error_rega)
				if Error_rega >= 5:
					driver.close()
					driver.quit()
					main()
		except NewConnectionError as error_with_connect:
			write_debug(f"Ошибка подключения {error_with_connect}")
			driver.close()
			driver.quit()
			main()
		except Exception as e:
			write_debug(e)
			Error_rega += 1
			print("Завершилось ошибкой", Error_rega)
			if Error_rega >= 5:
				driver.delete_all_cookies()
				driver.close()
				driver.quit()
				main()
	write_debug("rega final() done")
	with open("log_for_send_cards.txt", "r+", encoding="utf-8") as r:
		lines = r.readlines()
		#lines[1] всего попыток
		temp_num = int(lines[1])+ 1
		print(f"Попытка номер {temp_num}")
		lines[1] = str(temp_num) + "\n"
		r.seek(0)
		r.writelines(lines)


def open_pack2(driver) -> str:
	"""
	Проверка сколько карт
	"""
	try:
		driver.get("https://www.upperdeckepack.com/Collection")
		time.sleep(5)
		soup1 = BS(driver.page_source, features="html.parser")
		text1 = soup1.find_all("span", class_="filter-count")
		text1 = (str(text1)).lstrip("[<span class=\"filter-count\"> ").replace("</span>]", "")
		if text1 == "(0)":
			write_debug("open pack2() done with 0 cards")
			return "Error"
		else:
			write_debug("open pack2() done with 1+ cards")
			return "ok"
	except:
		driver.close()
		driver.quit()
		main()


def open_pack(driver):
	"""
	Открытие пака
	"""
	n = 1
	error_pack = 0
	while n > 0:
		try:
			print("Start Open Pack")
			write_debug("Start Open Pack")
			res_open_pack = open_pack2(driver)
			if res_open_pack == "Error":
				driver.get("https://www.upperdeckepack.com/Store")
				time.sleep(5)
				#elem12 = driver.find_element(By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")
				try:
					elem12 = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a")))
					for _ in range(5):
						elem12.send_keys(Keys.DOWN)
					elem13 = WebDriverWait(driver, 10).until(
						EC.element_to_be_clickable((By.XPATH, "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[1]/div[1]/div/a"))).click()
					time.sleep(3)
					# выбор самого пака
					#elem_mvp23_24 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[3]/a/span"))).click()

					#elem_ud22_23_ext = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
					#(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[1]/a/span"))).click()
					elem_ud23_24 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/a/span"))).click()
					#elem_ud22_23 = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(
						#(By.XPATH, "/html/body/div[1]/div/div[4]/div[2]/div[2]/div/div/div/div[1]/div/div[1]/div[3]/div[1]/div[1]/div/div/div[2]/a/span"))).click()
					time.sleep(5)
					WebDriverWait(driver, 10).until(
						EC.element_to_be_clickable((By.XPATH,  "//*[@id=\"Featured\"]/div/div[1]/div[3]/div[2]/button"))).click()
					write_debug("elem15 - ok")
					#Элемент картинки, что бы зацепиться для скрола
					#driver.execute_script("window.scrollBy(0, 500);")
					# elem_pic_for_pac = WebDriverWait(driver, 10).until(EC.presence_of_element_located(
					# 	(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div/div/div/div[1]/div[1]/div[2]/img[1]")))
					# for _ in range(5):
					# 	write_debug("Try scroll elem_pic_for_pack")
					# 	elem_pic_for_pac.send_keys(Keys.DOWN)
					# 	write_debug("scroll")
					#time.sleep(300)
					elem_open_scroll = WebDriverWait(driver, 15).until(
						EC.presence_of_element_located((By.XPATH,
													"//html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button")))
					driver.execute_script("arguments[0].scrollIntoView();", elem_open_scroll)
					WebDriverWait(driver, 15).until(
						EC.element_to_be_clickable((By.XPATH,  "//html/body/div[1]/div/div[4]/div/div/div/div/div[1]/div[2]/div[1]/button"))).click()
					write_debug("elem_open - ok")
					time.sleep(10)
					res_open_pack = open_pack2(driver)
					if res_open_pack == "ok":
						n = n - 1
						print("Pack is opened")
						write_debug("Pack is opened")
					else:
						print("No Cards")
						write_debug("No Cards")
				except:
					write_debug("Не нашел пак для открытия")
					main()

			else:
				n = n - 1



		except:
			print("Error with open pack")
			write_debug("Error with open pack")
			error_pack += 1
			if error_pack > 5:
				driver.close()
				driver.quit()
				main()
	print("debug ~ open pack() done")
	write_debug("Error with open pack")

def send_cards(driver):
	"""
	Отправка карт
	"""
	write_debug("Start send cards")
	n = 1
	count_error_send = 0
	while n > 0:
		try:
			driver.get("https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa")
			time.sleep(5)
			elem16_list_cards = driver.find_element(By.XPATH, "//*[@id=\"react-app\"]/div/div[4]/div/div[5]/div[1]/div[1]/a/i").click()
			time.sleep(5)
			elem_vsplit_push = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
																		"//*[@id=\"react-app\"]/div/div[5]/button"))).click()
			time.sleep(5)
			elem17 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
																				 "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[3]/div/div[1]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
			time.sleep(5)
			elem18 = driver.find_element(By.XPATH,
										 "//*[@id=\"react-app\"]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/a/img").click()
			time.sleep(7)
			elem19 = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
																				 "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[2]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
			time.sleep(3)
			elem_select_1_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
																				 "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[3]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
			elem_select_2_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,
																				 "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[3]/div/div[4]/div[1]/div[2]/div/div[3]/div/a/i"))).click()
			elem_select_3_card = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(((By.XPATH, "/html/body/div[1]/div/div[4]/div/div[3]/div/div/div[1]/div[1]/div[2]/div[3]/div/div[1]/button")))).click()
			time.sleep(3)
			elem_accept_trade_confirm = WebDriverWait(driver, 15).until(EC.element_to_be_clickable(((By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div/button[1]")))).click()
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
					write_debug("Cards Sended")
					driver.close()
					driver.quit()
					break

		except Exception as e:
			print("erorr with send")
			count_error_send += 1
			write_debug(f"Количкство ошибок {count_error_send}")
			if count_error_send > 5:
				driver.close()
				driver.quit()
				main()
			write_debug(e)

	write_debug("open pack() done")
	

def logging_accept(driver):
	"""
	Принятие трейда ответной стороной
	"""
	try:
		login = "gane.simonov.81@list.ru"
		psw = "Topless81"
		driver.get("https://www.upperdeckepack.com/Trading/Received")
		driver.find_element(By.XPATH,
										  "/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[1]/div/input").send_keys(
			login)
		driver.find_element(By.XPATH,
										"/html/body/div[2]/div/div/div/div[2]/div/form/div[2]/div[2]/div/input").send_keys(
			psw)
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable(((By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div/form/div[3]/button")))).click()

		WebDriverWait(driver, 20).until(EC.element_to_be_clickable(
			((By.XPATH, "/html/body/div[1]/div/div[4]/div/div/div/div/div[2]/div[3]/a/div[5]")))).click()
		WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
			((By.XPATH, "/html/body/div[1]/div/div[4]/div/div[1]/div/div[4]/div/div/div[1]/button")))).click()
		WebDriverWait(driver, 10).until(
			EC.element_to_be_clickable(((By.XPATH, "/html/body/div[3]/div/div/div/div[3]/div/button[1]")))).click()
		time.sleep(2)

		driver.get("https://www.upperdeckepack.com/Dashboard")
		time.sleep(3)
		soup1 = BS(driver.page_source, features="html.parser")
		text1 = soup1.find_all("div", class_="highlight-count count-text")
		l_res = []
		for i in text1:
			number_trades = i.text
			l_res.append(number_trades)
		print(l_res[0].split()[0])
		if int(l_res[0].split()[0]) > 30:
			check_15_true_try(int(l_res[0].split()[0]))
		if "Trade Received" in l_res[3]:
			res = l_res[3].replace(" Trade Received", "")
		if "Trades Received" in l_res[3]:
			res = l_res[3].replace(" Trades Received", "")

		res = int(res)
		if res == 0:
			print("Trade accepted by pdsdosoaaa")
			write_debug("Trade accepted by pdsdosoaaa")

		write_debug("logging_accept() done")
		with open("log_for_send_cards.txt", "r+", encoding="utf-8") as r:
			lines = r.readlines()
			#lines[3] удачных попыток
			temp_num = int(lines[3])+ 1
			print(f"Удачных попыток {temp_num}")
			lines[3] = str(temp_num) + "\n"
			r.seek(0)
			r.writelines(lines)

	except Exception as e:
		print("erorr with accept")
		write_debug("erorr with accept")
		write_debug(e)


def check_15_true_try(num):
	"""
	Подсчет карт на учетке, если больше 45
	"""
	check_num = num - 30
	if check_num > 15:                                          
		tg_msg(num)


def tg_msg(num):
	"""
	Отправка сообщения в тг
	"""
	text = f"Можно менять 15 накидали. Всего {num}"
	params = {
		"chat_id": "",
		"text": text,
		}
	token = ""
	requests.get("https://api.telegram.org/bot"+ token + "/sendMessage", params=params)


def main():
	with Driver(headed=False) as driver:
		driver.maximize_window()
		driver.implicitly_wait(30)
		
		write_debug("="*100)
		rega_final(driver=driver)
		open_pack(driver=driver)
		send_cards(driver=driver)
		logging_accept(driver=driver)
	write_debug("script done")
	print("script done")

loop = 5
while loop >=4:

	main()
