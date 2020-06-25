li = [1, 2, 3, 4, 5, 6]
n = int(input())
n = n % 30
for i in range(n):
    m1 = i%5
    m2 = i%5 +1
    li[m1], li[m2] = li[m2], li[m1]
print("".join(map(str, li)))