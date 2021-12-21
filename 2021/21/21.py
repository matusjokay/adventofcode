#!/usr/bin/env python3


from functools import cache


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


@cache
def play(play_cur, play_next, score_cur=0, score_next=0, move=None):
    if move:
        # update state of the game board for a player in this turn
        play_cur = (play_cur + move) % 10
        if not play_cur:
            play_cur = 10
        score_cur += play_cur

        # check win condition
        if score_cur >= 21:
            return 0, 1

    # if no player wins, go to the next turn of the game:
    # split the universe into **seven** copies
    # (reduced states after three rolls of Dirac dice)
    dd = {3:1, 4:3, 5:6, 6:7, 7:6, 8:3, 9:1}
    win = [0, 0]
    for move in dd:
        ret = play(play_next, play_cur, score_next, score_cur, move)
        win = win[0] + ret[1] * dd[move], win[1] + ret[0] * dd[move]
    return win


def partB(board):
    res = play(board[1], board[0])
    print(max(res))


#players = [4, 8]
players = [3, 4]
partA(players[:])
partB(players[:])
