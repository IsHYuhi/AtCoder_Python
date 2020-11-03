c = int(input())
nml = [list(map(int, input().split())) for _ in range(c)]
n_min = 1
m_min = 1
l_min = 1

for i in nml:
    i.sort()
    n_min = max(n_min, i[0])
    m_min = max(m_min, i[1])
    l_min = max(l_min, i[2])

print(n_min*m_min*l_min)
