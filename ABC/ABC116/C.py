n = int(input())
h = list(map(int, input().split()))

def mizuyari(h):
    if len(h)==0:
        return 0
    elif len(h)==1:
        return h[0]

    m = min(h)
    l = 0
    r = 0
    sm = 0

    while r < len(h):
        if h[r]==m:
            sm += mizuyari(list(map(lambda x: x-m, h[l:r])))
            l = r+1
        r += 1
    sm += mizuyari(list(map(lambda x: x-m, h[l:r])))

    return m + sm

print(mizuyari(h))