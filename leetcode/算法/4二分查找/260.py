import functools

nums = [1, 2, 1, 3, 2, 5]
ret = functools.reduce(lambda x, y: x ^ y, nums)
div = 1
while div & ret == 0:
    div <<= 1
a, b = 0, 0
for n in nums:
    if n & div:
        a ^= n
    else:
        b ^= n
print([a, b])
