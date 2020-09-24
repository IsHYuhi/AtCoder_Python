import math
a, b, x = map(int, input().split())
s = x/a
half = (a*b)/2

if s<=half:
    y = (2*s)/b
    z = math.sqrt(b**2+y**2)
    alpha = b/z
    alpha = math.asin(alpha)
    alpha = math.degrees(alpha)

    print(alpha)

if s>half:
    z = math.sqrt(b**2+a**2)

    alpha = b/z
    alpha = math.asin(alpha)
    alpha = math.degrees(alpha)

    beta = a/z
    beta = math.asin(beta)
    beta = math.degrees(beta)

    l = 2*(s-half)/(math.sin(math.radians(90-alpha))*z)
    k = math.sqrt(z**2+l**2-2*l*z*math.cos(math.radians(90-alpha)))

    gamma = 2*(s-half)/(k*z)
    gamma = math.asin(gamma)
    gamma = math.degrees(gamma)

    print(90-(gamma+beta))