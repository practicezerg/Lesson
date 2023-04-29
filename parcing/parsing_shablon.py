import requests
from bs4 import BeautifulSoup
import time
import urllib
import csv

def get_html(url, params=None):
    r = session.get(url, headers=header, params=params)
    return r

def get_html2(url, params=None):
    d = requests.get(url, headers=HEADERS, params=params)
    return d


def get_pages_count(html):
    soup = BeautifulSoup(html, "html.parser")
    paginationTo = soup.find("div", class_="nums")
    if paginationTo:
        paginationTo = soup.find("div", class_="nums")
        pagination = paginationTo.find_all("a")
        return int(pagination[-1].get_text())
    else:
        return 1



HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
useragent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
session = requests.Session()
HOST = "https://freedom-vrn.ru/"
link = "https://lk.freedom-vrn.ru/#/login?redirect=%2Fmain"

header = {
    "user-agent": useragent
}
data ={}

responce = session.post(link, data=data, headers=header).text


html = get_html(ur  l)
if html.status_code == 200:
    catalog = []
    pages_count = get_pages_count(html.text)
else:
    print("Error")








parse()

