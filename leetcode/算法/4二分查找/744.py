letters=["c", "f", "j"]
target="j"
l, r, ans = 0, len(letters)-1, -1
while l <= r:
    print(l,r)
    mid = (r + l) // 2
    if letters[mid] <= target:
        l = mid + 1
    else:
        ans = mid
        r = mid - 1

print(letters[ans])