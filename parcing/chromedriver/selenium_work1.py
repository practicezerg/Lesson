from selenium import webdriver
import os
import time


path = os.getcwd()+"chromedriver.exe"
print(path)
#переменная для запросов
url = "hh.ru"
#создание веббраузера
#При использовании в области Windows слеши нужно экранировать исрользуя \\
driver = webdriver.Chrome(executable_path=path)


try:
    driver.get(url=url)
    time.sleep(15)
    driver.get("url=https://ru.stackoverflow.com/")
except Exception as ex:
    print(ex)
finally:
    # Иначе куча виртуальных запросов
    driver.close()
    driver.quit()

