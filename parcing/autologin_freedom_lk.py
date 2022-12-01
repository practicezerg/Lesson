import requests
from bs4 import BeautifulSoup
import time
import urllib
import csv
import json


def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password

login, password = pass_txt()
print(login, password)
session = requests.Session()
link = "https://lk.freedom-vrn.ru/#/login?redirect=%2Fmain"
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"

data = {
    "appVersion": "LK, version: 1.1.154, svn: 167, build time: 2022-07-19 18:07:07",
    "method": "auth",
    "params": {
        "device": {
            "clientType": "browser",
            "model": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36",
            "platform": "Win32"
        },
        "password": password,
        "rememberMe": "true",
        "username": login
    }
}
data = json.dumps(data)
headers = {
    "User-Agent": useragent,
    'Content-type': 'application/json'
}

try1 = session.post("https://lk-api.freedom-vrn.ru/lk/api/v1", data=data, headers=headers)
print(try1.text)
tyty = json.loads(try1.content)

a = try1.text.find("Cid")
b = try1.text.find("\"error")
deviceCid = (try1.text[14:142])
print(deviceCid, "deviceCid")
token = try1.text[163:291]
print(token, "token")
data = {
    "appVersion": "LK, version: 1.1.154, svn: 167, build time: 2022-07-19 18:07:07",
    "deviceCid": deviceCid,
    "method": "getClient",
    "params": {}
}
headers = {
    "IC-token": token,
    "User-Agent": useragent,
    'Content-type': 'application/json'
}

data = json.dumps(data)
try2 = session.post("https://lk-api.freedom-vrn.ru/lk/api/v1", data=data, headers=headers)
print(try2.text)

open_file = open("any auth.html", "w", encoding="utf-8")
open_file.write(try2.text)
open_file.close()

