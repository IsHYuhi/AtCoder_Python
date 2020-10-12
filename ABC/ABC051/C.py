from collections import deque
sx, sy, tx, ty = map(int, input().split())
ans = ''

def move(right, up):
    global ans
    while right and up:
        while up:
            s = up.popleft()
            ans += s

        while right:
            s = right.popleft()
            ans += s

right = deque(['R']*(tx-sx))
up = deque(['U']*(ty-sy))
move(right, up)

left = deque(['L']*abs(sx-tx))
down = deque(['D']*abs(sy-ty))
move(left, down)


right = deque(['R']*(tx-sx+1))
up = deque(['U']*(ty-sy+1))

ans += 'L'
move(right, up)
ans += 'D'

left = deque(['L']*(abs(sx-tx)+1))
down = deque(['D']*(abs(sy-ty)+1))

ans += 'R'
move(left, down)
ans += 'U'

# print(len(ans))
print(ans)