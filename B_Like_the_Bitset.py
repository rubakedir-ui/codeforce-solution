t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    s = input().strip()
    max = 0
    current = 0
    for char in s:
        if char == "1":
            current = current + 1
            if current > max:
                max = current
        else:
            current = 0
    if max >= k:
        print("NO")
    else:
        print("YES")
        total = 0
        for char in s:
            if char == "1":
                total= total + 1
        ones = 1
        ans = total + 1
        for char in s:
            if char == "1":
                print(ones, end=" ")
                ones = ones + 1
            else:
                print(ans, end=" ")
                ans = ans + 1
        print() 
