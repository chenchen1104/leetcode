num = -7
seven = []
absnum = abs(num)
while absnum >= 7:
    seven.append(absnum % 7)
    absnum = absnum // 7
seven.append(absnum)
seven = [str(i) for i in seven]
if num >= 0:
    print("".join(seven))
else:
    seven.reverse()
    print("-" + "".join(seven))
