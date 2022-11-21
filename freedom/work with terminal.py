import telnetlib
import time
import datetime

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

sw = "hn-test-tp-3470-koles.vrn.ru"
user = "admin"
password = ""  #написать передачу пароля из файла gitignore
port = 11
print(sw)
tn = telnetlib.Telnet(sw)
tn.read_until(b"login:")
tn.write(to_bytes(user))
if password:
    tn.read_until(b"Password:")
    tn.write(to_bytes(password))
time.sleep(3)
tn.write(b"config\n")
time.sleep(3)
tn.write(b"interface ethernet 1/0/2\n")
time.sleep(3)
tn.write(b"no speed-duplex\n")
time.sleep(3)
tn.write(b"bandwidth control 215040 both\n")
time.sleep(3)
tn.write(b"write\n")
time.sleep(3)
tn.write(b"yes\n")
time = datetime.datetime.now()
time2 = str(time)
time2 = time2.replace(":", "-").replace(".", "--")
print(time2)
my_file = open("{}.txt".format(time2), "w+")
my_file.write("{} + {}port + tarif".format(sw, port))
my_file.close()
print("script end")


# zz = subprocess.check_output(["ping", "hn-test-tp-3470-koles.vrn.ru"], timeout=5).decode("cp866")

# print(zz)


# 10.255.119.214
# hn-test-tp-3470-koles.vrn.ru





# sw = input("Введите домен свитча == ")
# sw = sw.replace(" ","")  таким образом режем пробелы

# zz = subprocess.run(["ping", "{}".format(sw[0])], timeout=5)
# zz = subprocess.check_output(["ping", "{}".format(sw[0])], timeout=5)
# subprocess.run(["ping", "hn-rost46-7-sw04.vrn.ru"], timeout=5)
# gg = open("terminal.txt", "w")
# gg.write(zz)
# encoding="utf-8"
# process = subprocess.run(['ping', 'google.com'], timeout=5)