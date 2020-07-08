s = input()
for i, st in enumerate(s):
    if st=='A':
        start = i
        break
for i, st in enumerate(s):
    if st=='Z':
        end = i
print(end-start+1)