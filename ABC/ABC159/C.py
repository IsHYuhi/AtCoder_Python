from decimal import Decimal
L = float(input())
ans = Decimal((L/3)**3)
print('{:.12f}'.format(ans))