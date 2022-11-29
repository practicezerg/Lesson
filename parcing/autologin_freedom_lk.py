import requests
from bs4 import BeautifulSoup
import time
import urllib
import csv


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
data = {
    "appVersion": "LK, version: 1.1.154, svn: 167, build time: 2022-07-19 18:07:07",
    "deviceCid": "QYD3TEENZTOIO3MOOXM2TLSG7539APM10ERMZG0RC558NLP1E1JR8Y4X4HD341OZ8F5NJNF12SAG7IHL7N1JORZ4V5Q3IPQKLBV7842GUU8GGMJC4FNSTO44KVQ2C6LN",
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
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
}

try1 = session.post(link, data=data, headers=headers).text
print(try1)

