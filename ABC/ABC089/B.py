from collections import Counter
n = int(input())
s = Counter(list(input().split()))
if len(s)==4:
    print('Four')
else:
    print('Three')
