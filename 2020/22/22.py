#!/bin/env python3


def read_input(fname):
    players = []
    for line in open(fname):
        line = line.strip()
        if line.startswith('Player'):
            decks = []
            continue
        elif not line:
            players += [decks]
            continue

        decks.append(int(line))

    return players


def game(players, recurse = False):
    state = [set(), set()]

    while players[0] and players[1]:
        # end infinite recursion
        if tuple(players[0]) in state[0] or tuple(players[1]) in state[1]:
            winner = 0
            break
        state[0].add(tuple(players[0]))
        state[1].add(tuple(players[1]))

        # sub-game
        if recurse and (len(players[0][1:]) >= players[0][0]) and (len(players[1][1:]) >= players[1][0]):
            winner, _ = game([players[0][1:players[0][0]+1], players[1][1:players[1][0]+1]], True)

        # normal round game
        else:
            if players[0][0] > players[1][0]:
                winner = 0
            else:
                winner = 1

        players[winner].append(players[winner].pop(0))
        players[winner].append(players[(winner+1)%2].pop(0))

    return (winner, players[winner])


players = read_input('input.txt')
# part 1
_, winner = game([players[0][:],players[1][:]])
print(sum(list([(i+1)*w for i,w in enumerate(winner[::-1])])))
# part 2
_, winner = game([players[0][:], players[1][:]], recurse=True)
print(sum(list([(i+1)*w for i,w in enumerate(winner[::-1])])))
