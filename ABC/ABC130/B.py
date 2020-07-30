n, x = map(int, input().split())
l = list(map(int, input().split()))
dim1 = 0
for i in range(n):
    dim1 = dim1 + l[i]
    if dim1 > x:
        print(i+1)
        exit()
print(n+1)
