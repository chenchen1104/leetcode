s = "00110011"
counts = []
ptr = 0
count = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count += 1
    else:
        counts.append(count)
        count = 1
counts.append(count)
ans = 0
for i in range(1, len(counts)):
    ans += min(counts[i], counts[i - 1])
print(ans)
