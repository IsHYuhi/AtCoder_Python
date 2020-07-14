seq = list(map(int, input().split()))
seq.sort()
print(sum(seq[:2]))