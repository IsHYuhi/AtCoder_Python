n = int(input())
ss = [input() for _ in range(n)]

wo = dict()
ex = dict()
for s in ss:
    if s[0]== '!':
        ex[s[1:]] = True

    else:
        wo[s] = True

keys = set(wo.keys()) & set(ex.keys())

if keys:
    print(list(keys)[0])
else:
    print('satisfiable')