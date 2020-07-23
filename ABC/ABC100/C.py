n = int(input())
a = list(map(int, input().split()))

count = 0
for i in a:
    if i%2 == 0:
        num = i
        while num%2==0:
            num = num//2
            count +=1
if count==0:
    print(0)
else:
    print(count)