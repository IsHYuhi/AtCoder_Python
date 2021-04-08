n = int(input())
m = list(map(int, input().split()))
m = [max(0, 80-i) for i in m]
print(sum(m))