mac = "AAAA:BBBB:CCCC"

mac = mac.replace(".",":") # заменяем точку на двоеточие, чтобы все разделители были одинаковые
mac_split = mac.split(":") # разбиваем адрес на блоки по две цифры
binary_string = "" # создаем пустую строку для записи двоичного представления

for block in mac_split:
    decimal = int(block, 16) # преобразуем блок из 16-ричной в десятичную систему
    binary = bin(decimal)[2:].zfill(8) # преобразуем десятичное число в двоичное и добавляем недостающие нули в начало
    binary_string += binary # добавляем двоичное представление блока к общей строке

print(binary_string) # выводим результат на экран



ip = "192.168.3.1"
ip_split = ip.split(".")
teamplate = """
IP address:
{0:10}  {1:10}  {2:10}  {3:10}
{0:010b}  {1:010b}  {2:010b}  {3:010b}
"""
print(type(ip_split[0]))
print(teamplate.format(int(ip_split[0]), int(ip_split[1]), int(ip_split[2]), int(ip_split[3])))