import math
def lcm(a, b):
    return (a*b)//math.gcd(a, b)

a, b, c, d = map(int, input().split())
ans = (b-(a-1))-(b//c-(a-1)//c)-(b//d-(a-1)//d)+(b//lcm(c,d)-(a-1)//lcm(c,d))
print(ans)