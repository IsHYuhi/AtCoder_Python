import math
def fun(A, B, x):
    return math.floor(A*x/B)-A*math.floor(x/B)

A, B, N = map(int,input().split())
x = min(B-1, N)
print(int(fun(A, B, x)))