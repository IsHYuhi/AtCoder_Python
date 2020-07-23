a, b = map(int, input().split())

for i in range(1, 1000):
    if abs(b-a)==i:
        print(int((i-1)*i/2) - a)
        break