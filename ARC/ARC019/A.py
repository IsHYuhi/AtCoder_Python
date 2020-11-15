s = list(input())
dic = {'O':'0', 'D':'0', 'I':'1', 'Z':'2', 'S':'5', 'B':'8'}
print(''.join([dic[i] if dic.get(i) else i for i in s]))
