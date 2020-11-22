r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

#同じ
if r1==r2 and c1==c2:
    print(0)
    exit()
#斜め
elif c1==r1-r2+c2 or c1==-(r1-r2)+c2:
    print(1)
    exit()
#3つ以内
elif abs(r1-r2)+abs(c1-c2) <= 3:
    print(1)
    exit()
#6つ以内
elif abs(r1-r2)+abs(c1-c2) <= 6:
    print(2)
    exit()

#斜め移動x2
if (r1+c1)%2 == (r2+c2)%2:
        print(2)
        exit()

else:
    if (c1+1)==r1-r2+c2 or (c1+2)==(r1-1)-r2+c2 or c1==(r1+1)-r2+c2 or (c1-1)==(r1+2)-r2+c2 or (c1+1)==-(r1-r2)+c2 or (c1-1)==-(r1-r2)+c2 or (c1-2)==-(r1-1-r2)+c2 or (c1+1)==-(r1+2-r2)+c2:
        print(2)
        exit()
    #斜め移動x2でいけないところ
    else:
        print(3)
        exit()


