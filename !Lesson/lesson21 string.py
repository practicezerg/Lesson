import string
s = "Mama Mila ramy!"
print(s[0])
print(s[7:])
print(s[0:2])   # последний ограничитель среза не входит в сам срез
print(s[::2])   #извелкается срез с шагом 2
print(s[:2])
print(s.split(" "))
s1 = "Mama Mila ramy i okno poka ti spal"
print(s1[::-1], "[start:stop:step]")
s = s[0:-1] + " i okno!"
print(s)
s51 = (s1.split())
print(s1.split(), "/// для позиционки")
print(s1.split("o"))
s2 = "400300200100"
print(s2.split("00"))
print("-".join(s1))
print("-".join(s2))
print("".join(s51))
print(s2.find("0"))  #находит символ и выдает его индекс первый по списку. Если не находит возвращает -1
print(s1.find("ramy"), "/// ну ка покажи")
print((s1[s1.find("ramy")::]), "/// двойная вкладка ищет слово целиком")
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
print(s1.islower(), "проверяет булит маленький символ")
print(s2.center(30))  #по цеентру с обоиз сторон 30 пробелов
print(s2.isdigit())  # проверка на цифру
print(s7.title())  # каждое новое слово с болшой буквы
print(s1.count("a"), "//// количество вхождений в строку") # количество вхождений в строку
s19 = "ba"
print(s19.isalpha())  # проверка на букву
s20 = "fffffff34433.112"
print(s20.lstrip("f34."), "//// убирает символы с левой стороны")
print(s20.rstrip("34.112"), "//// убирает символы с правой стороны")
s21 = "\tnasdasda\n\n\t"
print(s21)
print(s21.strip()) #убирает все табуляции и подобные вещи
num = 5
s22 = f'Start\t{num+12:15}{num+5:10}{num+1:5}\nStart\t{num+5:15}{num+7:10}{num+2:5}'
print(s22) # делает вывод таблицизированным. Выравнивая строки. Что бы первые тоже были выравнены из выставляем отдельной переменной, если требуется
print(s6.capitalize(), " ///// Ставит паервую букву заглавной")
print(s1.swapcase(), "//// Меняет тип букв с маленьких на большие и наоборот")
print(s5.startswith("Dolgno")," ///// Проверка на то, начинается или заканчивается ли строка на определенные символы")
print(s5.endswith("Dolgno")," ///// Проверка на то, начинается или заканчивается ли строка на определенные символы")
print(s1.endswith("spal")," ///// Проверка на то, начинается или заканчивается ли строка на определенные символы")
s5151 = "=f02= =werwdsf[]="
print(s5151.strip("="), "//// подрезает в начале и конце строки")
print(s1.isalnum() , "Метод isalnum() возвращает True, если все символы в строке являются буквенно-цифровыми (либо алфавитами, либо цифрами). Если нет, возвращается False.")
print(s2.isalnum())
print(string.ascii_uppercase, "//// Все большие буквы алфавита")
print(string.ascii_letters,"//// Все буквы")
print(string.ascii_lowercase,"//// Все маленькие буквы")
print(string.digits, "//// пвсе цифры")
print(string.printable , "//// всю клавиатуру")