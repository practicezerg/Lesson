# str = "\n \n\nСистема\n\n-0,16%\n1,74%\n11,41%\n23,65%\n4,64%\n10.98%\n"
# print(str.replace("\n", ""))
# l = str.split("\n")
#
# print("name", l[3])
# print("1 mouth", l[7])
# print("YTD", l[8])
# print("3 years", l[10])

from tkinter import *
import tkinter.messagebox as msgbox
import requests
from bs4 import BeautifulSoup
import openpyxl

def update_data():
    try:
        # получаем HTML-код страницы и парсим данные
        response = requests.get(url)
        if response.status_code == 200:
            html_code = response.content
            soup = BeautifulSoup(html_code, 'html.parser')
            table = soup.find('table', {'id': 'cross_rate_markets_stocks_1'})
            data = []
            for row in table.find_all('tr'):
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols[1:])

            # записываем данные в файл Excel
            wb = openpyxl.load_workbook("statistics.xlsx")
            ws = wb["Статистика"]
            for i, row in enumerate(data):
                for j, value in enumerate(row):
                    ws.cell(row=i+1, column=j+1, value=value)
            wb.save("statistics.xlsx")
            msgbox.showinfo("Успех", "Данные успешно обновлены!")
        else:
            msgbox.showerror("Ошибка", "Не удалось получить HTML-код страницы.")
    except:
        msgbox.showerror("Ошибка", "Не удалось обновить данные.")



url = "https://ru.investing.com/equities/"
root = Tk()
root.title("Статистика")
root.geometry("300x100")
btn_update_all = Button(root, text="Обновить все", command=update_data)
btn_update_all.pack(pady=10)

# запускаем приложение
root.mainloop()