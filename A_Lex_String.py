t = int(input())

for i in range(t):
    n, m, k = map(int, input().split())
    a = sorted(input())
    b = sorted(input())

    i = 0
    j = 0
    countA = 0
    countB = 0

    ans = []
    while i < n and j < m:
        if (a[i] < b[j] and countA < k) or countB == k:
            ans.append(a[i])
            i += 1
            countA += 1
            countB = 0
        else:
            ans.append(b[j])
            j += 1
            countB += 1
            countA = 0

    print("".join(ans))