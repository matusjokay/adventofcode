#!/usr/bin/env python3


def partA(board):
    player = 1
    score = [0, 0]
    turn = 0

    for i in range(1, 10_000, 3):
        turn += 3

        player = (player + 1) % 2
        board[player] = (board[player] + 3*i + 3) % 10
        if not board[player]:
            board[player] = 10

        score[player] += board[player]
        if score[player] >= 1000:
            print(turn, score[(player+1)%2], score[(player+1)%2] * turn)
            return


def play(board, score=[0, 0], move=None, turn=1):
    # reduced states after three rolls of Dirac dice
    dd = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}

    if move:
        # update state of the game board for a player in this turn
        board[turn % 2] = (board[turn % 2] + move) % 10
        if not board[turn % 2]:
            board[turn % 2] = 10
        score[turn % 2] += board[turn % 2]

        # check win condition: res[0] is set to 1 if player 1 wins,
        # res[1] is set to 1 if player 2 wins
        res = [0, 0]
        if score[turn % 2] >= 21:
            res[turn % 2] = 1
            return res

    # if no player wins, go to the next turn of the game:
    # split the universe into **seven** copies
    # (reduced states after three rolls of Dirac dice)
    win = [0, 0]
    for move in dd:
        ret = play(board[:], score[:], move, turn+1)
        win = win[0] + ret[0] * dd[move], win[1] + ret[1] * dd[move]
    return win


def partB(board):
    res = play(board)
    print(max(res))


#players = [4, 8]
players = [3, 4]
partA(players[:])
partB(players[:])
