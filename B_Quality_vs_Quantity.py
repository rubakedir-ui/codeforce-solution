t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    a.sort()
    
    blue_sum = a[0] + a[1]
   
    red_sum = a[n - 1]
    
   
    left = 1       
    right = n - 1 
    
    possible = False
    
    while left < right:
        if red_sum > blue_sum:
            possible = True
            break
        
        left = left + 1
        right = right - 1
        
        if left < right:
            blue_sum = blue_sum + a[left]
            red_sum = red_sum + a[right]
            
    if possible:
        print("YES")
    else:
        print("NO")