a, b = map(int, input().split())
ans = 0

def select_button(a, b):
    ten = abs(abs(b-a)-10)
    five = abs(abs(b-a)-5)
    one = abs(abs(b-a)-1)

    return min(ten, five, one)

def neg(a, b):
    if b>a:
        return -1
    else:
        return 1

while abs(b-a)!=0:
    ans += 1
    a = b+select_button(a, b)

print(ans)
