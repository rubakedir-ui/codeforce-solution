t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))  
    b = list(map(int, input().split()))
    courses = []
    for i in range(n):
        courses.append((b[i], i + 1))
    courses.sort(reverse=True)
    ans = []
    for level, idx in courses:
        while level <= k:
            ans.append(idx)
            level += 1

    print(len(ans))
    print(*ans)