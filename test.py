import requests


def max_digit(value):
    l = []
    value = str(value)
    for i in value:
        l.append(i)
    print(l)
    return int(max(l))




value = 0
res = max_digit(value)
print(res)
params = {
        "chat_id": chat_id,
        "text": res
    }
responce = requests.get('https://api.telegram.org/bot' + token + '/sendMessage', params=params)