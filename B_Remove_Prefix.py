t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    num = set()
    count= 0
    for i in range(n - 1, -1, -1):
        ans= a[i]
        if ans in num:
            count = i + 1
            break
        num.add(ans)
    print(count)