"""This is a simplified version of Fizz Buzz mission.
You should write a function that will receive a positive integer and return:
"Fizz" if the number is divisible by 3 (3, 6, 9 ...) otherwise convert the given number to a string (2 -> "2")."""
def checkio(num):
    x = num/3
    if x == int(x):
        return "Fizz"
    else:
        return f"{num}"

num = 7
a = checkio(num)
print(a)