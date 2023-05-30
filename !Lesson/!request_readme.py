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