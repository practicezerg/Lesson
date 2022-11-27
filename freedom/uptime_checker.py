import telnetlib
import time

def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def pass_txt():
    open_file = open("passwords for freedom.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    password = slovo_test[1].replace("\n", "")
    return password

# hn-prlen148-sw05.vrn.ru
# https://nic2.vrn.ru/swfirmware/   тут можно глянуть аптаймы
user = "admin"
sw = input("Введите домен свитча =  ")
password = pass_txt()
sw = sw.replace(" ", "")  #таким образом режем пробелы
tn = telnetlib.Telnet(sw)
tn.read_until(b"login:")
tn.write(to_bytes(user))
if password:
    tn.read_until(b"Password:")
    tn.write(to_bytes(password))
time.sleep(3)
tn.write(to_bytes("sh ver"))
time.sleep(3)
info_sw = tn.read_until(b"minutes")
info_sw = info_sw.decode("utf-8")
print(info_sw)
print(type(info_sw))
print(info_sw.find("Uptime"))
print(info_sw.find("days"))
print(info_sw[info_sw.find("Uptime"): info_sw.find("days")])
info_uptime = info_sw[info_sw.find("Uptime"): info_sw.find("days")]
res_uptime_week = info_uptime[info_uptime.find("is")+3: info_uptime.find("w")]
print(res_uptime_week)
res_uptime_week = int(res_uptime_week)
if res_uptime_week >= 8:
    tn.write(to_bytes("write"))
    time.sleep(3)
    tn.write(to_bytes("yes"))
    time.sleep(3)
    tn.write(to_bytes("reload"))
    time.sleep(3)
    tn.write(to_bytes("yes"))
    print("script end")
else:
    print("Uptime only {}".format(info_sw[info_sw.find("Uptime"):]))