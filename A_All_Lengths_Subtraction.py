t = int(input())

for i in range(t):
    n = int(input())
    D = list(map(int, input().split()))
    
    possible = True
    for k in range(n, 0, -1):
        subarray = False
        for l in range(n - k + 1):
            positive = True
            for i in range(l, l + k):
                if D[i] <= 0:
                    positive = False
                    break
            if positive:
                for i in range(l, l + k):
                    D[i] -= 1
                subarray = True
                break 
        if not subarray:
            possible = False
            break
    if possible:
        print("YES")
    else:
        print("NO")