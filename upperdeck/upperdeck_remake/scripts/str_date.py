# -*- encoding: utf-8 -*-

from datetime import datetime


def get_str_date_now():
	"Выдает текущее время и дату"
	#10-04-2024 14:51:28
	date_now = datetime.now().replace(microsecond=0)
	str_now_date = date_now.strftime("%d-%m-%Y %H:%M:%S")
	return str_now_date



def get_time():
	"Выдает только время"
	time_now = datetime.now().replace(microsecond=0)
	return time_now
