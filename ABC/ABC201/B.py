n = int(input())
st = []
for _ in range(n):
    s, t = input().split()
    st.append([s, int(t)])

st.sort(reverse=True, key=lambda x: x[1])
print(st[1][0])