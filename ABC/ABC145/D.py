x, y = map(int, input().split())
com = [0, 0]
for i in range(x//2+1):
   if i + (x-2*i)*2 == y:
       com = [i, x-2*i]

if com[0]+com[1]==0:
    print(0)
    exit()

mod = 10**9+7
n = 1
p = 1
l = com[0]+com[1]

for i in range(1, l+1):
    if i > com[1]:
        n *= i
        n %= mod

    if i <= com[0]:
        p *= pow(i, mod-2, mod)
        p %= mod

print((n*p)%mod)