t = int(input())
for i in range(t):
    k, q = map(int, input().split())
    a = list(map(int, input().split()))
    Q = list(map(int, input().split()))
    a1 = a[0]
    ans = []
    for i in Q:
        if i < a1:
            ans.append(i)
        else:
            ans.append(a1 - 1)
    print(*ans)