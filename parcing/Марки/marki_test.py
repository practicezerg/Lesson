import requests
import json
from bs4 import BeautifulSoup

"""спарсить первые 10 марок Артикул	Тип	Цена Название
https://rusmarka.ru/catalog/marki.aspx"""

session = requests.Session()
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"

data = {
}
headers = {
    "user-agent": useragent
}
try1 = session.get("https://rusmarka.ru/catalog/marki.aspx")
# try2 = session.post("https://rusmarka.ru/catalog/marki.aspx", data=data, headers=headers)


soup = BeautifulSoup(try1.text, features="html.parser")
text1 = soup.find("div", class_="section-item_content border pb-3")
zz = text1.find("h3")
zz = str(zz)
zz = zz.lstrip("<h3>")
name_marka = (zz[:zz.find("<")])
print(name_marka)

n = 0
# while n < 10:
"""где то тут нужен цикл"""

text2 = text1.find(class_="btn btn-cart")
# print(text1)

text2 = str(text2)
text2 = text2.lstrip("<a class=\"btn btn-cart\" href=\"")
find_ending = text2.find("\"")
end_link = text2[:find_ending]
start_link = "https://rusmarka.ru"
final_link = start_link + end_link
print(final_link)
try2 = session.get(final_link)
soup2 = BeautifulSoup(try2.text, features="html.parser")
text21 = soup2.find(class_="table text-center table-bordered")
qq = text21.text
qq = str(qq)
qq = qq.split()
art = qq[4]
price = qq[6] + qq[7]
print(qq[0], art)
print(qq[2], price)


open_file = open("marki.txt", "a", encoding="utf-8")
open_file.write(name_marka +" "+final_link +" "+ qq[0]+" "+ art+" "+qq[2]+" "+ price+"\n")
open_file.close()

