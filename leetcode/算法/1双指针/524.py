s = "abpcplea"
dictionary = ["ale","apple","monkey","plea"]
longestword = ""
for d in dictionary:
    l1 = len(longestword)
    l2 = len(d)
    if l1 > l2 or (l1 == l2 and longestword < d):
        continue
    i = 0
    j = 0
    while i < len(s) and j < len(d):
        if s[i] == d[j]:
            j += 1
        i += 1
    if j == len(d):
        longestword = d
print(longestword)
