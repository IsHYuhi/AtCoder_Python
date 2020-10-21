n = int(input())
words = input().split()

takahashi = ['TAKAHASHIKUN', 'Takahashikun', 'takahashikun', 'TAKAHASHIKUN.', 'Takahashikun.', 'takahashikun.']
ans = 0

for w in words:
    if w in takahashi:
        ans += 1

print(ans)
