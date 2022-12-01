import datetime
import time
import random
from datetime import time

import requests
import json
from bs4 import BeautifulSoup


def debug_fail_for_html(result):
    open_file = open("any auth.html", "w", encoding="utf-8")
    open_file.write(result.text)
    open_file.close()


def pass_txt():
    open_file = open("pass.txt", "r", encoding="utf-8")
    slovo_test = open_file.readlines()
    login = slovo_test[0].replace("\n", "")
    password = slovo_test[1].replace("\n", "")
    return login, password

time_start = datetime.datetime.now()
session = requests.Session()
login, password = pass_txt()
print(login, password)
useragent = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 OPR/93.0.0.0"
headers = {
    "User-Agent": useragent
}
data = {
    "email": login,
    "password": password,
    "rememberMe": "true",
    "twoFactorCode": "",
    "site": "https://www.upperdeckepack.com/",
    "platform": "ePack"
}

try1 = session.post("https://www.upperdeckepack.com/auth/Auth/LoginForIdentity", data=data, headers=headers).text
arx = json.loads(try1)
token = (arx["success"]['Token'])
print(token)
data = {
    "token": token,
    "rememberMe": "true"
}
try2 = session.post("https://www.upperdeckepack.com/api/User/LoginWithToken", data=data, headers=headers).text
arx2 = json.loads(try2)
UserIdToken = arx2["success"]['userIdentity']["UserIdToken"]
print(UserIdToken)
UserAuthToken = arx2["success"]['userIdentity']['UserAuthToken']
print(UserAuthToken)
username = arx2["success"]['userIdentity']['Username']
print(username)
try3 = session.post("https://www.upperdeckepack.com/api/User/LoginVisit", headers=headers).text
try4 = session.get("https://www.upperdeckepack.com/api/transfer/GetTransferCount", headers=headers).text
try5 = session.get("https://www.upperdeckepack.com/api/User/ReloadNotifications/", headers=headers).text
try6 = session.get("https://www.upperdeckepack.com/api/User/Dashboard", headers=headers).text
print(json.loads(try6)["DashboardStatus"]["CardsOwned"], " карточек")
try7 = session.get("https://www.upperdeckepack.com/Store/", headers=headers).text
soup7 = BeautifulSoup(try7, features="html.parser")
text71 = soup7.find("div", class_="dropdown")

"""тут в этом классе
дальше есть class="dropdown-toggle btn"

не успел
сделал скрин в телеге сформировалась временная сылка на твой пак который ты выбрал
"""
# print(text71)

# https://newmsg.upperdeckepack.com//messaging/negotiate?clientProtocol=1.5&userToken=gsuo4V/3Ods16p1vnnWO5B6qQVEWOZidfVv49fnKiqo=&userAuth=sDyXTDPyt5wjO/2sN1yeJhHsYdJJimosFOzAV7RpmFA=&userName=pdsdosoaaa&connectionData=[{"name":"privatemessaginghub"},{"name":"publicmessaginghub"}]&_=1669897451951# def link_for_msg(UserToken, userAuth, username):
# &connectionData=[{"name":"privatemessaginghub"},{"name":"publicmessaginghub"}]&_=1669897451951#
#
#     b = "3D&userAuth="
#     c = "3D&userName="
#     link_for_msg = a + UserToken + b + userAuth + c + username
#     return link_for_msg
def link_try_ConnectionToken(UserIdToken,UserAuthToken,username):

    a = "https://newmsg.upperdeckepack.com//messaging/negotiate?clientProtocol=1.5&userToken="
    b = "&connectionData=[{\"name\":\"privatemessaginghub\"},{\"name\":\"publicmessaginghub\"}]&_=1909897451951"
    link_try_ConnectionToken = a + UserIdToken + "&userAuth=" + UserAuthToken + "&userName=" + username + b
    return link_try_ConnectionToken

# тут сделаем сылочку для токенов
link_try_ConnectionToken = link_try_ConnectionToken(UserIdToken,UserAuthToken,username)
print(link_try_ConnectionToken)
try8 = session.get(link_try_ConnectionToken, data=data, headers=headers).text
ConnectionToken = json.loads(try8)["ConnectionToken"]
ConnectionId = json.loads(try8)["ConnectionId"]

def link_for_msg(UserIdToken, UserAuthToken, username, ConnectionToken):
    a = "https://newmsg.upperdeckepack.com//messaging/send?transport=longPolling&clientProtocol=1.5&userToken="
    b = "&userAuth="
    c = "&userName="
    g = "&connectionToken="
    e = "&connectionData=[{\"name\":\"privatemessaginghub\"},{\"name\":\"publicmessaginghub\"}]"
    link_for_msg = a + UserIdToken + b + UserAuthToken + c + username + g + ConnectionToken + e
    return link_for_msg
link_for_msg = link_for_msg(UserIdToken, UserAuthToken, username, ConnectionToken)

print(link_for_msg)


def msg_for_forum():
    l = ["Hi somebody wanna trade?", "anybody here? Go trade!", "Go trade with me-_-?", "May be stop blank?Go trade ))",
         "Any wanna purple cards?20 purple for 1 Combinable?", "Hey wanna trade? msg me!",
         "Check may be any card need you ?",
         "Looking for UpperDeck base, any set", "All available, send an offer!", "hi be free for trade?? or blank",
         "Taking any trades doesn’t have to be anything"]
    msg_for_forum = l[random.randint(0, len(l) - 1)]
    return msg_for_forum


msg_for_forum = msg_for_forum()
# "connectionToken" - 128 символов
data3 = {
    "transport": "longPolling",
    "clientProtocol": "1.5",
    "userToken": UserIdToken,
    "userAuth": UserAuthToken,
    "userName": username,
    "connectionToken": ConnectionToken,
    "connectionData": "[{\"name\":\"privatemessaginghub\"},{\"name\":\"publicmessaginghub\"}]"
}
for_data91 = "{\"H\": \"publicmessaginghub\", \"M\": \"SendMessage\", \"A\": [\" " + msg_for_forum + "\"\", \"sports\"], \"I\": 3}"
print(for_data91)
data2 = {
    "data": for_data91,
}
try9 = session.post(link_for_msg, data=data2, headers=headers).text
print(try9)

# вывод времени работы скрипта
print(datetime.datetime.now() - time_start)