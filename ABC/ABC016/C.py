N, M = map(int, input().split())
relation = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    relation[A].append(B)
    relation[B].append(A)

def count_relation(re, se, n, d):
    for i in re:
        if i == se:
            continue
        d = d| set(relation[i])
    d = d - set(re)
    if se in d:
        return len(d)-1
    return len(d)

for i in range(1,N+1):
    print(count_relation(relation[i], i, 0, set()))

