import collections

def main():
    N = int(input())
    A = list(map(int, input().split()))
    A = collections.Counter(A)
    for i in range(1,N+1):
        print(A[i] if A[i] is not None else 0)

if __name__ == '__main__':
    main()