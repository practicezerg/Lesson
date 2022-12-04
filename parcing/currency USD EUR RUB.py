import requests
from bs4 import BeautifulSoup


session = requests.Session()
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
headers = {"User-Agent": useragent}
try1 = session.get("https://cbr.ru", headers=headers).text
soup1 = BeautifulSoup(try1, features="html.parser")
USD = soup1.find("div", class_="col-md-2 col-xs-9 _dollar").text
EU = soup1.find("div", class_="col-md-2 col-xs-9 _euro").text
Yuan = soup1.find("div", class_="col-md-2 col-xs-9 _yuan").text
Value_price = soup1.find_all("div", class_="col-md-2 col-xs-9 _right mono-num")
USD_value = str(Value_price[1]).lstrip("<div class=\"col-md-2 col-xs-9 _right mono-num\">").replace("</div>","")
EU_value = str(Value_price[3]).lstrip("<div class=\"col-md-2 col-xs-9 _right mono-num\">").replace("</div>","")
Yuan_value = str(Value_price[5]).lstrip("<div class=\"col-md-2 col-xs-9 _right mono-num\">").replace("</div>","")

USD = (USD + " = " + USD_value).replace(" ","")
EU = (EU + " = " + EU_value).replace(" ","")
Yuan = (Yuan + " = " + Yuan_value).replace(" ","")
print(USD)
print(EU)
print(Yuan)
bank = USD + EU + Yuan