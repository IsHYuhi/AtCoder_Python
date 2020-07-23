a, b, c = map(int, input().split())
k = int(input())
print((max(a, b, c))*(2**k)+a+b+c-max(a, b, c))
