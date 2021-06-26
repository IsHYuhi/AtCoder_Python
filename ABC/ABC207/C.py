n = int(input())
tlr = [list(map(int, input().split())) for _ in range(n)]

tlr.sort(key = lambda x: x[1])

count = 0
for i in range(n-1):
    for j in range(i+1, n):
        #print("check", tlr[i][0], tlr[j][0])
        if tlr[i][0] == 1 or tlr[i][0] == 3:# "]"

            if tlr[j][0] == 1 or tlr[j][0] == 2:# "["
                if tlr[j][1] - tlr[i][2] <= 0:
                    #(tlr[j][1], tlr[i][2])
                    count += 1

            elif tlr[j][0] == 3 or tlr[j][0] == 4:# "("
                if tlr[j][1] - tlr[i][2] < 0:
                    #print(tlr[j][1], tlr[i][2])
                    count += 1

        elif tlr[i][0] == 2 or tlr[i][0] == 4:# ")"

            if tlr[j][0] == 1 or tlr[j][0] == 2:# "["
                
                if tlr[j][1] - tlr[i][2] < 0:
                    #print(tlr[j][1], tlr[i][2])
                    count += 1

            elif tlr[j][0] == 3 or tlr[j][0] == 4:# "("
                if tlr[j][1] - tlr[i][2] < 0:
                    #print(tlr[j][1], tlr[i][2])
                    count += 1


print(count)