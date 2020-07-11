n = int(input())
s = [int(input()) for _ in range(n)]
s.sort(reverse=True)
sm = sum(s)
ans = 0
while (sm - ans)%10==0 and s:
    now = s.pop()
    ans += now
    if(sm - now)%10!=0:
        ans = now
        break

print(sm - ans)
