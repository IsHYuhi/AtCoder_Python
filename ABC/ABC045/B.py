from collections import deque

a = deque(input())
b = deque(input())
c = deque(input())
dic = {'A':a, 'B':b, 'C':c}
pop = dic['A'].popleft().upper()

while dic[pop]:
    pop = dic[pop].popleft().upper()

print(pop)