n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))
ans = [0]*3
for i in p:
    if i <= a:
        ans[0] += 1
    elif a < i <= b:
        ans[1] += 1
    else:
        ans[2] += 1

print(min(ans))
