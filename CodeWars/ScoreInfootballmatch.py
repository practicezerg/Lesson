match = ["3:1", "2:2", "1:0", "0:1", "0:1", "1:0", "3:1", "1:3", "1:3", "1:0"]
number_game = 0
score = 0
for one_game in match:

    if one_game[0] > one_game[2]:
        score = score + 3
    elif one_game[0] < one_game[2]:
        score = score + 0
    else:
        score = score + 1
    number_game += 1
print(score)