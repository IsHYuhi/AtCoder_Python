import math
r, x, y = map(int, input().split())
if r != ((x**2+y**2)**0.5) and ((x**2+y**2)**0.5)  <= 2*r:
    print(2)
else:
    print(math.ceil(((x**2+y**2)**0.5)/r))