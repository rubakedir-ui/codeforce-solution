t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    mex = []
    ans = []
    for num in a:
        if num not in mex:
            mex.append(num)
        else:
            ans.append(num)
    ans = mex + ans
    print(*ans)