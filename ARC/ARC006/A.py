e = list(map(int, input().split()))
b = int(input())
l = list(map(int, input().split()))


if e == l:
    print(1)
    exit()

count = 0
for i in range(6):
    if l[i] in e:
        count += 1

if count == 5 and b in l:
    print(2)

else:
    ans = 8-count if count>=3 else 0
    print(ans)
