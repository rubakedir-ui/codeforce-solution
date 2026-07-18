t = int(input())
for i in range(t):
    n = int(input())
    players = [input().split(), input().split(), input().split()]
    
    count = {}
    for p in players:
        for word in p:
            count[word] = count.get(word, 0) + 1
    scores = [0, 0, 0]
    for i in range(3):
        for word in players[i]:
            if count[word] == 1:
                scores[i] += 3
            elif count[word] == 2:
                scores[i] += 1
    print(scores[0], scores[1], scores[2])