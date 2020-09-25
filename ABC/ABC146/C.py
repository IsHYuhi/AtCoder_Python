a, b, x = map(int, input().split())

def binary_search(a, b, x):
    left = 1
    right = 10**9
    while left<=right:
        mid = (left+right)//2
        if x == a*mid+b*int(len(str(mid))):
            return mid
        elif x<a*mid+b*int(len(str(mid))):
            right = mid-1
        else:
            left = mid+1
    return right

print(binary_search(a, b, x))
