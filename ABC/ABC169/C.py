from decimal import Decimal
A, B = list(map(Decimal,input().split()))
print(int(Decimal(A*B)))