from math import factorial
p = int(input())
ans = 0
for i in range(1, 11):
    d = factorial(i+1)
    r = p % d
    ans += r // factorial(i)
    p -= r
print(ans)

# from collections import deque
# p = int(input())
# f = [1]
# for i in range(2, 11):
#     f.append(a[-1]*i)

# f = deque(f)
# ans = 0
# r = 1

# while r != 0:
#     c = f.pop()
#     q = p // c
#     r = p % c
#     p -= q * c
#     ans += q

# print(ans)