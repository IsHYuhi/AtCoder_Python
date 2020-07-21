from collections import deque
n = int(input())

txy = deque([list(map(int, input().split())) for _ in range(n)])

tn, xn, yn = 0, 0, 0
while txy:
    t, x, y = txy.popleft()
    if (abs(xn-x)+abs(yn-y)<=(t-tn)) and (abs(xn-x)+abs(yn-y))%2==(t-tn)%2:
        tn, xn, yn = t, x, y
    else:
        print('No')
        exit()
print('Yes')