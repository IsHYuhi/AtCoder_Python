X, N = map(int,input().split())
Ps =  set(map(int, input().split()))
for i in range(N+1):
    if (X-i) not in Ps:
        print(X-i)
        exit()
    elif (X+i) not in Ps:
        print(X+i)
        exit()
