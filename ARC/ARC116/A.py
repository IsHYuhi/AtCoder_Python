#AC with PyPy3
t = int(input())
cases = [int(input()) for _ in range(t)]

for case in cases:
    e_count = 0
    if case == 2:
        print('Same')
    elif case%2 == 1:
        print('Odd')
    else:
        while case%2==0:
            case = case//2
            e_count +=1
        if e_count == 1:
            print('Same')
        else:
            print('Even')


