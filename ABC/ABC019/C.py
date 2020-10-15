n = int(input())
a = list(map(int, input().split()))

def check_core(n):
    for i in range(1, 31):
        if n%2 == 0:
            n = n//2
        else:
            return n

a = [check_core(i) for i in a]

print(len(set(a)))