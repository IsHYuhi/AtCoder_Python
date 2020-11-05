n = int(input())
pannel = [list(input()) for _ in range(n)]

keep = False
count = 0
o_count = 0

for j in range(9):
    for i in range(n):

        if pannel[i][j] == 'o':
            keep = True
            o_count = 1

        elif pannel[i][j] == 'x':
            count += 1
            keep = False

        else:
            keep = False

        if not keep:
            count += o_count
            o_count = 0

    if o_count == 1:
        count += o_count
        o_count = 0

print(count)