N, Q = map(int, input().split())
S = input()
t = [0] * (N + 1)
lr = [tuple(map(int, input().split())) for _ in range(Q)]
for i in range(N):
    t[i + 1] = t[i] + (1 if S[i : i + 2] == 'AC' else 0)
for l, r in lr:
    print(t[r-1] - t[l-1])