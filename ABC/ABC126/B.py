s = input()
a = int(s[:2])
b = int(s[2:])
if 0<a<=12 and 0<b<=12:
    print('AMBIGUOUS')
elif a<=99 and 0<b<=12:
    print('YYMM')
elif 0<a<=12 and b<=99:
    print('MMYY')
else:
    print('NA')
