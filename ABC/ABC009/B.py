N = int(input())
As = set([int(input()) for i in range(N)])
As = sorted(list(As), reverse=True)
print(As[1])