h, n = map(int, input().split())
a = list(map(int, input().split()))

if h<=sum(a):
    print('Yes')
else:
    print('No')