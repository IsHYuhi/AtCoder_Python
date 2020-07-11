h, w = map(int, input().split())

field = [input() for _ in range(h)]

print('#'*(w+2))
for f in field:
    print('#'+f+'#')
print('#'*(w+2))