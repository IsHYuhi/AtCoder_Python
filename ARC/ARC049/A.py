s = list(input())
abcd = list(map(int, input().split()))

for i, idx in enumerate(abcd):
    s.insert(idx+i, '"')

print(''.join(s))