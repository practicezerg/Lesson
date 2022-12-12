"""Simple, given a string of words, return the length of the shortest word(s).
String will never be empty and you do not need to account for different data types."""



def find_short(s):
    l = s.split()
    l2 = []
    for i in l:
        num_i = len(i)
        l2.append(num_i)
    print(l2)
    g = min(l2)
    return g



s = "turns out random test cases are easier than writing out basic ones"
s_res = find_short(s)
print(s_res)
