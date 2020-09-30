import collections
def main():
    N = int(input())
    S = [input() for i in range(N)]
    S = collections.Counter(S)
    print(len(S))

if __name__ == '__main__':
    main()


