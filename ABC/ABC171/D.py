from collections import Counter
#import numpy as np
N = int(input())
A = list(map(int, input().split()))
Q = int(input())
ans = sum(A)
A = Counter(A)
bc = [tuple(map(int, input().split())) for i in range(Q)]
# print(A)
# print(A.items())
for b, c in bc:
    v = A.pop(b, None)
    if v:
        A[c] += v
    #ans = sum(lambda x: x[0]*x[1], A.items())
    #ans = sum(i*j for i, j in A.items())
        ans = ans+((c-b)*v)
    #ans = sum(A.items(), key=lambda x: x[0]*x[1])
    #print(b, c)
    #print(A)
    print(ans)


# #A = np.asarray(A)
# for b, c in bc:
#     A = np.where(A == b, c, A)
#     # print('bc', b, c)
#     # print('A', A)
#     print(sum(A))
