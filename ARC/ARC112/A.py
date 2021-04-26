t = int(input())
cases = [list(map(int, input().split())) for i in range(t)]

for l, r in cases:
    if r-l*2 < 0:
        print(0)
        continue
    print((r-l*2+1)*(r-l*2+2)//2)
