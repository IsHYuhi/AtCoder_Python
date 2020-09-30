X = int(input())
count = 0
start = 100
while(X>start):
    start += int(start*0.01)
    count+=1
print(count)