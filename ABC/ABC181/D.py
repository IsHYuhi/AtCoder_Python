from collections import Counter
s = input()
div = list(map(int, list(s)))
count = Counter(div)

if len(s)<=1:
    if int(s) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

elif len(s) <= 2:
    if int(str(div[0])+str(div[1])) % 8 == 0 or int(str(div[1])+str(div[0])) % 8 == 0:
        print('Yes')
    else:
        print('No')
    exit()

for i in range(100, 1000):
    if i % 8 == 0:
        flag = True
        for k, v in Counter(list(map(int, list(str(i))))).items():
            if count.get(k):
                if not count[k]>=v:
                    flag = False
            else:
                flag = False

        if flag == True:
            print('Yes')
            exit()
print('No')

#print(eights)