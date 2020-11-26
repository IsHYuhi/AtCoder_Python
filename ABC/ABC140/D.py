n, k = map(int, input().split())
s = input()

count = 0
for i in range(n-1):
    if s[i]==s[i+1]:
        count += 1

print(min(count+2*k, n-1))