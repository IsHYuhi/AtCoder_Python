from collections import deque
n = int(input())
a = list(map(str, input().split()))
b = a[1::2][::-1]+a[::2]
if len(a)%2==0:
    print(' '.join(b))
else:
    print(' '.join(b[::-1]))