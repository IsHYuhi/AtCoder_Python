n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]

mn = float('inf')
mx = 0
ab.sort(key=lambda x: x[0])

print(ab[-1][1]+ab[-1][0])