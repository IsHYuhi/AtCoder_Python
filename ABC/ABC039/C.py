from collections import Counter
onkai_m = ['Mi', 'Fa', 'So', 'La', 'Si', 'Do', 'Re'][::-1]
onkai_s = [ 'Si', 'Do', 'Re', 'Mi', 'Fa', 'So', 'La'][::-1]

s = input()
for i in range(20-1):
    if s[i:i+2] == 'WW':
        index = i+1
        break
num = Counter(s[index:index+6])

w_num = Counter(s[:index-1])
w_num = w_num['W']
if num['B']==3:
    print(onkai_m[w_num-1])
elif num['B']==2:
    print(onkai_s[w_num-1])