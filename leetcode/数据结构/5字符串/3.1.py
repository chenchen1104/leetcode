# 编程之美3.1：给定两个字符串 s1 和 s2，要求判定 s2 是否能够被 s1 做循环移位得到的字符串包含。
# s1 进行循环移位的结果是 s1s1 的子字符串，因此只要判断 s2 是否是 s1s1 的子字符串即可。

s1 ="AABCD"
s2 = "CDAA"
s1s1=s1+s1
if s2 in s1s1:
    print(True)
else:
    print(False)

