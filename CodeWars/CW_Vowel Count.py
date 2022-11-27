"""Return the number (count) of vowels in the given string.
We will consider a, e, i, o, u as vowels for this Kata (but not y).
The input string will only consist of lower case letters and/or spaces."""


def get_count(a):
    count = 0
    count_vowels = ['a', 'e', 'i', 'o', 'u']
    for i in a:
        if i in count_vowels:
            count += 1
    return count


a = "ehoerherpehe pwerpiodsfklwerwb ncmvclfmsodhfwierhwqwe"
count = get_count(a)
print(count)