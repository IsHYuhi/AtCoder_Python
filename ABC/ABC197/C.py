#AC with PyPy
from functools import reduce
n = int(input())
a = list(map(int, input().split()))

def my_or(x, y):
    return x | y

def or_list(numbers):
    return reduce(my_or, numbers)

def ors(idxs):
    if idxs == [0]:
        return a
    arr = []
    s = 0
    for i in idxs[1:]:
        arr.append(or_list(a[s:i]))
        s = i

    arr.append(or_list(a[s:]))

    return arr

def xors(idxs):
    ans = 0
    li = ors(idxs)
    for i in li:
        ans = ans ^ i
    return ans


def dfs(split_idx):
    mi = xors(split_idx)

    if split_idx[-1] == n:
        return mi

    for i in range(split_idx[-1]+1, n):
        mi = min(dfs(split_idx+[i]), mi)

    return mi

def dfs2(idx, split_idx):
    mi = xors(split_idx)

    if idx == n:
        return mi

    mi = min(dfs2(idx+1, split_idx+[idx]), mi)
    mi = min(dfs2(idx+1, split_idx), mi)

    return mi

# print(dfs([0]))
print(dfs2(1, [0]))