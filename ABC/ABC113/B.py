n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))
h = [abs(a-(t-x*0.006)) for x in h]
print(h.index(min(h))+1)
