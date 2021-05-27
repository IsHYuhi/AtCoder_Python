n, m, q = map(int, input().split())
wv = [list(map(int, input().split())) for _ in range(n)]
x = list(map(int, input().split()))
lr = [list(map(int, input().split())) for _ in range(q)]

x = [(x[i], i+1) for i in range(m)]
x.sort(key=lambda x: x[0])

for l, r in lr:
    ans = 0
    visited = [False]*n

    for xi, i in x:
        if l<=i<=r:
            continue

        else:
            tmp = 0
            tmp_i = -1
            for j, (w, v) in enumerate(wv):
                if w<=xi and visited[j]!=True:
                    if tmp<=v:
                        tmp = v
                        tmp_i = j

            ans += tmp
            if tmp_i != -1:
                visited[tmp_i] = True

    print(ans)
