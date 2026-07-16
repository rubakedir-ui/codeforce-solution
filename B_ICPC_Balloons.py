t = int(input())
for i in range(t):
    n = int(input())  
    s = input()       
    problems = []  
    balloons = 0
    for problem in s:
        if problem not in problems:
            balloons += 2
            problems.append(problem)
        else:
            balloons += 1
    print(balloons)