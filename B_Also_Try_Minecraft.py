first_line = input().split()
n = int(first_line[0])
m = int(first_line[1])

heights = []
for x in input().split():
    heights.append(int(x))

pref_lr = [0] * n
for i in range(1, n):
    if heights[i-1] > heights[i]:
        damage = heights[i-1] - heights[i]
    else:
        damage = 0
    pref_lr[i] = pref_lr[i-1] + damage

pref_rl = [0] * n
for i in range(n-2, -1, -1):
    if heights[i+1] > heights[i]:
        damage = heights[i+1] - heights[i]
    else:
        damage = 0
    pref_rl[i] = pref_rl[i+1] + damage
for i in range(m):
    quest = input().split()
    s = int(quest[0]) - 1 
    t = int(quest[1]) - 1
    
    if s < t:
        ans = pref_lr[t] - pref_lr[s]
        print(ans)
    else:
        ans = pref_rl[t] - pref_rl[s]
        print(ans)