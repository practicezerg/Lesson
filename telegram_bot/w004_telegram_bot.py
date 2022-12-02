import datetime
import time
import random
import requests
import json
import logging
from bs4 import BeautifulSoup
from auth_data import token
from aiogram import Bot, Dispatcher, executor, types

"""aiogramm"""



def messege_for_tg():
    session = requests.Session()
    useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
    headers = {
        "User-Agent": useragent
    }
    try1 = session.get("https://funpay.com/chips/85/", headers=headers).text
    soup1 = BeautifulSoup(try1, features="html.parser")
    text1 = soup1.find_all("div", class_="tc-price")
    text1 = text1[1:11]
    l = []
    l2 = []
    for i in text1[1:11]:
        i = str(i).replace("<div class=\"tc-price\" data-s=\"0\">", "").replace("</div>", "") \
            .replace("<span class=\"unit\">", "").replace("</span>", "").replace("<div>", "") \
            .replace("<div class=\"tc-price\" data-s=\"", "").replace("\">", "")
        i = i.replace(" ", "").replace("\n", "")
        l.append(i[1:11])
    return l



l = messege_for_tg()



def telegram_bot(token, messege_for_tg):
    pass

print(token)
bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("start")

@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("1)Нужен прайс с первого по 10 позицию, пиши price\n"
                        "2)Нужно минимальное значение по рынку, пиши price_min\n"
                        "3)Нужно Максимальное значение по рынку, пиши price_max")

@dp.message_handler(commands=['price'])
async def send_welcome(message: types.Message):
    await message.reply(l)

@dp.message_handler(commands=['price_min'])
async def send_welcome(message: types.Message):
    await message.reply(l[0])

@dp.message_handler(commands=['price_max'])
async def send_welcome(message: types.Message):
    await message.reply(l[9])


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)


# time_start = datetime.datetime.now()
