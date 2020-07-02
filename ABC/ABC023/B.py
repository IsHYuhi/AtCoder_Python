from collections import deque
n = int(input())
S = input()
len(S)
S = deque(S)
ans = 0
while len(S)>1:
    l = S.popleft()
    r = S.pop()
    ans += 1
    if len(S)%3 == 2:
        if not l==r=='b':
            print(-1)
            exit()
    elif len(S)%3 == 0:
        if not (l=='c' and r=='a'):
            print(-1)
            exit()
    elif len(S)%3 == 1:
        if not (l=='a' and r=='c'):
            print(-1)
            exit()

if len(S)==0:
    print(-1)
    exit()
elif len(S)==1:
    if not 'b'==S.pop():
        print(-1)
        exit()
print(ans)