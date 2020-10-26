n, m = map(int, input().split())
disk = [int(input()) for _ in range(m)]

case = [i for i in range(1, n+1)]
player = 0

for d in disk:
    if d == player:
        continue
    player, case[case.index(d)] = d, player

for i in case:
    print(i)
