n = int(input())
s = [input()[::-1] for _ in range(n)]
s.sort()
for i in s:
    print(i[::-1])

