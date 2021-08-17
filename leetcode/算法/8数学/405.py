num = -1
if num == 0:
    print('0')
ret = []
template = '0123456789abcdef'
for _ in range(8):
    ret.append(template[num % 16])
    num //= 16
print(''.join(ret[::-1]).lstrip('0'))
