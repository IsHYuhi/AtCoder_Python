n, x = map(int, input().split())
a = list(map(int, input().split()))
bin_str = format(x, 'b')
#print(bin_str)
ans = 0
for j, i in enumerate(bin_str[::-1]):
    #print(i)
    if int(i)==1:
        ans += a[j]
print(ans)
