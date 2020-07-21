a = int(input())
b = int(input())
c = int(input())
x = int(input())

ans = 0
for i in range(0,a+1):
    for j in range(0, b+1):
        if 0 <= ((x-500*i-100*j)//50) <= c:
            ans += 1
print(ans)