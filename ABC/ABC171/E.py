n = int(input())
a = list(map(int, input().split()))
b=0
for i in range(n):
    b ^= a[i]
ans = []
for i in range(n):
    ans.append(b^a[i])
print(' '.join(list(map(str, ans))))
