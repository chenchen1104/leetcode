nums = [4, 1, 2, 1, 2]
ret = 0
for n in nums:
    ret = ret ^ n
    print(ret)
