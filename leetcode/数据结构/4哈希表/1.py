nums = [2, 7, 11, 15]
target = 9
hashmap = {}
for index, num in enumerate(nums):
    hashmap[num] = index
print(hashmap)
for i, num in enumerate(nums):
    # j为值target - num对应的键
    j = hashmap.get(target - num)
    if j is not None and i != j:
        print([i, j])
