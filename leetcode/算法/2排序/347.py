import collections
import heapq

nums = [4, 3, 1, 6, 8, 2, 4, 9, 2]
k = 3
# 统计每个数字出现的次数
counter = collections.Counter(nums)
h = []
for key, val in counter.items():
    print(h)
    print(key, val)
    heapq.heappush(h, (val, key))
    if len(h) > k:
        heapq.heappop(h)

print([x[1] for x in h])
