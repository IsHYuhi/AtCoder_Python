sd = input()
t = input()

n = len(sd)
m = len(t)
s = []

for i in range(n-m, -1, -1):
    t_p = sd[i:i+m]
    for j in range(m+1):
        if j == m:
            print((sd[:i] + t + sd[i + len(t):]).replace("?", "a"))
            exit()
        else:
            if t_p[j] == "?":
                continue
            elif t_p[j] != t[j]:
                break

print("UNRESTORABLE")