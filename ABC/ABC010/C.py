import math
txa, tya, txb, tyb, t, v = map(int, input().split())
n = int(input())
xy = [tuple(map(int,input().split())) for i in range(n)]
dis_a = [(x-txa, y-tya) for x, y in xy]
dis_b = [(txb-x, tyb-y) for x, y in xy]
# l_a = []
# l_b = []
l = []
for (x, y), (xb, yb) in zip(dis_a, dis_b):
    # l_a.append(math.sqrt(x**2 + y**2))
    # l_b.append(math.sqrt(xb**2 + yb**2))
    l.append(math.sqrt(x**2 + y**2)+math.sqrt(xb**2 + yb**2))
# print(l_a)
# print(l_b)
# print(l)
# print(dis_a)
# print(xy)
for length in l:
    if length <= v*t:
        print('YES')
        exit()
print('NO')