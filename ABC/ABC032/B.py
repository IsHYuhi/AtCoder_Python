s = input()
k = int(input())
ans = 0
words = set()
for i in range(len(s)-k+1):
    if s[i:i+k] not in words:
        ans+=1
        words.add(s[i:i+k])
print(ans)