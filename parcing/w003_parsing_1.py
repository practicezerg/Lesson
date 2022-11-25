import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://www.upperdeckepack.com/Collection"
r = requests.get(URL_TEMPLATE)  # get запрос
print(r.status_code)    # 200 положительный ответ
print(r.text)

#вводные данные через
user_data = {
    "email": "gane.simonov.81@list.ru",
    "password": "Topless81",
    "rememberMe": True,
    "twoFactorCode": "",
    "site": "https://www.upperdeckepack.com",
    "platform": "ePack"
}
#<input type="email" class="form-control" id="login-email" placeholder="Email Address" value="gane.simonov.81@list.ru" aria-label="Email Address">