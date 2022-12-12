"""There are n rings and each ring is either red, green, or blue. The rings are distributed across ten rods labeled from 0 to 9.
You are given a string rings of length 2n that describes the n rings that are placed onto the rods. Every two characters in rings forms a color-position pair that is used to describe each ring where:
The first character of the ith pair denotes the ith ring's color ('R', 'G', 'B').
The second character of the ith pair denotes the rod that the ith ring is placed on ('0' to '9').
For example, "R3G2B1" describes n == 3 rings: a red ring placed onto the rod labeled 3, a green ring placed onto the rod labeled 2, and a blue ring placed onto the rod labeled 1.
Return the number of rods that have all three colors of rings on them."""


def countPoints(rings):
    l = []
    num_res = 0
    x = 0
    for i in range(0, len(rings), 2):
        l.append(rings[i] + rings[i + 1])
    while x < len(rings):
        num_G = l.count(f"G{x}")
        num_R = l.count(f"R{x}")
        num_B = l.count(f"B{x}")
        if num_G == num_R == num_B:
            if num_G != 0:
                num_res += 1
        x += 1
    return num_res




rings = "B0B6G0R6R0R6G9"
#18 так как всего 9 стержней
res = countPoints(rings)
print(res)


