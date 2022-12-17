# param = {
#     "email": login,
#     "password": password,
#     "rememberMe": "true",
#     "twoFactorCode": "",
#     "site": "https://www.upperdeckepack.com/",
#     "platform": "ePack"
# }
# print(param)
# headers = {
#
# }

VOWELS = "aeiouy"

def translate(phrase):
    human_phrase = []
    i = 0

    while i < len(phrase):
        human_phrase.append(phrase[i])
        if phrase[i] in VOWELS:
            i += 3
        elif phrase[i] == ' ':
            i += 1
        else:
            i += 2
    print(human_phrase)
    return ''.join(human_phrase)







    print(l)
    # print(l2)
    print(text2)



text = "hieeelalaooo"
res = translate(text)
print(res)