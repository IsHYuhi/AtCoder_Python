from collections import Counter
abc = list(map(int, input().split()))

ans = 0
m = max(abc)
for i in range(len(abc)):
    count = (m-abc[i])//2
    ans += count
    abc[i] = abc[i]+2*count

abc = Counter(abc)

if len(abc)==1:
    print(ans)
else:
    key = [k for k, v in abc.items() if v == 2][0]
    if key == m:
        print(ans+2)
    else:
        print(ans+1)
