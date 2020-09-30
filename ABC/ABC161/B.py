N, M= list(map(int, input().split()))
A = list(map(int, input().split()))
total = sum(A)

if len([i for i in A if i >= total/(4*M)])>= M:
    print("Yes")
else:
    print("No")