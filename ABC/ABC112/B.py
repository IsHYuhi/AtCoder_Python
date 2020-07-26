n, t = map(int, input().split())
ct = [list(map(int, input().split())) for _ in range(n)]

ct = [i[0] for i in ct if i[1]<=t]
if not ct:
    print('TLE')
else:
    print(min(ct))