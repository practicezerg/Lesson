from bs4 import BeautifulSoup as BS
import requests
import lxml
import re
import json

session = requests.Session()
stroka = session.get("https://ru.wikipedia.org/wiki/%D0%A2%D0%BE%D0%BC%D0%B0%D1%82").text
soup = BS(stroka, features="lxml")


# так же может исользоватся  features="html.parser"
# print(soup)
#получение всех тегов со страницы title
# title = soup.title
# print(title.string)

#find and find_all    первый ищет до первого появления. второй ищет по всему документу и создает СПИСОК!
# text1 = soup.find("h1")
# print(text1)
# text2 = soup.find_all("h1")
# print(text2)

#find and find_all    вторым параметром можно передавать class_=
# text3 = soup.find("td", class_="plainlist")
# print(text3.text)

# иногда можно парсить спомощью словаря задавая пары запросов

# text4 = soup.find("div", {"class": "ts-Taxonomy-rang-row"})
# print(text4.text)

# как спарсить ссылки
links = soup.find(class_="wikitable").find("tbody").find_all("a")
print(links)
test_for_json = {}
for i in links:
    item_text = i.text
    url = i.get("href")
    url2 = "https://ru.wikipedia.org"+url
    print(f"{item_text}: {url2}")


    test_for_json[item_text] = url2

    with open("fail.json", "w") as file:
        json.dump(test_for_json, file, indent=4, ensure_ascii=False)
        """indent параметр отступа в файле - если убрать будет все в одну строку"""
        """ensure)ascii - снимает проблемы с кодировкой"""

# по структуре снизу верх find_parent()  find_parents()

text5 = soup.find(class_="wrap").find_parent()
print(text5)

# по структуре снизу верх next_element (может выводить пустоту - тогда нужно повторить
next_el = soup.find(class_="ts-Начало_цитаты-quote").next_element.next_element
next_el2 = soup.find(class_="ts-Начало_цитаты-quote").find_next().text
print(next_el)
print(next_el2)

# по структуре снизу верх find_next_sibling() ищет элементы в рамках тега

text6 = soup.find(class_="ts-Начало_цитаты-quote").find_next_sibling()
print(text6)

text7 = soup.find(class_="ts-Начало_цитаты-quote").find_previous_sibling()
print(text7)

# если нужно найти конкретный текст

text8 = soup.find_all(text=re.compile("томат"))
print(text8)

text9 = soup.find_all(text=re.compile("([Тт]омат)"))
# Данная запись указывает все слова с маленькой и большой буквой

