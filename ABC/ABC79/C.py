ABCD = input()

def dfs(i, f, sum):
    if i==3:
        if sum==7:
            print(f + '=7')
            exit()
    else:
        dfs(i+1, f + "-" + ABCD[i+1], sum - int(ABCD[i+1]))
        dfs(i+1, f + "+" + ABCD[i+1], sum + int(ABCD[i+1]))

dfs(0, ABCD[0], int(ABCD[0]))