import telnetlib
import time
import datetime

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

# sw = "hn-test-tp-3470-koles.vrn.ru"
sw = input("Введите домен свитча =  ")
sw = sw.replace(" ","")  #таким образом режем пробелы
user = "admin"
password = ""  #написать передачу пароля из файла gitignore
port_input = input("Введите номер порта клиента =  ")
port = "interface ethernet 1/0/{}\n".format(port_input)
print("Применяю изменения к ", sw)
tn = telnetlib.Telnet(sw)
tn.read_until(b"login:")
tn.write(to_bytes(user))
if password:
    tn.read_until(b"Password:")
    tn.write(to_bytes(password))
print("Script started.....")
time.sleep(3)
tn.write(b"config\n")
time.sleep(3)
tn.write(to_bytes(port))
time.sleep(3)
tn.write(b"speed-duplex auto 10 100\n")
time.sleep(3)
tn.write(b"no bandwidth control\n")
time.sleep(3)
tn.write(b"write\n")
time.sleep(3)
tn.write(b"yes\n")
time = datetime.datetime.now()
time2 = str(time)
time2 = time2.replace(":", "-").replace(".", "--")
print(time2)
my_file = open("{}.txt".format(time2), "w+")
my_file.write("{} + {} порт + Тариф 100".format(sw, port_input))
my_file.close()
print("script end")

