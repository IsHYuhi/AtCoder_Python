N = input()
m = int(N[-1])

if m == 3:
    print('bon')
elif m == 2 or m == 4 or m == 5 or m == 7 or m == 9:
    print('hon')
else:
    print('pon')
