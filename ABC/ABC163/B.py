def main():
    N, M = list(map(int, input().split()))
    A = list(map(int, input().split()))
    cost=0
    for i in A:
        cost += i
    print(N-cost if N>=cost else -1)

if __name__ == '__main__':
    main()