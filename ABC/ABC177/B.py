s = list(input())
t = list(input())
ans = float('inf')

for i in range(len(s)-len(t)+1):
    count = 0
    for j in range(len(t)):
        if not s[i+j]==t[j]:
            count += 1
    ans = min(ans, count)
print(ans)
