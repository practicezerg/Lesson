FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
SECOND_TEN = [
    "ten",
    "eleven",
    "twelve",
    "thirteen",
    "fourteen",
    "fifteen",
    "sixteen",
    "seventeen",
    "eighteen",
    "nineteen",
]
OTHER_TENS = [
    "twenty",
    "thirty",
    "forty",
    "fifty",
    "sixty",
    "seventy",
    "eighty",
    "ninety",
]
HUNDRED = "hundred"


def checkio(num):
    str_num = str(num)
    print(len(str_num))
    str_num_list = []
    for i in str_num:
        str_num_list.append(i)
        print(str_num_list)
    if len(str_num) == 3:
        return HUNDRED
    elif len(str_num) == 2:
        pass
    elif len(str_num) == 1:
        if str_num_list[0] == "1":
            return FIRST_TEN[0]
        pass
    return "string"


num = 1
answer = checkio(num)
print(answer)