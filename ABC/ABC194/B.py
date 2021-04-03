n = int(input())

ab = [list(map(int, input().split())) for _ in range(n)]
ab.sort(key=lambda x: x[0])
a, b = ab.pop(0)
ab.sort(key=lambda x: x[1])
_, c = ab.pop(0)
print(min(a+b, max(a,c)))
