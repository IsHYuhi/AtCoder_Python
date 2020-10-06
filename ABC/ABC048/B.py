a, b, x = map(int, input().split())
count = 0
start = 0
for i in range(x, 10**18+x+1, x):
    if a<=i:
        start = count
        break
    count += 1
if a==0:
    start = -1
print(b//x - start)