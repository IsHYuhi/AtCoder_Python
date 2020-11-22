import math

s = int(input())
mod = 10**9 + 7

seq = [0]*(s+1)
seq[0] = 1

for i in range(3, s+1):
    seq[i] = sum(seq[:i-2])
print(seq[s]%mod)
