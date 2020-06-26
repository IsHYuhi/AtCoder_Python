a = int(input())
b = int(input())

ans = abs(b-a)
ans = min(ans, abs(min(a,b)-0)+abs(max(a,b)-9)+1)
print(ans)