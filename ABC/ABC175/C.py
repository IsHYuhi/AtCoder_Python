x, k, d = map(int, input().split())

print(abs(abs(abs(x)-min((abs(x)//d), k)*d)-((k-min(abs(x)//d,k))%2)*d))