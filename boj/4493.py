First_for = int(input())

for i in range(First_for):
    player_1 = player_2 = 0
    Second_for = int(input())
    for j in range(Second_for):
        p1, p2 = input().split()
        if p1 == p2:
            continue
        elif p1 == 'R' and p2 == 'S' or p1 == 'S' and p2 == 'P' or p1 == 'P' and p2 == 'R':
            player_1 += 1
        else:
            player_2 += 1
    if player_1 > player_2:
        print("Player 1")
    elif player_1 == player_2:
        print("TIE")
    elif player_1 < player_2:
        print("Player 2")