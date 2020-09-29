n, k = map(int, input().split())
h = list(map(int, input().split()))

h.sort(reverse=True)
print(sum(h[min(n,k):]))