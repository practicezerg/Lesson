# -*- encoding: utf-8 -*-


from config import *
import requests


def tg_msg_log(text):
	"""
	Отправка сообщения в тг
	"""

	params = {
		"chat_id": chat_id_log,
		"text": text,
		}
	token = token_tg
	req = requests.get("https://api.telegram.org/bot"+ token + "/sendMessage", params=params)



def tg_msg(text):
	"""
	Отправка сообщения в тг
	"""

	params = {
		"chat_id": chat_id,
		"text": text,
		}
	token = token_tg
	req = requests.get("https://api.telegram.org/bot"+ token + "/sendMessage", params=params)