n = int(input())
s = input()
k = int(input())

sk = s[k-1]
ans = [i if i == sk else '*' for i in s]
print(''.join(ans))
