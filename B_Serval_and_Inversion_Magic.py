t = int(input())
for i in range(t):
    n = int(input())
    s = input()
    
    started = False
    ended = False
    possible = True
    
    for i in range(n // 2):
        left = s[i]
        right = s[n - 1 - i]
        
        if left!= right:
            
            if ended:
                possible = False
                break
            
            started = True
            
        else:
            if started:
                ended = True
    if possible:
        print("Yes")
    else:
        print("No")