x, y, a, b = map(int, input().split())
ans = 0
a_s = [x]

i = 1
count = -1
less_count = 0

while i <= 61 and a_s[-1]<y:
    less_count = i-1
    a_s.append(a_s[i-1]*a)

    if a_s[-1]-a_s[-2]>b:
        count = i-1
        break
    i += 1

if count == -1:
    count = less_count

ans += count
x = x*(a**count)

if x+b<y:
    ans += (y-x-1)//b

print(ans)