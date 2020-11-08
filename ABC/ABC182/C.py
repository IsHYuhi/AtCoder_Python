n = list(input())
length = len(n)

def dfs(i, count, sum):
    if i == length:
        if sum % 3 == 0 and sum != 0:
            return length-count
        else:
            return float('inf')

    d1 = dfs(i+1, count+1, sum+int(n[i]))
    d2 = dfs(i+1, count , sum)

    return min(d1, d2)

ans = dfs(0, 0, 0)

if ans != float('inf'):
    print(ans)
else:
    print(-1)