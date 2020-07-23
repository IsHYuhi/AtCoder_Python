d, n = map(int, input().split())
count = 0
i = 1

while True:
    c = 0
    num = i
    while num >= 100:
        if num%100==0:
            num = num//100
            c += 1
        else:
            break
    if c==d:
        count += 1
    if count == n:
        print(i)
        break
    i += 1