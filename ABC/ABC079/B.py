n = int(input())
l = [0]*(n+1)
l[0]=2
l[1]=1
def lucas_number(n):
    if l[n]!=0:
        return l[n]
    l[n] = lucas_number(n-1)+lucas_number(n-2)
    return l[n]
print(lucas_number(n))