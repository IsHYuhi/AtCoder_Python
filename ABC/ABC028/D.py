import itertools
n, k = map(int, input().split())
nums = [i for i in range(1, n+1)]

nums = [1]
for i in range(n-1):
    nums.append(nums[-1]+3)
#print(nums)
ans = []
alpha = 3
for i, num in enumerate(nums[:-1]):
    ans.append(num+(n-i-1)*alpha)
    alpha += 6
ans.append(nums[-1])
#print(ans)
print(ans[k-1]/sum(ans))

##--------模範解答-------------[https://www.slideshare.net/chokudai/abc028]
#print(((n-k)*(k-1)*6+(n-1)*3+1)/n**3)





##法則チェック
# print(nums)
# nums = list(map(sorted,map(list,itertools.product(nums, repeat=3))))
# c1, c2, c3, c4, c5, c6, c7 = 0, 0, 0, 0, 0, 0, 0
# for i in nums:
#     if i[1]==1:
#         c1 += 1
#     elif i[1]==2:
#         c2 += 1
#     elif i[1]==3:
#         c3 += 1
#     elif i[1]==4:
#         c4 += 1
#     elif i[1]==5:
#         c5 += 1
#     elif i[1]==6:
#         c6 += 1
#     elif i[1]==7:
#         c7 +=1
# print(c1, c2, c3, c4, c5, c6, c7)
# print(nums)