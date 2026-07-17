t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    sort = sorted(s)
    max1 = sort[-1]  
    max2 = sort[-2] 
    for i in range(n):
        if s[i] == max1:
            advantage = s[i] - max2
        else:
            advantage = s[i] - max1
            
        print(advantage, end=" ")
    print()