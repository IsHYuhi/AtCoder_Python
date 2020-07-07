n, k = map(int, input().split())
#一つ目はk通り、それ以降は(k-1)通りをn-1回繰り返す
print(int(k*((k-1)**(n-1))))