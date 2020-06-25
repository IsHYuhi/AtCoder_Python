from collections import Counter

N, K = map(int, input().split())
S = list(input())

s_sorted = sorted(S)
t = ""

diff = 0
counter = Counter(S[:1])
print(counter)
counts = sum(counter.values())
print(counts)

for i in range(N):
    # t + c が可能か調べる
    for c in s_sorted:
        # t + c の中で元の位置と違う文字の数
        diff1 = diff + (c != S[i])
        # まだ使ってない文字の中で元の位置と違う文字の数
        diff2 = counts - (counter[c] > 0)

        if diff1 + diff2 <= K:
            t += c
            s_sorted.remove(c)
            diff = diff1
            counter = Counter(S[:i + 2]) - Counter(t)
            print(counter)
            counts = sum(counter.values())
            break
print(t)