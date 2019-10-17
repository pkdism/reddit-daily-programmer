s = input()

n_players = 2
scores = [0]*11
striker = 0
non_striker = 1
balls = 0
extras = 0
for i in s:
    if balls == 6:
        striker, non_striker = non_striker, striker
        balls = 0
    if i >= '1' and i <= '9':
        scores[striker] += int(i)
        # print('run ', int(i))
        if int(i)%2 == 1:
            striker, non_striker = non_striker, striker
        balls += 1
    elif i == '.':
        balls += 1
        # continue
    elif i == 'b':
        extras += 1
        balls += 1
    elif i == 'w':
        extras += 1
    elif i == 'W':
        striker += max(striker, non_striker) + 1
        balls += 1
        n_players += 1
    # print(balls)
    # print(striker)
    # print(non_striker)
    # print(scores)
    # print("")

for i in range(n_players+1):
    print('P' + str(i+1) + ": " + str(scores[i]))
print('Extras: ' + str(extras))
