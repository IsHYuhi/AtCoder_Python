n, l = map(int, input().split())

amida = [input() for _ in range(l+1)]

amida = amida[::-1]

for i in range(len(amida[0])):
    if amida[0][i] == 'o':
        now = i

for row in amida[1::]:
    if now<n*2-3 and row[now+1] == '-':
        now += 2
    elif now>1 and row[now-1] == '-':
        now -= 2

print(now//2+1)
