n, k = map(int, input().split())
a = list(map(int, input().split()))

t = 0
count = 0
visited = [0]*n
l_count = 0

for _ in range(k):
    visited[t] += count
    count += 1
    t = a[t]-1

    if visited[t] != 0:
        break

k = (k-count)%(count-visited[t])

for _ in range(k):
    t = a[t] - 1

print(t+1)
