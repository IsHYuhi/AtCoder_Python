S = list(input())
S.pop()
while S[:len(S)//2]!=S[len(S)//2:]:
    S.pop()
print(len(S))