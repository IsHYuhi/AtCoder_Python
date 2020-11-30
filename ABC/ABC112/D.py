n, m = map(int, input().split())

def div(n, d):
    arr = []
    for i in range(1, int(n**(1/2)+1)):
        if n%i==0:
            arr.append(i)
            arr.append(n//i)

    return [i for i in arr if i <=d]

if n == 1:
    print(m)
else:
    print(max(div(m, m/n)))