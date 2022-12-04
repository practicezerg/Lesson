import datetime
import time
import random
import requests
import json
from bs4 import BeautifulSoup
import names
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def registration():
    random_string = '123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
    psw = ''  # предварительно создаем переменную psw
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
    return first_name, second_name, psw, email, username

time_start = datetime.datetime.now()

driver = webdriver.Chrome()
first_name, second_name, psw, email, username = registration()
BirthDay = random.randint(1,29)
BirthMonth = random.randint(1,12)
BirthYear = random.randint(1975,2003)
# print(BirthDay, "BirthDay")
# print(BirthMonth, "BirthMonth")
# print(BirthYear, "BirthYear")
# print(first_name)
# print(second_name)
# print(psw)
# print(email)
# print(username)
confirm_psw = psw

useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
session = requests.Session()

headers = {
"User-Agent": useragent
}
try1 = session.get("https://www.upperdeckepack.com/Registration", headers=headers).text
# soup1 = BeautifulSoup(try1, features="html.parser")
# text1 = soup1.find_all("script", src_="")
# print(text1)
# # print(soup1)

# вроде как не меняется параметр /dist/main-client.js?v=lI3ZvFEVIYgAKkpM5mZOEEaRUydRg1PYNFBb_qjWjY8"
data = {
    "v": "lI3ZvFEVIYgAKkpM5mZOEEaRUydRg1PYNFBb_qjWjY8"
}
data = json.dumps(data)
try2 = session.get("https://www.upperdeckepack.com/dist/main-client.js?v=lI3ZvFEVIYgAKkpM5mZOEEaRUydRg1PYNFBb_qjWjY8", data=data, headers=headers).text
# tyty = json.loads(try2.content)


data = {
    "FirstName": first_name,
    "LastName": second_name,
    "BirthDay": BirthDay,
    "BirthMonth": BirthMonth,
    "CaptchaToken":"03AEkXODDLVi27sv9OUk9teA-sJNafQfk5-CD1EkksdA3SziJwbADku9Pq4Wn2SzYkkdaZQu6cY1TlphoamkhTb7go4eheR2Pc08KvdpDO1-PQ_DZDYOjFrHJ1l_WqCz9BhF5TNIqmTPO5DQY-2iOm8cxmC_pklucY7Xr6eBpqg1hFD8Igx3RJ1Ro0NlRoc3FfZ9mhgYgJLx3yazxiD7oqc-WB4BPEqLSLrcqFKmWT9VRfwflD9dMfzOZUYr0AjxpFePlZOxudjxRSflPAoomuzQwD5iMfTnfk5DaH-A8O7PhCcJlq5LBsaYmobTSwwCEeW12mT_CwkxuXvcLSKGBdcY_9plPFfn7RPe1Oe6Vt66iYk0LQZ3RJLb998KbK6hbxjsOHvXDKrLHTO-SjqCLLeMlEBQJ0ApxbnjE3q-sUYvmc-6Z3lPXUSpoXIiPccWIjvHyFljPNCBTeM35hErUHUsmWRshHtDr90eZvQKi_sr-aqrNyzO9YZnFtqYkoAcSAOjthhGXOuFnu",
    "Signature":"false",
    "EmailAddress": email,
    "BirthYear": BirthYear,
    "ConfirmPassword": psw,
    "Country": "US",
    "Password": psw,
    "UserName": username,
    "QuickRegistration": "false",
    "ReceiveMarketingEmails": "true",
    "TermsAndConditions": "true"
}
headers = {
    "User-Agent": useragent
}
try3 = requests.post("https://www.upperdeckepack.com/Registration", data=data, headers=headers).text
print(username)
open_file = open("any auth.html", "w", encoding="utf-8")
open_file.write(try3)
open_file.close()

"https://www.upperdeckepack.com/Profile/pdsdosoaaa"



print(datetime.datetime.now() - time_start)