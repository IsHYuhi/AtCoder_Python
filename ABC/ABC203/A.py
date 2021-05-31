from collections import Counter
abc = list(map(int, input().split()))

count = Counter(abc)

if len(count)>=3:
    print(0)
    exit()
elif len(count)==1:
    print(abc[0])
    exit()


for i, v in count.items():
    if v==1:
        print(i)


