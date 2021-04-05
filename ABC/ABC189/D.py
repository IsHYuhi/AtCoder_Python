n = int(input())
oprs = [input() for _ in range(n)]
ans = 1

for i, s in enumerate(oprs[::-1], 1):
    if s == 'OR':
        ans += 2**(n-i+1)
    elif s == 'AND':
        ans *= 1

print(ans)