def main():
    K, N = map(int,input().split())
    if K<=N:
        print('unsafe')
    else:
        print('safe')


if __name__ == '__main__':
    main()