S = list(input())
chars = [chr(ord('a')+i) for i in range(26)]
for i in chars:
    if i not in S:
        print(i)
        exit()
print('None')