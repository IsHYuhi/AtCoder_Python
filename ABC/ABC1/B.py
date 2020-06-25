m = int(input())
#m = m/1000
if m < 100:
    c = 0
elif m <= 5000:
    c = int(m/100)
elif m <=30000:
    c = int((m+50000)/1000)
elif m <=70000:
    c = int((m-30000)/5000 + 80)
else:
    c = 89
c = str(c)
c = str('0')+c if len(c) <2 else c

print(c)