N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
alice = A[::2]
bob = A[1::2]

print(sum(alice) - sum(bob))