t = int(input())
for k in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    ans = True
    i = 0
    while i < n:
        count = 0
        j = i
        while j < n and s[j] == s[i]:
            count += 1
            j += 1
        if count == 1:
            ans = False
            break
            
        i = j
    if not ans:
        print(-1)
    else:
        p = [0] * n
        i = 0
        while i < n:
            j = i
            while j < n and s[j] == s[i]:
                j += 1
            p[i] = j  
            for k in range(i + 1, j):
                p[k] = k  
            
            i = j
        for num in p:
            print(num, end=" ")
        print() 