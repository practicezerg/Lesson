# -*- encoding: utf-8 -*-

from str_date import get_str_date_now
from config import *


def write_error(data):
	"Пишит ошибки только"
	with open(f"{path_for_log}errors.txt", "a", encoding="utf-8") as a:
		full_msg = f"{get_str_date_now()}\n{data}"
		a.write(str(full_msg)+"\n")
