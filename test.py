import subprocess
# encoding="utf-8"
process = subprocess.run(['ping', 'google.com'], timeout=5, encoding="ascii")
# slovo2 = []
# test_char = input("tet")
# slovo = "елочка"
# if test_char in slovo:
#     print("Есть такая буква!У вас осталось {} попыток!")
#     x = (slovo.find(test_char))
#     print(x)
#     slovo2 = slovo2.append(test_char)
#     # slovo2 = show_user_easy[0:x] + test_char + show_user_easy[x:]
#     print(type(slovo2))
#     # input_type -= 1
# else:
#     print("В задуманном мною слове нет такой буквы")
#     print("У вас осталось {} попыток!")
#     # input_type -= 1