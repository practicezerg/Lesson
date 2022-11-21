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


def checkio(num):  # 1 < num < 1000
    num_str = str(num)
    x = int(num_str[0])
    y = int(num_str[1])
    z = int(num_str[2])




    #
    # if num == 100:
    #     return HUNDRED
    # if 20 <= num <= 99:
    #     y = int(num_str[1])
    #     return OTHER_TENS[x-2]+" "+FIRST_TEN[y-1]
    # if 10 <= num <= 19:
    #     y = int(num_str[1])
    #     return SECOND_TEN[y]
    # if 1 <= num <= 9:
    #     return FIRST_TEN[num-1]
    # if 101 <= num <= 109:
    #     z = int(num_str[2])
    #     return "One "+ HUNDRED +" and "+ FIRST_TEN[z-1]
    # if 110 <= num:
    #     z = int(num_str[2])
    #     return





num = 110
answer = checkio(num)
print(answer)