from itertools import combinations

abcd = list(map(int, input().split()))
total = sum(abcd)

for i in range(1, 5):
    comb = list(combinations(abcd, i))

    for j in comb:
        choose = sum([j for j in list(j)])

        if  choose == total - choose:
            print('Yes')
            exit()

print('No')

