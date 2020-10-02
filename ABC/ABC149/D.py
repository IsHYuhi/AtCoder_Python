import math
n, k = map(int, input().split())
r, s, p = map(int, input().split())
t = input()
#r<-p, s<-r, p<-s
dic = {'r': p, 's': r, 'p': s}
point = 0
lose = False

for j in range(k):
    point += dic[t[j]]
    for i in range(j+k, n, k):
        if t[i-k] != t[i] or lose:
            point += dic[t[i]]
            lose = False
        else:
            lose = True
    lose = False
print(point)
