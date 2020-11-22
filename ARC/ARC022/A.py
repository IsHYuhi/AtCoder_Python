s = input().lower()

seq = 'ict'
idx = 0
for i in s:
    if i == seq[idx]:
        idx += 1
        if idx >= 3:
            print('YES')
            exit()
print('NO')
