h, w = map(int, input().split())
n = int(input())
a = list(map(int, input().split()))
field = [[0]*w for _ in range(h)]

def check(field):
    for l in field:
        print(' '.join(map(str, l)))

rw = w
dh =  h
k = 0
count = 0
k_count = 0
while True:
    for wi in range(w-rw, rw):
        field[h-dh][wi] = k+1
        count += 1
        k_count += 1
        if count >= h*w:
            check(field)
            exit()
        if k_count >= a[k]:
            k_count = 0
            k += 1

    for hi in range(h-dh+1, dh):
        field[hi][rw-1] = k+1
        count += 1
        k_count += 1
        if count >= h*w:
            check(field)
            exit()
        if k_count >= a[k]:
            k_count = 0
            k += 1

    for wi in range(1, 2*rw - w):
        field[dh-1][rw-wi-1] = k+1
        count += 1
        k_count += 1
        if count >= h*w:
            check(field)
            exit()
        if k_count >= a[k]:
            k_count = 0
            k += 1

    for hi in range(1, 2*dh - h -1):
        field[dh-hi-1][w-rw] = k+1
        count += 1
        k_count += 1
        if count >= h*w:
            check(field)
            exit()
        if k_count >= a[k]:
            k_count = 0
            k += 1

    rw -= 1
    dh -= 1
