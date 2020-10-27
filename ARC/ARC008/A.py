n = int(input())

print(min((n//10)*100+(n%10)*15,(n//10 + 1)*100))