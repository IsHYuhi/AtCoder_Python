from collections import Counter
n = int(input())
a = list(map(int, input().split()))
counter = Counter(a)

kind = len(counter)
divs = []
odds = []

for k, v in counter.items():
    if v%2==0:
        divs.append(k)
    else:
        odds.append(k)


if len(divs)%2!=0:
    kind -= 1

print(kind)
