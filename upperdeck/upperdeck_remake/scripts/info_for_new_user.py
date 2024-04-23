# -*- encoding: utf-8 -*-

import random
import names
import re
#mine scripts
from str_date import get_str_date_now
from write_errors_log import write_error
from config import *
from function_for_log import *


def information_for_new_user() -> str:
	"""
	Создает всю информацию по регистрации
	return str
	"""
	try:
		psw = random_psw()
		name = names.get_full_name().split()
		first_name = name[0]
		second_name = name[1]
		email_add = ""
		for i in range(5):
			email_add = email_add + random.choice(list(random_string))
		email = second_name + email_add + "@gmail.com"
		username = second_name + email_add
		birthday = random.randint(1, 29)
		birthmonth = random.randint(1, 12)
		birthyear = random.randint(1975, 2003)
		json_for_new_user = {
		"first_name":first_name,
		"second_name":second_name,
		"psw":psw,
		"email":email,
		"username":username,
		"birthday":birthday,
		"birthmonth":birthmonth,
		"birthyear":birthyear,
		}
		write_step(f"{get_str_date_now()}		information_for_new_user() done")
		return json_for_new_user
	except Exception as e:
		write_error(e)
	


def random_psw():
	"""генерация пароля
	Возвращает строку 8-15 символов"""
	while True:
		psw_length = random.randint(8, 15)
		psw = ''.join(random.choices(random_string, k=psw_length))
		if password_check(psw):
			return psw



def password_check(psw):
	"""
	Requires 8-15 characters, at least one upper case, lower case, and number.
	Требуется 8–15 символов, по крайней мере одна заглавная, строчная и цифра.

	Возвращает True или False
	"""
	# Проверяем длину строки
	if len(psw) < 8 or len(psw) > 15:
		return False
	# Проверяем наличие хотя бы одной строчной буквы
	if not re.search(r'[a-z]', psw):
		return False

	# Проверяем наличие хотя бы одной заглавной буквы
	if not re.search(r'[A-Z]', psw):
		return False

	# Проверяем наличие хотя бы одной цифры
	if not re.search(r'\d', psw):
		return False

	return True
