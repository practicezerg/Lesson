def finalValueAfterOperations(operations):
    X = 0
    for i in operations:
        if i == "--X" or i == "X--":
            X -= 1
        if i == "++X" or i == "X++":
            X += 1
    return X





operations = ["--X","X++", "X++"]
X = finalValueAfterOperations(operations)
print(X)