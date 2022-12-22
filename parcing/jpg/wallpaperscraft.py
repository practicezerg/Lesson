from bs4 import BeautifulSoup as BS
import requests
import urllib.request
import time
import wget



session = requests.Session()
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
headers = {
    "User-Agent": useragent}


try1 = session.get("https://wallpaperscraft.ru/catalog/fantasy/1600x1200", headers=headers).text
soup = BS(try1, features="html.parser")
text1 = soup.find("div", class_="wallpapers wallpapers_zoom wallpapers_main").find_all("a", class_="wallpapers__link")
# print(text1)
url_main = "https://wallpaperscraft.ru/"
l_dl = []
res = ""
name_res = ""
url_fine = ""
for i in text1:
    url = i.get("href")
    name = url.lstrip("/download/").replace("/1600x1200", "")
    url_res = url_main + url
    l_dl.append(url_res)
    res += url_res + "\n"
    name_res += name + "\n"
    # print(f"название {name} и cсылка {url_res}")
    url_fine = f"https://images.wallpaperscraft.ru/image/single/{name}_1600x1200.jpg"
    # filename = wget.download(f"{url_res}.jpg")
    print(url_fine)
    urllib.request.urlretrieve(url_fine, f"{name}.jpg")
    time.sleep(10)

#по умолчанию будет лежать с проэтом водной папке
#название файла urlib
#

