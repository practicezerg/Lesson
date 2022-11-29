import requests


params = {
    "q": "funny cats"
}

responce = requests.get("https://www.google.com/search", params=params)
if responce:

print(responce.status_code)
# 200 - успех
# 300-400 - перенаправление на другую страницу
# 400-500 ошибка на стороне клиента
# 500-600 нет ответа от сервера
# print(responce.headers)
# тут информация что сайт передает нашему браузеру
# print(responce.content)
# строка последовательности байт
# print(responce.text)
# по сути скачиваем траницу на комп
open_file = open("any auth.html", "w", encoding="utf-8")
open_file.write(responce.text)
open_file.close()

# особенность get запроса - передается в юрл строке как служебная страница