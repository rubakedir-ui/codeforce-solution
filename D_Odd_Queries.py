t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    ans = [0] * (n + 1)
    for i in range(1, n + 1):
        ans[i] = ans[i - 1] + a[i - 1]
        
    total_sum = ans[n]
    for _ in range(q):
        l, r, k = map(int, input().split())

        original_sum = ans[r] - ans[l - 1]
        new_sum = (r - l + 1) * k
        new_total_sum = total_sum - original_sum + new_sum
        if new_total_sum % 2 != 0:
            print("YES")
        else:
            print("NO")