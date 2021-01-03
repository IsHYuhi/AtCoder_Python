a, b = map(str, input().split())

sum_a = 0
for i in a:
    sum_a += int(i)

sum_b = 0
for i in b:
    sum_b += int(i)

print(max(sum_a, sum_b))