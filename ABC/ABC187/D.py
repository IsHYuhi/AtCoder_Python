n = int(input())
diff = []
result = 0
for i in range(n):
    a, b = map(int, input().split())
    diff.append(2*a+b)
    result -= a

diff.sort(reverse=True)
i = 0
while result<=0:
    result += diff[i]
    i += 1
print(i)