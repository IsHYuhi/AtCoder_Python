import bisect
n = int(input())
a = list(map(int, input().split()))
a.sort()
total = sum(a)
ans = 0
for o, i in enumerate(a, 1):
    total -= i
    ans += abs(i*(n-o)-total)

print(ans)

# total = sum(a)
# div = [total]
# a = [[i, idx] for idx, i in enumerate(a)]
# new_a = sorted(a, key=lambda x: x[0])
# su = 0
# for i, j in new_a:
#     su += i
#     div.append(total-su)

# print(total)
# print(new_a)
# print(div)
# ans = 0
# new_a = sorted(new_a, key=lambda x: x[1], reverse=True)
# off = 0
# for i, j in new_a:
#     l = j-1
#     r = j
#     # l = bisect.bisect_left(new_a, i)
#     # r = bisect.bisect_right(new_a, i)
#     # print(l, r)
#     #print()
#     ans += l*i-(total-div[l]) + div[r]-off-(n-l)*i
#     off += div[l]
#     #print(div[bisect.bisect_left(new_a, i)])
#     #print()

# print(ans)