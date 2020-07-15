x, a, b = map(int, input().split())
li = [abs(x-a), abs(x-b)]
ans = ['A', 'B']
print(ans[li.index(min(li[0], li[1]))])
