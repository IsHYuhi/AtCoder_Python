a, b = map(int, input().split())

idx = 0
scale = 2
xor_count = [0]*40

for idx in range(0, 40):
    bc = ((b+1)//scale)*(scale//2)+max(0, (b+1)%scale - scale//2)
    ac = (a//scale)*(scale//2)+max(0, a%scale - scale//2)
    xor_count[idx] =  bc-ac

    scale *= 2

ans = '0b'+''.join(list(map(str,[i%2 for i in xor_count[::-1]])))
print(int(ans, 0))