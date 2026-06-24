t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = (a[-1] - a[0] + 1) // 2

    print(ans)