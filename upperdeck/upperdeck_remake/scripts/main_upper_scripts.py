#!/usr/bin/env python3
# -*- encoding: utf-8 -*-



from seleniumbase import Driver
#mine scrips import
from config import *
from info_for_new_user import information_for_new_user
from str_date import *
from function_for_log import *
from registration_new_user import reg_new_user
from open_pack import opening_pack
from func_accept_trade import accept_trade
from func_send_cards import send_cards



def main():
	answer = True
	while answer:	
		answer = False
		counts_results("start")
		debug("="*100)
		debug(get_str_date_now())
		write_step("="*100)
		write_step(f"{get_str_date_now()}		Start Script!")
		start_time = get_time()
		#########
		#False - отключает визуализацию
		with Driver(headed=False) as driver:
			driver.maximize_window()
			# Устанавливаем максимальное время ожидания в 30 секунд для всех элементов
			driver.implicitly_wait(30)
			# создаем всю информацию котоаря нужна при регистрации
			json_for_new_user = information_for_new_user()
			# регистрируем нового пользователя
			reg_new_user(json_for_new_user, driver)
			# открытие пака
			answer = opening_pack(driver)
			# отсылаем карты
			send_cards(driver)
			# принимаем карты
			answer = accept_trade()
		end_time = get_time()
		write_step(f"{get_str_date_now()}		Script Done!")
		final_log(start_time, end_time)
		counts_results("stop")
		debug("finish")




main()
