n, k = map(int, input().split())
h = list(map(int, input().split()))
print(len([i for i in h if i>=k]))
