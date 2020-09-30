N, M = map(int,input().split())
Hs = list(map(int,input().split()))
L = [[] for i in range(N)]
count = 0
for i in range(M):
    A, B = map(int,input().split())
    (L[A-1]).append(Hs[B-1])
    (L[B-1]).append(Hs[A-1])
for i in range(N):
    if not L[i]:
        count+=1
        continue
    if Hs[i] > max(L[i]):
        count += 1
print(count)
