import math
n = int(input())
t = input()

s = '110'*(math.ceil(n/3)+1)
idx_1 = 0

if t == '1':
    print(int(2*1e10))
    exit()

while True:

    if ''.join(t)==s[idx_1:idx_1+n]:
        break

    if idx_1>=3:
        print(0)
        exit()
    idx_1 += 1


print(int((3*1e10-(idx_1)-n))//3+1)