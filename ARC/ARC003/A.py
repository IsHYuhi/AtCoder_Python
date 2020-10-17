n = int(input())
total = 0
dic = {'A': 4, 'B': 3, 'C': 2, 'D': 1, 'F':0}
gp = list(input())
for e in gp:
    total += dic[e]
print(total/n)
