import heapq

n, m = map(int, input().split())
a = list(map(int, input().split()))
a = [-i for i in a]
heapq.heapify(a)

while m>0:
    c = heapq.heappop(a)
    heapq.heappush(a, -((-c)//2))
    m -= 1

ans = [-i for i in a]
print(sum(ans))