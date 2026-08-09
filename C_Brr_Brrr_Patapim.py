t = int(input())
for i in range(t):
    n = int(input())
    grid = []
    for i in range(n):
        row = input().split()
        num = []
        for val in row:
            num.append(int(val))
        grid.append(num)
    p = [0] * (2 * n + 1)
    for j in range(n):
        p[2 + j] = grid[0][j]
    for i in range(1, n):
        p[i + 1 + n] = grid[i][n - 1]
        
    total = (2 * n) * (2 * n + 1) // 2
    sum = 0
    for idx in range(2, 2 * n + 1):
        sum += p[idx]
        
    p[1] = total - sum
    for idx in range(1, 2 * n + 1):
        print(p[idx], end=" ")
    print()  