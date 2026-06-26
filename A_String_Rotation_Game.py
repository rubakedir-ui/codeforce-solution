t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    count = 0

    for i in range(n):
        if s[i] != s[(i + 1) % n]:
            count += 1

    if count == n:
        print(n)
    else:
        print(count + 1)