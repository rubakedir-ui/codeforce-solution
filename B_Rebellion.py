t = int(input())


for _ in range(t):
    
    n = int(input())
    a = [int(x) for x in input().split()]
    
    left = 0
    right = n - 1
    ans = 0
    while left < right:
        
        if a[left] == 0:
            left += 1
            
        elif a[right] == 1:
            right -= 1
            
        else:
           ans += 1 
           left += 1       
           right -= 1      
            
    print(ans)