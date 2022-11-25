import telnetlib
import time
import datetime


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def make_log_txt():
    time = datetime.datetime.now()
    time2 = str(time)
    time2 = time2.replace(":", "-").replace(".", "--")
    print(time2)
    my_file = open("{}.txt".format(time2), "w+")
    my_file.write("{} + {} порт + Тариф 500".format(sw, port_input))
    my_file.close()
    print("script end")
    print("{} + {} порт \n Тариф {} для клиента применен".format(sw, port_input, tariff))


def qsw_100():
    tn.write(to_bytes("speed-duplex auto 10 100"))
    time.sleep(3)
    tn.write(to_bytes("no bandwidth control"))
    time.sleep(3)


def qsw_200():
    tn.write(to_bytes("no speed-duplex"))
    time.sleep(3)
    tn.write(to_bytes("bandwidth control 215040 both"))
    time.sleep(3)


def qsw_500():
    tn.write(to_bytes("no speed-duplex"))
    time.sleep(3)
    tn.write(to_bytes("bandwidth control 537600 both"))
    time.sleep(3)


user = "admin"
sw = input("Введите домен свитча =  ")
password = input("password =    ")
sw = sw.replace(" ", "")  #таким образом режем пробелы
port_input = input("Введите номер порта клиента =  ")
port = "interface ethernet 1/0/{}\n".format(port_input)
tariff = input("100/200/500=    ")
print("Применяю изменения к ", sw)
tn = telnetlib.Telnet(sw)
tn.read_until(b"login:")
tn.write(to_bytes(user))
if password:
    tn.read_until(b"Password:")
    tn.write(to_bytes(password))
time.sleep(3)
print("Script started.....")
tn.write(to_bytes("config"))
time.sleep(3)
tn.write(to_bytes(port))
time.sleep(3)
if tariff == "500":
    qsw_500()
elif tariff == "200":
    qsw_200()
elif tariff == "100":
    qsw_100()
time.sleep(3)
tn.write(to_bytes("write"))
time.sleep(3)
tn.write(to_bytes("yes"))
time.sleep(3)
make_log_txt()
