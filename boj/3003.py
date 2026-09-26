chess_input = list(map(int, input().split()))
chess_Right = [1, 1, 2, 2, 2, 8]
chess_print = []

for i in range(len(chess_input)):
    if chess_input[i] != chess_Right[i]:
        chess_print.append(chess_Right[i] - chess_input[i])
    else:
        chess_print.append(0)
    print(chess_print[i], end = ' ')