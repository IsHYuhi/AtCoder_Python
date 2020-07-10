a, b = map(lambda x:True if x=='H' else False, input().split())
if a ^ b:
    print('D')
else:
    print('H')