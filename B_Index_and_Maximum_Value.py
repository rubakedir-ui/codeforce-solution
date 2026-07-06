t = int(input())

for i in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    current_max = max(a)
    ans = []

    for i in range(m):
        parts = input().split()
        op = parts[0]
        l = int(parts[1])
        r = int(parts[2])
        
        if l <= current_max <= r:
            if op == '+':
                current_max += 1
            elif op == '-':
                current_max -= 1
        ans.append(current_max)
    print(*ans)