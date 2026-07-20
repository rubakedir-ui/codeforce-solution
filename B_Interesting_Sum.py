t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    max = (a[-1] + a[-2]) - (a[0] + a[1])
    print(max)