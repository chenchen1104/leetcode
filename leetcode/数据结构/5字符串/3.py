# 字符串翻转。
# s = "I am a student"
# Return "student a am I"

s = "I am a student"
letters = list(map(str, s.split()))
letters.reverse()
print(" ".join(letters))