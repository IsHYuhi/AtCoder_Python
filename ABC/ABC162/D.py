def main():
    n = int(input())
    s = input()
    r, g, b = s.count('R'), s.count('G'), s.count('B')
    ans = r*g*b

    for i in range(n-2):
        for j in range(i+1, n-1):
            k = 2*j-i
            if 0 <= k < n:
                if s[i] != s[j] and s[j] != s[k] and s[k] != s[i]:
                    ans -= 1
    print(ans)

if __name__ == '__main__':
    main()