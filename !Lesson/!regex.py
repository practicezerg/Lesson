import re

s = "osdf!fdsofsd aa ! d4asda 11s 1 tow free</m б  sd22  = - !!! sd-sd -asdfaas  tram,vaim mam, tyt"

s1 = "Well you need this work"
s2 = "AD 1234AD AD AD"
s3 = "55!212werweO+GJDOFG sdfs 75+wer+w+sss2342666+ 77 ---     +3233+ 3331111 441 5555g5555"

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
result = re.search(r'75.w', s3)
print(result, "точка заменяет один любой символ, несколько точек - несколько символов")
result = re.search(r'7\d', s3)
print(result, " \d любую цифру")
result = re.search(r'7\D', s3)
print(result, " \D любую символ кроме цифры")
result = re.search(r'7\s', s3)
print(result, " \s любой пробельный символ, \S любой не пробелный символ")
result = re.search(r'\W', s3)
print(result, " \w любую буква цифра или _ , \W любая не буква и не цифра и не _ ")
result = re.search(r'\Ber', s3)
print(result, " \b начало любого слова , \B в середине слова ")
result = re.search(r'\d+', s3)
print(result, " \d* 0 или более вхождений символов в это слово , \d+ одно или более вхождений ")
result = re.search(r'[dfklfh]', s3)
print(result, " [] диапазоy если встретиься одна из букв , [4-6] диапазон если встретиться одна из цифр в этом диапазоне ")
result = re.search(r'[^4-9]', s3)
print(result, " [^] говрит нам исключая этот диапазон ")
result = re.search(r'R|r', s3)
print(result, " | говрит нам вывести либо это либо это")
result = re.search(r'\d{3}', s3)
print(result, " {3} говрит нам о количествах повторений")
result = re.search(r'\d{2,3}', s3)
print(result, " {3} говрит нам о количествах повторений от 2 до 3")
result = re.search(r'\d{4,}', s3)
print(result, " {4,} говрит нам о количествах повторений не менее 4")
result = re.search(r'\d{,5}', s3)
print(result, " {,5} говрит нам о количествах повторений не более 5")
s4 = "Привет! Как у тебя дела? Все нормально, но я люблю есть сыр. Каждый день в 10 часов"
result = re.findall(r'[цкнгшщзхждлрпвфчсмтбЦКНГШЩЗХФВПРЛДЖЧСМТБ]\w+',s4)
print(result,"вывод всех слов начинающихся на большую согласную")