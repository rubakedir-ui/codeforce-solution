t = int(input())

for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    sum = 0
    min_height = 2 * 10**18 
    
    ans = []
    
    for i in range(n):
        sum += a[i]
        possible_height = sum // (i + 1)
        min_height = min(min_height, possible_height)
        ans.append(min_height)
    print(*ans)
