data = input()
d = data[1:len(data) - 1]
nums = list(map(int, d.split(',')))
target = int(input())

# lens = len(nums)
# j = -1
# for i in range(lens):
#     if (target - nums[i]) in nums:
#         if (nums.count(target - nums[i]) == 1)&(target - nums[i] == nums[i]):#如果num2=num1,且nums中只出现了一次，说明找到是num1本身。
#             continue
#         else:
#             j = nums.index(target - nums[i],i+1) #index(x,i+1)是从num1后的序列后找num2
#             break
# if j>0:
#     print([i,j])
# else:
#     print([])


# 此种解法只有在数组中没有重复数字时才可以使用
newnums = sorted(nums)
lens = len(nums)
i = 0
j = lens - 1
while i <= j:
    if newnums[i] + newnums[j] == target:
        print([nums.index(newnums[i]), nums.index(newnums[j])])
        break
    elif newnums[i] + newnums[j] < target:
        i += 1
    else:
        j -= 1

