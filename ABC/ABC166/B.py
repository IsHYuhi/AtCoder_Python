import collections

N, K = map(int,input().split())
sunuke = [0]*N# for _ in range(N)]
for i in range(K):
    _ = input()
    n = map(int,input().split())
    for j in n:
        sunuke[j-1] +=1
sunuke = collections.Counter(sunuke)
#print(sunuke)
print(sunuke[0])