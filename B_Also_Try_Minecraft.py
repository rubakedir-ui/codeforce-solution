n, m = map(int, input().split())
a = list(map(int, input().split()))
left = [0] * n
for i in range(1, n):
    if a[i - 1] > a[i]:
        ans = a[i - 1] - a[i]
    else:
        ans = 0
    left[i] = left[i - 1] + ans
right = [0] * n
for i in range(n - 2, -1, -1):
    if a[i + 1] > a[i]:
        ans = a[i + 1] - a[i]
    else:
       ans = 0
    right[i] = right[i + 1] + ans
for i in range(m):
    s, t = map(int, input().split())
    s = s - 1
    t = t - 1
    if s < t:
        print(left[t] - left[s])
    else:
        print(right[t] - right[s])