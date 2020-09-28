import numpy as np
from itertools import permutations
n = int(input())
p = tuple(map(int, input().split()))
q = tuple(map(int, input().split()))
permu = [i for i in range(1, n+1)]
permu = permutations(permu, n)

for i, s in enumerate(permu):
    if p == s:
        a = i+1
    if q == s:
        b = i+1

print(abs(a-b))
