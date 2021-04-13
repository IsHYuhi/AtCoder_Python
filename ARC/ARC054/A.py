l, x, y, s, d = map(int, input().split())

speed_n = x+y
speed_b = 0 if x-y>0 else -(x-y)

if s<=d:
    print(min((d-s)/speed_n if speed_n != 0 else float('inf'), (l-d+s)/speed_b if speed_b != 0 else float('inf')))
else:
    print(min((l-s+d)/speed_n if speed_n != 0 else float('inf'), (s-d)/speed_b if speed_b != 0 else float('inf')))