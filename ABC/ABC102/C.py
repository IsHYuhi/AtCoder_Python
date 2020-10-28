n = int(input())
a = list(map(int, input().split()))

a = [i-j for j, i in enumerate(a, 1)]
a.sort()
b = a[n//2]
a = [abs(i-b) for i in a]
print(sum(a))