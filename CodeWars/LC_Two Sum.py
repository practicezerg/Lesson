nums = [3,2,4]
target = 6

for i in nums:
    if i < target:
        x = target - i
        # print(x, "=x")
        g = nums.index(x)
        z = nums.count(x)
        # print(z, "= z")
        # print(g, " = g")
        if g != i and z == 1:
            print(nums.index(i), g)




        # if g >= 0:
        #     p = nums.count(i)
        #     print(p, g)


