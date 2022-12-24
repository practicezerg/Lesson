"""You are given an array items, where each items[i] = [typei, colori, namei] describes the type, color, and name of the ith item. You are also given a rule represented by two strings, ruleKey and ruleValue.
The ith item is said to match the rule if one of the following is true:
ruleKey == "type" and ruleValue == typei.
ruleKey == "color" and ruleValue == colori.
ruleKey == "name" and ruleValue == namei.
Return the number of items that match the given rule."""

def countMatches(List, ruleKey, ruleValue):
    res = 0
    if ruleKey == "color":
        for i in List:
            if i[1] == ruleValue:
                res += 1
    if ruleKey == "type":
        for i in List:
            if i[0] == ruleValue:
                res += 1
    if ruleKey == "name":
        for i in List:
            if i[2] == ruleValue:
                res += 1
    return res




List = [["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
ruleKey = "type"
ruleValue = "phone"
res = countMatches(List, ruleKey, ruleValue)
print(res)