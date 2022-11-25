import telnetlib
import time
import datetime

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

# sw = "hn-test-tp-3470-koles.vrn.ru"
sw = input("Введите домен свитча =  ")
sw = sw.replace(" ","")  #таким образом режем пробелы
user = "admin"
password = "Inter004"  #написать передачу пароля из файла gitignore
port_input = input("Введите номер порта клиента =  ")
port = "config ports {}\n".format(port_input)
print("Применяю изменения к ", sw)

tn = telnetlib.Telnet(sw)
time.sleep(3)
tn.read_until(b"username:")
tn.write(to_bytes(user))
time.sleep(3)
if password:
    tn.read_until(b"password:")
    tn.write(to_bytes(password))
print("Script started.....")
time.sleep(3)
tn.write(to_bytes("config ports {} capability_advertised 10_half 10_full 100_half 100_full 1000_full".format(port)))
time.sleep(3)
tn.write(to_bytes("config bandwidth_control {} rx_rate 537600 tx_rate 537600".format(port)))
time.sleep(3)
tn.write(b"save\n")
time.sleep(3)
tn.write(b"yes\n")
time = datetime.datetime.now()
time2 = str(time)
time2 = time2.replace(":", "-").replace(".", "--")
print(time2)
my_file = open("{}.txt".format(time2), "w+")
my_file.write("{} + {} порт + Тариф 500".format(sw, port_input))
my_file.close()
print("script end")

