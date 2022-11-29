import requests


def pass_txt():
    open_file = open("passwords for freedom.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    open_file.close()
    return login, password




lgoin, password = pass_txt()
params = {

}
Heades = {

}

useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0 (Edition Yx 02)"
responce = requests.get("https://lk.freedom-vrn.ru/#/login?redirect=%2Fmain", params=params)
if responce:
    if responce.status_code == 200:
        print("get taked")
    elif 300 <= responce.status_code <= 400:
        print("куда то перенаправил")
    elif 400 < responce.status_code <= 499:
        print("error by client")
    else:
        print("server not answer")
else:
    print("Error requests.get")

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