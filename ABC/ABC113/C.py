n, m = map(int, input().split())
py = []

for i in range(m):
    _p, _y = map(int, input().split())
    py.append([_p, _y, i])

py = sorted(py, key=lambda x: (x[0], x[1]))
ans = []
p = -1
x = 1

for i in range(m):
    if p != py[i][0]:
        x = 1
        p = py[i][0]
    else:
        x += 1

    pid = str(py[i][0]).zfill(6)
    xid = str(x).zfill(6)
    ans.append([pid+xid, py[i][2]])

ans = sorted(ans, key=lambda x: x[1])

for a, i in ans:
    print(a)
