a, b, k, l = map(int, input().split())

if a < b/l:
    print(k*a)
else:
    print(min( a*(k-l*(k//l))+b*(k//l), b*(k//l+1)))
