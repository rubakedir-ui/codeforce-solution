t = int(input())
for i in range(t):
    n, m = map(int, input().split())
    p = list(map(int, input().split()))

    ans = [-1] * n
    x = set()
    count = 0
    for num in range(m):
        post = p[num]
        t = num + 1  
        if post not in x:
            x.add(post)
            count += 1
            post= n - count
            ans[post] = t
            
            if count == n:
                break
    for t in ans:
        print(t , end=" ")
    print()  