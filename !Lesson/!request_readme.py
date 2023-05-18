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