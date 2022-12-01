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


soup = BeautifulSoup(try1.text, features="html.parser")
text1 = soup.find_all("div", class_="section-item_content border pb-3")
# print(text1)
test555 = soup.find_all("h3")
all_names_marks = []
for i in test555:
    i = str(i)
    i = i.replace("<h3>", "")
    i = i.replace("</h3>", "")
    all_names_marks.append(i)

# print(all_names_marks)
# print(soup)
text2 = soup.find_all(class_="btn btn-cart")
links = []
for i in text2:
    i = str(i)
    i = i.replace("<a class=\"btn btn-cart\" href=\"", "").replace("\">купить</a>", "").replace("\">подробнее</a>","")
    links.append(i)
# print(links)

start_link = "https://rusmarka.ru"
final_link = []
for i in links:
    final_link.append(start_link + i)

# print(len(final_link))
# print(final_link[0])
n = 0
final_art = []
final_price = []
while n < len(final_link):
    try2 = session.get(final_link[n])
    soup2 = BeautifulSoup(try2.text, features="html.parser")
    text21 = soup2.find(class_="table text-center table-bordered")
    qq = text21.text
    qq = str(qq)
    qq = qq.split()
    art = qq[4]
    price = qq[6] + qq[7]
    final_art.append(qq[0] + " " + art)
    final_price.append(qq[2] + " " + price)
    n += 1

def final_res(all_names_marks,final_link,final_art,final_price):
    n = 0
    while n < len(final_link):
        stroka = final_art[n] + "-" + all_names_marks[n] + " = " + final_price[n] + "\n" + final_link[n]
        print(stroka)
        open_file = open("marki.txt", "a", encoding="utf-8")
        open_file.write(stroka + "\n")
        open_file.close()
        n += 1


final_res(all_names_marks,final_link,final_art,final_price)
print("End")





