A = int(input())
B = int(input())
C = int(input())
li = [A, B, C]
sort = sorted(li, reverse=True)
for i in li:
    print(sort.index(i)+1)