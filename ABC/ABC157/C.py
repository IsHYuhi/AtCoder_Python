n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
start = 10**(n-1) if n>1 else 0
for i in range(start, 1000):
    count = 0
    for s, c in sc:
        if len(str(i))>=s:
            if int(str(i)[s-1])==c:
                count += 1
            else:
                break
    if count == m:
        print(i)
        exit()
print(-1)