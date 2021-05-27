n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
imos = [0]*(10**6+2)

for a, b in ab:
    imos[a] += 1
    imos[b+1] += -1

for i in range(1, (10**6+2)):
    imos[i] += imos[i-1]

print(max(imos))
