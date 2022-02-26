n, k = map(int, input().split())
a = list(map(int, input().split()))
ai = [[j, i] for i, j in enumerate(a)]
ai = sorted(ai, key=lambda x: x[0])

p = k//n
k -= p*n
ans = [p+1]*k + [p]*(n-k)
ans, ai = zip(*sorted(zip(ans, ai), key=lambda x: x[1][1]))

print("\n".join(map(str, list(ans))))

# N, K = map(int,input().split())
# a = list(map(int,input().split()))

# class C:
#   def __init__(self, i):
#     self.id = i
#   def __lt__(self, other):
#     return a[self.id] < a[other.id]

# order = [C(i) for i in range(N)]
# order.sort()

# answer = [K // N for i in range(N)]
# for i in range(K % N):
#   answer[order[i].id] += 1
# for x in answer:
#   print(x)
