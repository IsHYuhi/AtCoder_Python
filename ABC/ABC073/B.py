n = int(input())
def minus(x):
    return int(x[1])-int(x[0])+1
lr = [minus(input().split()) for i in range(n)]
print(sum(lr))
