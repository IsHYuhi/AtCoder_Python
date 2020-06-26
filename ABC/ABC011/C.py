N = int(input())
ng = [int(input()) for i in range(3)]
ng.sort(reverse=True)
ng3 = [i%3 for i in ng]
#print(ng3)
if N in ng:
    print("NO")
    exit()
count = 0
# for i in ng3:
#     if i == N%3:
#        N = N-3*((N - i)//3)
#        count += (N - i)//3
#        N -= 4
#        count += 2
while N > 0:
    if N-3 in ng and N-2 in ng and N-1 in ng:
        print('NO')
        exit()
    if N-3 not in ng and N-3 >= 0:
        N -= 3
        count += 1
    elif N-2 not in ng and N-2 >= 0:
        N -= 2
        count += 1
    elif N-1 not in ng and N-1 >= 0:
        N -= 1
        count += 1

    if count>100:
        print('NO')
        exit()
print('YES')


###ans
# N = int(input())
# ng = [int(input()) for i in range(3)]
# if N in ng:
#     print("NO")
#     exit()
# if N <= 3:
#     print("YES")
#     exit()
# dp = [float('inf')]*(N+1)
# dp[N] = 0
# for i in range(N, -1, -1):
#     if i not in ng:
#         for j in range(1,4):
#             dp[i-j] = min(dp[i]+1, dp[i-j])
# if dp[0]<=100:
#     print("YES")
# else:
#     print("NO")