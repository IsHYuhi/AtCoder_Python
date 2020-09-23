n = int(input())

def binary_search(l, target):
    left = 0
    right = len(l)
    while left<right:
        mid = (left+right)//2

        if target == l[mid]:
            return True
        elif target < l[mid]:
            right = mid
        else:
            left = mid+1

    return False

seki = [i*j for i in range(1, 10) for j in range(1, 10)]
seki.sort()

if binary_search(seki, n):
    print('Yes')
else:
    print('No')