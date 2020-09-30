K = int(input())
A, B = map(int,input().split())

for i in range(A,B+1):
    if i%K ==0:
        print('OK')
        exit()
print('NG')
