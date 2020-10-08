k = int(input())

if k%7==0:
    l = 9*(k//7)
elif k%5==0 or k%2==0:
    print(-1)
    exit()
else:
    l = 9*k

n = 10
for i in range(1, l):
    if n % l == 1:
        print(i)
        exit()
    n = 10*(n%l)

print(-1)