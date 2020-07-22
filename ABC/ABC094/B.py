n, m, x = map(int, input().split())
a = list(map(int, input().split()))
root = [0]*n
for i in a:
    root[i] += 1
print(min(sum(root[:x+1]), sum(root[x:])))
