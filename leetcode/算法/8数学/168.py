columnNumber = 701
excellist = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
data = []
while columnNumber > 0:
    data.append(columnNumber % 26)
    columnNumber = columnNumber // 26
    print(data,columnNumber)
data.reverse()
print(data)
excelname = ""
for i in data:
    excelname += excellist[i - 1]
print(excelname)
