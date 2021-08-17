nums = [1, 2, 2, 1]
dict = {}
for i in nums:
    if i in dict.keys():
        dict[i]+=1
    else:
        dict[i]=1
maxLen = 0
for j in dict.keys():
    if j + 1 in dict.keys():
        maxLen = max(maxLen, dict[j] + dict[j + 1])
print(maxLen)
