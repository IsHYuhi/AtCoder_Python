N = int(input())
As = list(map(int,input().split()))
sum = 1
if 0 in As:
    print(0)
    exit()
for i in As:
    sum *=i
    if sum>10**18:
        sum = -1
        break
print(sum)