t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for x in input().split():
        a.append(int(x))
    freq = {}
    max_freq = 0
    
    for num in a:
        if num in freq:
            freq[num] = freq[num] + 1
        else:
            freq[num] = 1
            
        if freq[num] > max_freq:
            max_freq = freq[num]
            
    required_count = (n + 1) // 2
    if max_freq >= required_count:
        print("YES")
    else:
        print("NO")