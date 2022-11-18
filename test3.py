import telnetlib
import time

def to_bytes(line):
    return f"{line}\n".encode("utf-8")

sw = ["hn-test-tp-3470-koles.vrn.ru", "10.255.119.214"]
user = "admin"
password = "Inter004"
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