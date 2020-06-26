from collections import Counter
N = int(input())
S = [input() for i in range(N)]
S = Counter(S)
print(max(S, key=S.get))