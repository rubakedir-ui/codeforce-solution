t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    for i in range (n):
        if a[i] <= i+1:
            count+=1
    print (count)