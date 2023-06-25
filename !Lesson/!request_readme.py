import time
from bs4 import BeautifulSoup as BS
import requests
from fake_useragent import UserAgent

url = "http://httpbin.org/"

# req = requests.get(url)
# print(req)
"""
Вместе в url в request можно передовать 
params = Словарь или байты, которые будут отправлены в строке запроса
headers = словарь http-заголовка, отправленых с запросом
cookies = Объект Dict или CookieJar для отправки с запросом
auth = AuthObject для включения базовой аутентификации HTTP
timeout = Число с плавающей запятой, описывающее тайм-аут запроса.
allow_redirects = Логическое значение. Установите значение True, если разрешено перенаправление
proxies = Протокол сопоставления словаря с URL-адресом прокси.
stream = Удерживает соединение открытым, пока не получен весь Response.content
"""

# Для большого потока запросов есть смысл создавать фейковый юзерагент import fake_useragent

useragent = UserAgent()
print(useragent.random)   #Функция рандом эт не стандартный рандом, а часть fake_useragent

# Для использования proxy
# proxy = {
#     "http": "http://103.177.45.3:80",
#     "https": "http://103.177.45.3:80",
# }
# response = requests.get(url, proxies=proxy)
# print(response.json())

# скачивание изображения
req = requests.get("https://afabrica.ru/images/manga/IMG_2757.jpeg")
with open(file= "test.jpeg", mode= "wb") as file:
    file.write(req.content)

# timeout
"""Время ожидания ответа на запрос 21 секунда Чтобы сократить время этого ожидания до секунды
напишем тот же код только с атрибутом timeout=1. А если timeout=None будем ждать ответ вечно"""

start = time.perf_counter()
try:
    req = requests.get("http://reps.ru", timeout=1)
    print(req)
except Exception as ex:
    print(ex)
    print(time.perf_counter()-start)


"""Загружаем видео при помощи
Когда возникает потребность скачать видео с сайта мы прибегаем к помощи библиотеки она делает
эту задачу максимально простой
У метода .get() есть подходящий параметр для этих целей stream = True
stream = TrueПозволяет удерживать соединение пока мы не получили весь требуемый контент Этот
параметр используется при скачивании тяжеловесных файлов
Мы можем использовать response.content для загрузки если файл относительно не большой

Если файл очень большой или вы не хотите ждать пока файл скачает полностью то рекомендуется
использовать .iter_content() это метод который позволяет совершать итерацию по response.content
Для .iter_content() мы должны определить размер скачиваемой части файла
Параметром chunk_size=1000000 где цифра это размер в байтах
"""

req = requests.get("http://mail.ru")
print(req.status_code)
print("Вывод статус кода отдельно, для отработок ошибок")
print("*"*100)

# url = "https://parsinger.ru/task/1/"
# req = requests.get(url)
# soup = BS(req.text, features="html.parser")
# l_links = soup.find("div", class_="main")
# stroka = l_links.find_all("a")
# for i in stroka:
#     href = i.get("href")
#     req = requests.get(f"https://parsinger.ru/task/1/{href}")
#     if req.status_code == 200:
#         print(href)
print("Парсинг из кучи сcылок нужную")
print("*"*100)

req = requests.get("https://parsinger.ru/html/index1_page_1.html")
req.encoding = "utf-8"
soup = BS(req.text, features="html.parser")
price = soup.find("div", class_="item_card").find_all("p", class_="price")
for i in price:
    num = int(i.text.replace(" руб", ""))
    print(num)

print("Парсинг из под класса")
print("*"*100)

req = requests.get("https://parsinger.ru/html/hdd/4/4_1.html")
req.encoding = "utf-8"
soup = BS(req.text, features="html.parser")
price = soup.find("span", {"id":"price"}).text.replace(" руб", "")
full_price = soup.find("span", {"id":"old_price"}).text.replace(" руб", "")
anwer = (int(full_price) - int(price))*100/int(full_price)
print(anwer)
print("Парсинг цена и вычетание процента")
print("*"*100)

req = requests.get("https://parsinger.ru/html/index1_page_1.html")
main_link = "https://parsinger.ru/html/"
req.encoding = "utf-8"
soup = BS(req.text, features="html.parser")
pages = soup.find("div", class_="pagen").find_all("a")
#Что бы узнать всего страниц на сайте
num_pages = [link.text for link in soup.find("div", class_="pagen").find_all("a")][-1]
print(num_pages, "Количество страниц")
links = [link.get("href") for link in pages]
print(links)
pagen = [link["href"] for link in soup.find("div", class_="pagen").find_all("a")]
print(pagen)
final_links = [f'{main_link}{link["href"]}' for link in soup.find("div", class_="pagen").find_all("a")]
print(final_links)

print("Парсинг пагинация и извлечение href и как узнать количество страниц")
print("*"*100)

req = requests.get("https://parsinger.ru/html/index3_page_1.html")
main_link = "https://parsinger.ru/html/"
req.encoding = "utf-8"
soup = BS(req.text, features="html.parser")
num_pages =[link.text for link in soup.find("div", class_="pagen").find_all("a")][-1]
full_names = []
for page in range(1,int(num_pages)+1):
    req = requests.get(f'https://parsinger.ru/html/index3_page_{page}.html')
    req.encoding = "utf-8"
    soup = BS(req.text, features="html.parser")
    # name_item = soup.find_all("a", class_="name_item")
    name_item = [name.text for name in soup.find_all("a", class_="name_item")]
    full_names.append(name_item)
print(full_names)

print("Извлечение названия товара со всех 4 страниц")
print("*"*100)

links = [f'https://parsinger.ru/html/mouse/3/3_{num_page}.html' for num_page in range(1, 33)]
arts =[]
for link in links:
    req = requests.get(link)
    req.encoding="utf-8"
    soup = BS(req.text, features="html.parser")
    art = soup.find("p", class_="article").text.split()[-1]
    arts.append(art)
print(arts)

print("Извлечение артикула из каждой карточки товара")
print("*"*100)

headers = {
    'user-agent': useragent,
    'x-requested-with': 'XMLHttpRequest',
}
responce = requests.get(url, headers=headers).json()

#В панели разработчика в закладке сеть - Fetch/XHR - ищем сылку  в заголовках  x-requested-with': 'XMLHttpRequest
#в ответ он отдает формат json
#в некоторых случаяш нужно отсыдать попутно дату data
data = {
    "some info"
}

print("AJAX и эмуляция его")
print("*"*100)

print("Извлечение артикула из каждой карточки товара")
print("*"*100)