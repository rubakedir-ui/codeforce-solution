t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    cnt = 0

    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            cnt += 1

    if cnt == n:
        print(n)
    else:
        print(cnt + 1)