N = int(input())
ans = ''

i = 1
while True:
    if N <= 26**i:
        N -= 1# a=1なので0に合わせる
        for j in range(i):
            ans += chr(ord('a') + N%26)# 26の時ord(a)+25
            N //= 26
        break
    else:
        N -= 26 ** i
    i+=1
print(ans[::-1])

# N = int(input())
# 2 ans = ''
# 3 while N > 0:
# 4 N -= 1
# 5 ans += chr(ord('a') + N % 26)
# 6 N //= 26
# 7 print(ans[::-1])


# l = []
# ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'

# i = 0
# pre = 0
# while N>26**i:
#     i += 1
# i -= 1

# #l.append((N%26))
# #N -= N%26
# print(i)
# while N>26:
#     l.append(N//(26**i)-1)
#     N -= (N//26**i)*26**i
#     i -= 1
#     print(N)
# l.append(N)
# print(l)
# for i in l:
#     print(ascii_lowercase[i-1], end='')
# print('')




# while N>26:
#     l.append(N%26)
#     N = (N//26)
#     print(N)
# l.append(N%26)
# print(l[::-1])
# for i in l[::-1]:
#     print(ascii_lowercase[i], end='')
# print('')