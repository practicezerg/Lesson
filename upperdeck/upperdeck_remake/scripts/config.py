# -*- encoding: utf-8 -*-

from datetime import datetime

from str_date import get_str_date_now


#name script
script_name = "UpperDeck open cards v4" 

#path
path_for_main = "/home/jung/scripts/upperdeck/upperdeck_remake/"
path_for_scripts = "/home/jung/scripts/upperdeck/upperdeck_remake/scripts/"
path_for_log = "/home/jung/scripts/upperdeck/upperdeck_remake/log/"


# LOGS
steps_log = "/home/jung/scripts/upperdeck/upperdeck_remake/log/log_script_step.txt"

#auth

login_upper = "gane.simonov.81@list.ru"
psw_upper = "Topless81"
useragent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/99.0.0.0"

#forum
login_main = "unknown_rus@mail.ru"
psw_main = "Xmzk8825x"

#tg

token_tg = "5878177496:AAHRpQ-8tDKD4fhYolBlLNZDdsJ9z3GvI34"
chat_id = "791327576"
chat_id_log = "-4057600612"

#urls

url_donor = "https://www.upperdeckepack.com/Trading/Create/pdsdosoaaa"

url_registration = "https://www.upperdeckepack.com/Registration"
url_dashboard = "https://www.upperdeckepack.com/Dashboard"
url_collection = "https://www.upperdeckepack.com/Collection"
url_store = "https://www.upperdeckepack.com/Store"
url_forum = "https://www.upperdeckepack.com/Chat/Sports"
url_received = "https://www.upperdeckepack.com/Trading/Received"

# debug function

def debug(data):
	with open(f"{path_for_log}debug.txt", "a", encoding="utf-8") as a:
		a.write(str(data)+"\n")


# other 

random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'