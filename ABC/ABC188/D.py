#いもす法の座標圧縮
n, c = map(int, input().split())

abc = []
ab = []
for _ in range(n):
    a, b, cost = map(int, input().split())
    ab.append(a)
    ab.append(b+1)
    abc.append([a, b+1, cost])

ab = sorted(list(set(ab)))
l = len(ab)

indexing = [[ab[i], i] for i in range(l)]
indexing = dict(indexing)

d = [0]*(l+1)
for a, b, cost in abc:
    a, b = indexing[a], indexing[b]
    d[a] += cost
    d[b] -= cost

#print(d)
for i in range(l):
    d[i+1] += d[i]
#print(d)

ans = 0
for i in range(l-1):
    if d[i] < c:
        ans += d[i]*(ab[i+1]-ab[i])
    else:
        ans += c*(ab[i+1]-ab[i])

print(ans)