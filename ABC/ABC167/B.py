A, B, C, K = map(int, input().split())

if K > A:
    K = K-A
    if K > B:
        K = K-B
        if K > C:
            print(A-C)
        else:
            print(A-K)
    else:
        print(A)
else:
    print(K)