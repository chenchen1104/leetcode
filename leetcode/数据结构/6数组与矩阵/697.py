# 因为符合条件的可能有多个，即多个不同的数在原数组中出现次数相同。
# 所以为了找到这个子数组，我们需要统计每一个数出现的次数，同时还需要统计每一个数第一次出现和最后一次出现的位置。


nums = [1, 2, 2, 3, 1]
dict = {}
n = len(nums)
for i in range(n):
    if nums[i] in dict:
        dict[nums[i]][0] += 1
        dict[nums[i]][2] = i
    else:
        dict[nums[i]] = [1, i, i]
maxNum = minLen = 0
for count, left, right in dict.values():
    if maxNum < count:
        maxNum = count
        minLen = right - left + 1
    elif maxNum == count:
        if minLen > (right - left + 1):
            minLen = right - left + 1

print(minLen)
