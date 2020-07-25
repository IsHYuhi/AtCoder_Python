s = input()
k = int(input())

for i in range(0,k):
    if s[i] != '1':
        print(s[i])
        exit()
print(s[0])
