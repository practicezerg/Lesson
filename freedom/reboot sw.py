import telnetlib
import time


def to_bytes(line):
    return f"{line}\n".encode("utf-8")


def pass_txt():
    open_file = open("passwords for freedom.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    password = slovo_test[1].replace("\n", "")
    open_file.close()
    return password


sw = ["hn-test-tp-3470-koles.vrn.ru", "10.255.119.214"]
user = "admin"
password = ""
port = 2
print(sw[0])
tn = telnetlib.Telnet("hn-test-tp-3470-koles.vrn.ru")
tn.read_until(b"login:")
tn.write(to_bytes(user))
if password:
    tn.read_until(b"Password:")
    tn.write(to_bytes(password))
time.sleep(3)
tn.write(b"reload\n")
time.sleep(3)
tn.write(b"yes\n")
print("script end")
