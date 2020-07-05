n = int(input())
a = list(map(int, input().split()))
b = [i for i in range(1, n+1)]
c = zip(a, b)
c = sorted(c, reverse=True, key=lambda x: x[0])
for _, i in c:
    print(i)