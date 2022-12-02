import datetime
import requests
from bs4 import BeautifulSoup


time_start = datetime.datetime.now()

session = requests.Session()
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
headers = {
    "User-Agent": useragent
}

try1 = session.get("https://funpay.com/chips/85/", headers=headers).text
soup1 = BeautifulSoup(try1, features="html.parser")
text1 = soup1.find_all("div", class_="tc-price")
# print(text1[1:11])
text1 = text1[1:11]
l = []
l2 = []
for i in text1[1:11]:
    i = str(i).replace("<div class=\"tc-price\" data-s=\"0\">","").replace("</div>", "")\
        .replace("<span class=\"unit\">", "").replace("</span>", "").replace("<div>", "")\
        .replace("<div class=\"tc-price\" data-s=\"","").replace("\">", "")
    i = i.replace(" ","").replace("\n","")
    l.append(i[1:11])
print(l)
for i in l:
    i = float(i[:-1])
    l2.append(i)
print(min(l2), "минимальная цена")
print(max(l2), "максимальная цена")
print(datetime.datetime.now() - time_start)

