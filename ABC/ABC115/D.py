from os import name
import math
n, x = map(int, input().split())

an = [1]*(n+1)
anp = [1]*(n+1)

for i in range(1, n+1):
    an[i] = 2*an[i-1]+3
    anp[i] = 2*anp[i-1]+1

idx = n
ans = 0
while idx>=0:
    if idx==0:
        print(ans+anp[idx])
        exit()
    if x >= an[idx]-(idx-1):
        print(anp[idx]+ans)
        exit()
    elif x==1:
        print(ans)
        exit()
    elif x == math.ceil(an[idx]/2):
        print(ans+anp[idx-1]+1)
        exit()
    elif x < math.ceil(an[idx]/2):
        x -= 1
        idx -= 1
    elif x > math.ceil(an[idx]/2):
        ans += anp[idx-1]+1
        x -= an[idx-1]
        x -= 2
        idx -= 1
