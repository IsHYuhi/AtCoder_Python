a, b, w = map(int, input().split())
w = w*1000

if a+(w%a)/(w//a)<= b:
    r = 1 if w%b != 0 else 0
    print(w//b+r, w//a)

else:
    print('UNSATISFIABLE')

