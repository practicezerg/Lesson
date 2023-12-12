#Необходима установка
pip install tabulate


#Сам код
from tabulate import tabulate

table = [["Sun",696000,1989100000],["Earth",6371,5973.6],
...          ["Moon",1737,73.5],["Mars",3390,641.85]]
print(tabulate(table))
-----  ------  -------------
Sun    696000     1.9891e+09
Earth    6371  5973.6
Moon     1737    73.5
Mars     3390   641.85
-----  ------  -------------

#headers создает шабку таблицы

print(tabulate(table, headers=["Planet","R (km)", "mass (x 10^29 kg)"]))
Planet      R (km)    mass (x 10^29 kg)
--------  --------  -------------------
Sun         696000           1.9891e+09
Earth         6371        5973.6
Moon          1737          73.5
Mars          3390         641.85



Если headers="firstrow", то используется первая строка данных:

>>> print ( tabulate ([[ "Name" , "Age" ],[ "Alice" , 24 ],[ "Bob" , 19 ]], 
...                headers = "firstrow" )) 
Имя Возраст 
--- --- ----- 
Алиса 24 
Боб 19



Если headers="keys", то используются ключи словаря/фрейма данных или индексы столбцов. Это также работает для массивов записей NumPy и списков словарей или именованных кортежей:

>>> print ( tabulate ({ "Name" :  [ "Alice" ,  "Bob" ], 
...                 "Age" :  [ 24 ,  19 ]},  headers = "keys" )) 
  Возраст Имя 
----- ------ 
   24 Алиса 
   19 Боб



Существует несколько способов форматирования таблицы в виде обычного текста. Третий необязательный аргумент tablefmtопределяет способ форматирования таблицы.

Поддерживаемые форматы таблиц:

Supported table formats are:

"plain"
"simple"
"github"
"grid"
"simple_grid"
"rounded_grid"
"heavy_grid"
"mixed_grid"
"double_grid"
"fancy_grid"
"outline"
"simple_outline"
"rounded_outline"
"heavy_outline"
"mixed_outline"
"double_outline"
"fancy_outline"
"pipe"
"orgtbl"
"asciidoc"
"jira"
"presto"
"pretty"
"psql"
"rst"
"mediawiki"
"moinmoin"
"youtrack"
"html"
"unsafehtml"
"latex"
"latex_raw"
"latex_booktabs"
"latex_longtable"
"textile"
"tsv"
