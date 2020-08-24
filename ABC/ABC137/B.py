k, x = map(int, input().split())
ans = [str(i) for i in range(x-k+1, x+k)]
print(' '.join(ans))