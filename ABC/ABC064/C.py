def color_judge(n):
    if 1<=n<=399:
        return 'gray'
    elif n<=799:
        return 'brown'
    elif n<=1199:
        return 'green'
    elif n<=1599:
        return 'light blue'
    elif n<=1999:
        return 'blue'
    elif n<=2399:
        return 'yellow'
    elif n<=2799:
        return 'orange'
    elif n<=3199:
        return 'red'
    else:
        return 'choice'

n = int(input())
a = list(map(int, input().split()))
dic = {}
for i in a:
    if dic.get(color_judge(i)):
        dic[color_judge(i)] += 1
    else:
        dic[color_judge(i)] = 1
choice = 0
l = len(dic)
if dic.get('choice'):
    choice = dic['choice']
    l -= 1
print(max(1, l), l+choice)