import math
A, B, H, M = map(int, input().split())

ra = H*30 + 0.5*M
rb = M*6
rc = abs(ra-rb)
if rc > 180:
    rc = 360 - rc
print(rc)
c2 = A**2 + B**2 - 2*A*B* math.cos(math.radians(rc))#cosのときはradianに直す
print(c2**(0.5))