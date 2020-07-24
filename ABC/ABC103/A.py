a, b, c = map(int, input().split())
print(min(abs(a-b)+abs(b-c), abs(a-c)+abs(c-b), abs(a-b)+abs(a-c)))