s = "Mama Mila ramy!"
print(s[0])
print(s[7:])
print(s[0:2])
print(s[::2])   #извелкается срез с шагом 2
print(s[:2])
print(s.split(" "))
s = s[0:-1] + " i okno!"
print(s)
s1 = "Mama Mila ramy i okno poka ti spal"
s51 = (s1.split())
print(s1.split(), "для позиционки")
print(s1.split("o"))
s2 = "400300200100"
print(s2.split("00"))
print("-".join(s1))
print("-".join(s2))
print("".join(s51))
print(s2.find("0"))  #находит символ и выдает его индекс первый по списку. Если не находит возвращает -1
print(s1.find("ramy"))
print(s1.find("test"))
print(s1.find("a", 4))   #с какого индекса начинаем искать
print(s1.replace("Mama", "Sanya"))  #первое заменяет на второе
s5 = "Dolgno bit vash rost - {}, s takim vesom {}" # №можно нумеровать вставки переменных
print(s5.format(198, 95))
s6 = "ti bil vesma yspeshnim v svoi {1}, tak kak y4ila {2}. I eto bilo v {0}"
print(s6.format(1986, 20, 10))
s7 = "ti bil vesma yspeshnim v svoi {vozrast}, tak kak y4ila {let}. I eto bilo v {god}"
print(s7.format(god ="1986",let = "10", vozrast = "20"))
print("{1:.2f} {0:.3f}".format(3.33333, 10/6))
print(s1.lower())   #все маленькими
print(s1.upper())    #все большими
print(s1.isupper())   #проверяет булит большой символ
print(s1.islower())   #проверяет булит маленький символ
print(s2.center(30))  #по цеентру с обоиз сторон 30 пробелов
print(s2.isdigit())  # проверка на цифру
print(s7.title())  # каждое новое слово с болшой буквы
print(s1.count("a")) # количество вхождений в строку