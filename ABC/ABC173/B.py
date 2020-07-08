from collections import Counter
n = int(input())

S = [input() for i in range(n)]
S = Counter(S)

li = ['AC', 'WA', 'TLE', 'RE']

for i in li:
    if S.get(i):
        print(i+' x '+str(S[i]))
    else:
        print(i+' x '+str(0))