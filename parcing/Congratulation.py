from bs4 import BeautifulSoup as BS
import requests
import random


n = 2
l =[]
while n <= 5:
    url = f"https://pozdravok.com/pozdravleniya/prazdniki/noviy-god/s-nastupayushchim/{str(n)}.htm"
    session = requests.Session()

    try1 = session.get(url).text
    soup = BS(try1, features="html.parser")
    text1 = soup.find("div", class_="content").find_all("p")
    for i in text1:
        i = str(i).replace("<br/>", "\n")
        num = i.find(">")
        l.append(i[num+1:])
    n +=1

res_num = random.randint(1, len(l))
print(res_num)
print(l[res_num].replace("</p>",""))