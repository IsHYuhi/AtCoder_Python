s, p = map(int, input().split())

for m in range(1, 10**6+1):
    if (s-m)*m==p:
        print('Yes')
        exit()
print('No')