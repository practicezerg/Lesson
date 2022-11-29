"""Вам дана строка и два маркера (начальный и конечный). Вам необходимо найти текст, заключенный между двумя этими маркерами. Но есть несколько важных условий.

Это упрощенная версия миссии Between Markers .

Начальный и конечный маркеры всегда разные.
Начальный и конечный маркеры всегда размером в один символ.
Начальный и конечный маркеры всегда есть в строке и идут один за другим.
Input: Три аргумента. Все строки. Второй и третий аргументы это начальный и конечный маркеры.

Output: Строка.

Пример:

assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"
Как это используется: Может использоваться для парсинга небольшой верстки.

Предусловия: Не может быть более одного маркера одного типа."""
def between_markers(text: str, start: str, end: str) -> str:
    for i in text:
        if i == start:
            s = text.index(i)
        if i == end:
            e = text.index(i)
    return text[s+1 : e]