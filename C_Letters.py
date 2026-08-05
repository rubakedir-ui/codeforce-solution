n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dorm = 0 
sum = 0  
for num in b:
    while num > sum + a[dorm]:
        sum = sum + a[dorm]
        dorm = dorm + 1
    dorm_num = dorm + 1
    room = num - sum

    print(dorm_num, room)