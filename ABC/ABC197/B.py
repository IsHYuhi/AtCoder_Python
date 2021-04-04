h, w, x, y = map(int, input().split())
field = [list(input()) for _ in range(h)]
ans = 0

for i in field[x-1][:y-1][::-1]:
    if i == '#':
        break
    ans += 1

for i in field[x-1][y-1:]:
    if i == '#':
        break
    ans += 1

for i in field[:x-1][::-1]:
    if i[y-1] == '#':
        break
    ans += 1

for i in field[x-1:]:
    if i[y-1] == '#':
        break
    ans += 1

print(ans-1)