a, b, c, d = map(int, input().split())


box_b = a
box_r = 0
count = 0

if box_b<=box_r*d:
    print(0)
    exit()

while True:
    if box_b<=box_r*d:
        break
    count += 1
    box_b += b
    box_r += c
    if count == 10**5+1:
        print(-1)
        exit()
    
print(count)
