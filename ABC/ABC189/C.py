n = int(input())
a = list(map(int, input().split()))

def split_array(a, key):
    n = len(a)
    l, r = 0, 0
    new = []
    i = 0
    while i<n:
        if a[i]==key:
            r = i
            if l!=r:
                new.append(a[l:r])
                l = r+1

            else:
                l += 1
        i += 1

    if a[n-1]!=key:
        new.append(a[l:n])

    return new

def dfs(a):
    if len(a)<=1:
        return min(a)
    min_a = min(a)
    max_a = min_a*len(a)
    for na in split_array(a, min_a):
        r = dfs(na)
        if r > max_a:
            max_a = r
    return max_a

print(dfs(a))
