n = int(input())
a = list(map(int, input().split()))
a = [(i, j) for i, j in enumerate(a, start=1)]
a.sort(key=lambda x: x[1])
a = [str(i) for i, j in a]
print(' '.join(a))
