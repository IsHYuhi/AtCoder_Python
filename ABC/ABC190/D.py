N = int(input())
while N % 2 == 0:
    N //= 2
sq = int(N ** 0.5)
ans = sum(N % i == 0 for i in range(1, sq + 1)) * 2 - (sq * sq == N)
print(ans * 2)