import re

s = "osdf!fdsofsd aa ! d4asda 11s 1 tow free</m б  sd22  = - !!! sd-sd -asdfaas  tram,vaim mam, tyt"

s1 = "Well you need this work"
s2 = "AD 1234AD AD AD"

print(re.match("AD" , s2) , "//// В начале строки")
print(re.search("AD" , s2) , "//// Все вхождения в строку, но первое найденное")
result = re.search("AD" , s2)
print(result[0], "//// Выводит сами символы которые искали")
print(re.findall("AD", s2), "/// находит все вхождения и формирует их в лист")
print(re.split(" ", s2), "/// находит все встречающиеся аргументы и  по ним формирует лист")
print(re.split("!", s), "/// находит все встречающиеся аргументы и  по ним формирует лист")
print(re.split("!", s, maxsplit=2), "/// maxsplit задается сколько первых вхождений разобьет, а дальше одной строкой")
print(re.sub("AD", "^_^", s2), "/// первый аргумент что ищет и будет заменять, второй что будет вставлять, 3 строка")
print(re.fullmatch("AD 1234AD AD AD", s2), "/// Проверяет является весь шаблон является ли строчкой")