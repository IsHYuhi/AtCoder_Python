n = int(input())
a = list(map(int, input().split()))

cost = [0]*n
cost[1] = abs(a[0]-a[1])

for i in range(2, n):
    one = abs(a[i]-a[i-1])
    two = abs(a[i]-a[i-2])
    cost[i] += min(cost[i-1]+one, cost[i-2]+two)

print(cost[-1])