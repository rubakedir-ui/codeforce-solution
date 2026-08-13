t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    found = False
    ones1 = 0
    others1 = 0
    for i in range(n - 2):
        if a[i] == 1:
            ones1 += 1
        else:
            others1 += 1
        if ones1 >= others1:
            ones_twos2 = 0
            threes2 = 0
            for j in range(i + 1, n - 1):
                if a[j] == 3:
                    threes2 += 1
                else:
                    ones_twos2 += 1
                if ones_twos2 >= threes2:
                    found = True
                    break
        if found:
            break
    if found:
        print("YES")
    else:
        print("NO")