n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]

for cx in range(0, 101):
    for cy in range(0, 101):
        flag = True

        for x, y, hi in xyh:
            if hi == 0:
                continue
            else:
                base_H = hi + abs(x-cx) + abs(y-cy)
                break

        for x, y, hi in xyh:
            if hi != max(base_H - abs(x-cx)-abs(y-cy), 0):
                flag = False
                break

        if flag == True:
            print(cx, cy, base_H)
            exit()
