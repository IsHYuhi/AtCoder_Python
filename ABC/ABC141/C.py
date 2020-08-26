n, k, q = map(int, input().split())
a = [int(input()) for i in range(q)]
p = [k-q]*n

for i in a:
    p[i-1] += 1

for i in p:
    if i>0:
        print('Yes')
    else:
        print('No')
