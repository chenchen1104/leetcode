# 编程之美2.7将字符串向右循环移动 k 位。
# s = "abcd123" k = 3
# Return "123abcd"

s = "asgsdsgsdg23"
k = 3
ss = s + s
l = len(s)
print(ss[l - k:l - k + l])
