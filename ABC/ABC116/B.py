s = int(input())
an = [s]
for i in range(1, 1000000):
    if an[i-1]%2==0:
        ins = an[i-1]//2
    else:
        ins = 3*an[i-1]+1

    if ins not in an:
        an.append(ins)
    else:
        print(i+1)
        exit()
