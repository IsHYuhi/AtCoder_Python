from collections import Counter
n = int(input())
s = list(input())

def count_p(d):
    c = Counter(d)

    lc = 0
    rc = 0
    if c.get('('):
        lc = c['(']

    if c.get(')'):
        rc = c[')']

    return lc - rc

x = float('inf')
for i in range(0, n+1):
    x = min(x, count_p(s[:i]))
ds = count_p(s)

print('('*(-x)+''.join(s)+')'*(ds-x))
