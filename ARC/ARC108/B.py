from collections import deque
n = int(input())
s = deque(input())
st = []
count = 0
while s:
    st.append(s.popleft())
    if 'fox' == ''.join(st[-3::]):
        count += 1
        [st.pop() for i in range(3)]
print(n - count*3)