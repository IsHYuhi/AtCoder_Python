import math
def main():
    A, B, C, D = map(int,input().split())

    if math.ceil(C/B) <= math.ceil(A/D):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()