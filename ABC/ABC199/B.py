n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

arr = []
for i in range(1, 1001):
    flag = 0
    for a_, b_ in zip(a, b):
        if not (a_<= i <= b_):
            flag = 1
            break
    if flag == 0:
        arr.append(i)

print(len(arr))