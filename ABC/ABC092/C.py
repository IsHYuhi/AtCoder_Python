n = int(input())
a = list(map(int, input().split()))
a = [0] + a + [0]
total = 0
pre = 0

for i in a:
    total += abs(i-pre)
    pre = i

for i in range(1, len(a)-1):
    print(total + abs(a[i+1]-a[i-1]) - abs(a[i]-a[i+1]) - abs(a[i]-a[i-1]))
