t = int(input())

for _ in range(t):
    n = int(input())
    s = input()
    
    target_char = s[n - 1]
    
    operations = 0
    
    for i in range(n):
        if s[i] != target_char:
            operations = operations + 1
            
    print(operations)