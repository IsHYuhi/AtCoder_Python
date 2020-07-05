a, b, c = map(int, input().split())

print(c//min(a,b)+(c-min(a,b)*(c//min(a,b)))//max(a,b))