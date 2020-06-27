S = input()
T = input()
ans = 0
for i, j in zip(S,T):
    if i!=j:
        ans += 1
print(ans)