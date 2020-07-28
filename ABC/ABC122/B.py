acgt = list('ACGT')
s = input()
ans = 0
count = 0
for i in s:
    if i in acgt:
        count += 1
        ans = max(count, ans)
    else:
        count = 0
print(ans)
