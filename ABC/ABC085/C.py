n, y = map(int, input().split())

for i in range(0, n+1):
    for j in range(0, n+1-i):
            if (n-i-j)*10000+j*5000+i*1000==y:
                print(n-i-j, j, i)
                exit()
print(-1, -1, -1)