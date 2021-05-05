x = int(input())
r = x%100

li = [1, 2, 3, 4, 5][::-1]

count = 0
for i in li:
    while r>=i:
        r -= i
        count += 1

if (x-r)//100 >= count:
    print(1)
else:
    print(0)