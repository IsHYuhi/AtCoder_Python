S = input()
N = int(input())

lr = [tuple(map(int, input().split())) for _ in range(N)]

for l, r in lr:
    l -= 1
    r -= 1
    S = S[:l]+S[r:l-len(S)-1:-1]+S[r+1:]
print(S)