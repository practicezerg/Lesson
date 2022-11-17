import subprocess
import sys

zz = subprocess.check_output(["ping", "ya.ru"], timeout=5).decode("cp866")
print(zz)



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