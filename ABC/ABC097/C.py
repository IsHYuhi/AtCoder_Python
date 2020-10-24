s = input()
k = int(input())
substrings = []

for i in range(len(s)):
    for j in range(i+1, len(s)+1):
        if j-i > k:
            continue
        substrings.append(s[i:j])


substrings = sorted(substrings)

pre = ''
count = 0
for _s in substrings:
    if _s == pre:
        continue
    count += 1
    pre = _s
    if count == k:
        print(_s)
        exit()
