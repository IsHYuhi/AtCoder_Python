n = int(input())
h = list(map(int, input().split()))

for i in range(1,n):
    if h[i-1]-h[i]>0:
        print('No')
        exit()
    elif h[i-1]-h[i] <= -1:
        h[i] -= 1
print('Yes')

