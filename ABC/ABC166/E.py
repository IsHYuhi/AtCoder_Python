n = int(input())
a = list(map(int,input().split()))

dic = dict()
for i, j in enumerate(a, start=1):
    if dic.get(i-j):
        dic[i-j] += 1
    else:
        dic[i-j] = 1

ans = 0
for i, j in enumerate(a, start=1):
    if dic.get(i+j):
        ans += dic[i+j]

print(ans)