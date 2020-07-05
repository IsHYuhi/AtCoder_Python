s = list(input().split('+'))
ans =0
for i in s:
    each = i.split('*')
    if '0' not in each:
        ans+=1
print(ans)