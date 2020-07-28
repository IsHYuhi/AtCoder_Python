nums = [int(input()) for _ in range(5)]
k = int(input())

if nums[-1]-nums[0]>k:
    print(':(')
else:
    print('Yay!')