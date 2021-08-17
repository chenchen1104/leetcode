nums = [2, 2]
dict = {}
for i in range(len(nums)):
    dict[i + 1] = 0
for i in range(len(nums)):
    if nums[i] not in dict:
        dict[nums[i]] = 1
    else:
        dict[nums[i]] += 1
m, n = 0, 0
for i in dict:
    if dict[i] == 0:
        n = i
    if dict[i] == 2:
        m = i
print([m, n])
