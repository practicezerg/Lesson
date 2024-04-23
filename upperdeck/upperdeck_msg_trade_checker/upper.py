#!/usr/bin/python3
import requests
from auth_data import token
import time
import datetime
import json


def pass_txt():
    open_file = open("/home/jung/for_server/pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password
def logging(login, password):
    session = requests.Session()
    useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    headers = {
        "User-Agent": useragent,
        "Connection": "keep-alive"
    }
    data = {
        "email": login,
        "password": password,
        "rememberMe": "",
        "twoFactorCode": "",
        "site": "https://www.upperdeckepack.com/",
        "platform": "ePack"
    }
    try1 = session.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", headers=headers, data=data).text
    headers = {
        "User-Agent": useragent,
        "Connection": "keep-alive",
	"Cookie": "_ga=GA1.1.872823427.1607956655; cookie-policy-accepted=8c6cb54c-8f35-4fd3-991d-c3f9ea517177; _ga_RXQT1ZCBZZ=deleted; _gcl_au=1.1.1003272523.1698092262; Auth-Session=CfDJ8GyJo8OSPWFGmObNNEmpz9OQAax8luxw9R35ufbYOqu9EGJguUL59rYFktIrTtWg90sRt4a%2FtqfA4Ag4XtrI6EfzMIXIXE13J%2BpcWtD3RY29ztNC83xP6Q2xX4jd7HnD2VJ9ZJvpQjtAcV24y4lWHHrHU9XSZtetslzAskg1wYrO; EPack-Store-Session=CfDJ8IUK5BMv7otFot2toxfA5TiJwvdtSP9OPVbwglTv8BUsAKBAzkWRGEgULgVYlauAyiipVq6cEptp%2FQy2F8z2knl4EoT1XwkJlCFYUTRjUXnkDTQdsiOiTJkdmuTHhuUAjycOocU%2ByJfChk0qLVFoD3sD7LTBEMdGXI50gO%2B%2BkvEI; UD-ePack-Session=CfDJ8NLIzgXoRgZPhnZj%2FMw5Ep1yIpJhMhOJploWfT3wXw78RJo7SrRmFzpuKvRihzpXqJ8vzxh5%2B8l5LaNrfsAeKcCqHjWctagyz%2Bx6y%2BxUPBCyDsgxqPyIH3g1xDVDU78REwIxtPNJianhRayAcgUQRloX22a%2FeuNL3GmZn8CR9Jj8; remembrance=%2FyBo45nMAqf6IDOFRTsZXtzL%2F8EdsHOpblieMhJkrVA%3D; epack-remembrance=%2FyBo45nMAqf6IDOFRTsZXtzL%2F8EdsHOpblieMhJkrVA%3D; _ga_RXQT1ZCBZZ=deleted; SRVNAME=web_132_; epack-settings=%7B%22n%22%3A%7B%22Notifications%22%3A%5B%7B%22NotificationType%22%3A1%2C%22NotificationCount%22%3A0%2C%22LastViewed%22%3A%222023-12-04T15%3A43%3A14Z%22%2C%22Notify%22%3Afalse%7D%2C%7B%22NotificationType%22%3A2%2C%22NotificationCount%22%3A1%2C%22LastViewed%22%3A%222023-12-01T18%3A17%3A18Z%22%2C%22Notify%22%3Atrue%7D%2C%7B%22NotificationType%22%3A3%2C%22NotificationCount%22%3A0%2C%22LastViewed%22%3A%222023-12-03T21%3A01%3A58Z%22%2C%22Notify%22%3Afalse%7D%2C%7B%22NotificationType%22%3A4%2C%22NotificationCount%22%3A1%2C%22LastViewed%22%3A%222023-09-15T06%3A57%3A00Z%22%2C%22Notify%22%3Atrue%7D%5D%2C%22CanSetCookie%22%3Atrue%2C%22BellWasOpened%22%3Afalse%7D%2C%22b%22%3A%5B%5D%7D; _ga_RXQT1ZCBZZ=GS1.1.1701704590.248.1.1701704605.45.0.0"
  }
    try2 = session.get("https://www.upperdeckepack.com/api/User/Dashboard", headers=headers)
    json_data = try2.json()
    num_offers = json_data["DashboardStatus"]["ReceivedTrades"]
    num_msg = json_data["DashboardStatus"]["UnreadMessages"]
    return num_offers, num_msg
def send_msg(num_offers, num_msg):
    data_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    if num_msg >=1:
        params = {
            "chat_id": "791327576",
            "text": f"UpperDeck {data_time} милорд, у вас {num_msg} сообщени(е/я)."
        }
        responce = requests.get('https://api.telegram.org/bot' + token + '/sendMessage', params=params)
    if num_offers >= 1:
        params = {
            "chat_id": "791327576",
            "text": f"UpperDeck {data_time} милорд, у вас запрос на обмен ({num_offers})."
        }
        responce = requests.get('https://api.telegram.org/bot' + token + '/sendMessage', params=params)


def main():
    login, password = pass_txt()
    data_time2 = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
    num_offers, num_msg = logging(login, password)
    print(f"Checking {data_time2}\n"
          f"Количество офферов {num_offers}\n"
          f"Количество сообщений {num_msg}")
    send_msg(num_offers, num_msg)



main()

