N, K = map(int, input().split())
R = list(map(int, input().split()))
R.sort()
rate = 0
#print(R)
R = R[N-K:]
#print(R)
for i in R:
    #print(rate)
    rate = (rate+i)/2
    #print(rate)
print(rate)
