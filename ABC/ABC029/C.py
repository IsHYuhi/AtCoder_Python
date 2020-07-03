import itertools
n = int(input())
abc = ['a', 'b', 'c']
li = list(map(lambda x: ''.join(x),itertools.product(abc, repeat=n)))
li.sort()
for i in li:
    print(i)