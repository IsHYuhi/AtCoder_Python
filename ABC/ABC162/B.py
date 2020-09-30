N = int(input())

sum=0
for i in range(1,N+1):
    if not (i%3==0 or i%5==0):
        sum += i
print(sum)